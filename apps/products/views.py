from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def home(request):
    featured = Product.objects.filter(is_active=True).order_by('-created_at')[:8]
    categories = Category.objects.all()[:6]
    return render(request, 'home.html', {
        'featured_products': featured,
        'categories': categories,
    })


def product_list(request):
    products = Product.objects.filter(is_active=True).select_related("category").prefetch_related("images")
    category_slug = request.GET.get("category")
    if category_slug:
        products = products.filter(category__slug=category_slug)
    categories = Category.objects.all()
    return render(request, "products/list.html", {
        "products": products,
        "categories": categories,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "products/detail.html", {"product": product})
