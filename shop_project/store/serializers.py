from rest_framework import serializers
from .models import Category, Product, CustomUser,Cart, CartItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "stock", "available", "image", "category"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'avatar', 'role','is_staff', ]
        extra_kwargs = {
            'username': {'required': False},
            'email': {'required': False},
        }

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    total_price = serializers.SerializerMethodField()
     
    class Meta:
        model = CartItem
        fields = [ 'id', 'product', 'quantity', 'added_at', 'total_price']
        
    def get_total_price(self, obj):
        return obj.get_total_price()
        

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
     
    class Meta:
        model = Cart
        fields = ['id', 'user', 'session_key', 'created_at', 'items']

