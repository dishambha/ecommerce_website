from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.products.models import Product
from .models import Wishlist, WishlistItem


def get_or_create_wishlist(user):
    wishlist, _ = Wishlist.objects.get_or_create(user=user)
    return wishlist


@login_required
def wishlist_detail(request):
    from django.shortcuts import render
    wishlist = get_or_create_wishlist(request.user)
    return render(request, "wishlist/detail.html", {"wishlist": wishlist})


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist = get_or_create_wishlist(request.user)
    WishlistItem.objects.get_or_create(wishlist=wishlist, product=product)
    messages.success(request, f'"{product.name}" added to wishlist.')
    return redirect("wishlist:detail")


@login_required
def remove_from_wishlist(request, item_id):
    item = get_object_or_404(WishlistItem, id=item_id, wishlist__user=request.user)
    item.delete()
    messages.success(request, "Removed from wishlist.")
    return redirect("wishlist:detail")
