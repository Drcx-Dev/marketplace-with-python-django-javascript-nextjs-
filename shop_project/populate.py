import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_project.settings')
django.setup()

from store.models import Category, Product

# Создание категорий
categories = [
    {'name': 'Электроника', 'slug': 'electronics'},
    {'name': 'Компьютеры', 'slug': 'computers'},
    {'name': 'Одежда', 'slug': 'clothing'},
]

for cat_data in categories:
    Category.objects.get_or_create(**cat_data)

# Создание продуктов
products = [
    {'name': 'Ноутбук', 'category_id': 2, 'description': 'Мощный ноутбук', 'price': 50000, 'stock': 10},
    {'name': 'Смартфон', 'category_id': 1, 'description': 'Современный смартфон', 'price': 30000, 'stock': 20},
    {'name': 'Футболка', 'category_id': 3, 'description': 'Удобная футболка', 'price': 1000, 'stock': 50},
]

for prod_data in products:
    Product.objects.get_or_create(**prod_data)

print("Тестовые данные добавлены!")