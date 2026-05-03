import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

from apps.products.models import Category, Product, ProductImage

def seed_data():
    print("Seeding database...")
    
    # 1. Categories
    electronics, _ = Category.objects.get_or_create(name="Electronics")
    fashion, _ = Category.objects.get_or_create(name="Fashion")
    accessories, _ = Category.objects.get_or_create(name="Accessories")

    # 2. Products
    p1, created1 = Product.objects.get_or_create(
        name="Premium Wireless Earbuds",
        defaults={
            'category': electronics,
            'description': "Noise-cancelling, premium sound quality, 24-hour battery life with charging case.",
            'price': 149.99,
            'discount_percent': 10,
            'stock': 50
        }
    )
    if created1:
        ProductImage.objects.create(
            product=p1,
            image_url="https://images.unsplash.com/photo-1590658268037-6bf12165a8df?auto=format&fit=crop&w=500&q=60",
            alt_text="Wireless Earbuds",
            is_primary=True
        )

    p2, created2 = Product.objects.get_or_create(
        name="Ultra-Thin Smart Watch",
        defaults={
            'category': electronics,
            'description': "Health and fitness tracking, custom watch faces, water resistant, up to 7 days battery.",
            'price': 199.99,
            'discount_percent': 0,
            'stock': 30
        }
    )
    if created2:
        ProductImage.objects.create(
            product=p2,
            image_url="https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=500&q=60",
            alt_text="Smart Watch",
            is_primary=True
        )

    p3, created3 = Product.objects.get_or_create(
        name="Minimalist Canvas Backpack",
        defaults={
            'category': accessories,
            'description': "Spacious interior, water-resistant canvas, padded laptop compartment.",
            'price': 69.99,
            'discount_percent': 15,
            'stock': 100
        }
    )
    if created3:
        ProductImage.objects.create(
            product=p3,
            image_url="https://images.unsplash.com/photo-1553062407-98eeb94c6a62?auto=format&fit=crop&w=500&q=60",
            alt_text="Backpack",
            is_primary=True
        )

    p4, created4 = Product.objects.get_or_create(
        name="Premium Leather Wallet",
        defaults={
            'category': accessories,
            'description': "Genuine leather, slim profile, RFID blocking protection.",
            'price': 45.00,
            'discount_percent': 0,
            'stock': 75
        }
    )
    if created4:
        ProductImage.objects.create(
            product=p4,
            image_url="https://images.unsplash.com/photo-1627123424574-724758594e93?auto=format&fit=crop&w=500&q=60",
            alt_text="Leather Wallet",
            is_primary=True
        )

    print("Seeding completed successfully!")

if __name__ == '__main__':
    seed_data()
