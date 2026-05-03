from django.contrib import admin
from django.urls import path, include
from apps.products.views import home
from core.views import subscribe_newsletter

urlpatterns = [
    path("", home, name="home"),
    path("subscribe/", subscribe_newsletter, name="subscribe"),
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.users.urls", namespace="users")),
    path("products/", include("apps.products.urls", namespace="products")),
    path("cart/", include("apps.cart.urls", namespace="cart")),
    path("orders/", include("apps.orders.urls", namespace="orders")),
    path("wishlist/", include("apps.wishlist.urls", namespace="wishlist")),
]
