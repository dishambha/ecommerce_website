from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from apps.cart.models import Cart
from .models import Order, OrderItem


@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    items = cart.items.select_related("product").all()

    if not items.exists():
        messages.error(request, "Your cart is empty.")
        return redirect("cart:detail")

    if request.method == "POST":
        shipping_address = request.POST.get("shipping_address", "").strip()
        if not shipping_address:
            messages.error(request, "Shipping address is required.")
            return render(request, "orders/checkout.html", {"cart": cart})

        with transaction.atomic():
            order = Order.objects.create(
                user=request.user,
                shipping_address=shipping_address,
                total_amount=cart.total,
            )
            for item in items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    product_name=item.product.name,
                    unit_price=item.product.discounted_price,
                    quantity=item.quantity,
                )
                # Deduct stock
                item.product.stock -= item.quantity
                item.product.save()
            items.delete()  # Clear cart after order

        messages.success(request, f"Order #{order.id} placed successfully!")
        return redirect("orders:detail", order_id=order.id)

    return render(request, "orders/checkout.html", {"cart": cart})


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "orders/history.html", {"orders": orders})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "orders/detail.html", {"order": order})
