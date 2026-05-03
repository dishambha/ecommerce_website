from django.db import models
from django.conf import settings
from apps.products.models import Product
from core.models import TimeStampedModel


class Wishlist(TimeStampedModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="wishlist"
    )

    def __str__(self):
        return f"Wishlist of {self.user.email}"


class WishlistItem(TimeStampedModel):
    wishlist = models.ForeignKey(
        Wishlist, on_delete=models.CASCADE, related_name="items"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("wishlist", "product")

    def __str__(self):
        return self.product.name
