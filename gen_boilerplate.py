import os

base = r'c:\Users\Dishambha Awasthi\OneDrive\Desktop\ecom website\ecommerce'

apps = {
    'users': {
        'verbose': 'Users',
        'admin_models': 'from .models import User, Address\n\nadmin.site.register(User)\nadmin.site.register(Address)\n',
    },
    'products': {
        'verbose': 'Products',
        'admin_models': 'from .models import Category, Product, ProductImage\n\nadmin.site.register(Category)\nadmin.site.register(Product)\nadmin.site.register(ProductImage)\n',
    },
    'cart': {
        'verbose': 'Cart',
        'admin_models': 'from .models import Cart, CartItem\n\nadmin.site.register(Cart)\nadmin.site.register(CartItem)\n',
    },
    'orders': {
        'verbose': 'Orders',
        'admin_models': 'from .models import Order, OrderItem\n\nadmin.site.register(Order)\nadmin.site.register(OrderItem)\n',
    },
    'wishlist': {
        'verbose': 'Wishlist',
        'admin_models': 'from .models import Wishlist, WishlistItem\n\nadmin.site.register(Wishlist)\nadmin.site.register(WishlistItem)\n',
    },
}

for app, info in apps.items():
    app_dir = os.path.join(base, 'apps', app)

    open(os.path.join(app_dir, '__init__.py'), 'w').close()

    with open(os.path.join(app_dir, 'admin.py'), 'w') as f:
        f.write('from django.contrib import admin\n' + info['admin_models'])

    with open(os.path.join(app_dir, 'apps.py'), 'w') as f:
        f.write(
            'from django.apps import AppConfig\n\n\n'
            f'class {info["verbose"]}Config(AppConfig):\n'
            '    default_auto_field = "django.db.models.BigAutoField"\n'
            f'    name = "apps.{app}"\n'
            f'    verbose_name = "{info["verbose"]}"\n'
        )

    with open(os.path.join(app_dir, 'views.py'), 'w') as f:
        f.write(f'# Views for the {app} app\n')

    with open(os.path.join(app_dir, 'urls.py'), 'w') as f:
        f.write(
            'from django.urls import path\n'
            'from . import views\n\n'
            f'app_name = "{app}"\n\n'
            'urlpatterns = [\n'
            '    # Add your URL patterns here\n'
            ']\n'
        )

print('All app boilerplate files created successfully.')
