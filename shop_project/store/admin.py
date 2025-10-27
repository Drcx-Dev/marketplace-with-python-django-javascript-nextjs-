from django.contrib import admin
from .models import Category,Product,CustomUser
from django.contrib.auth.admin import UserAdmin

@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'available')
    list_filter = ('available', 'category')
    search_fields = ('name','description')

@admin.register(CustomUser)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["email", "username", "is_staff", "is_active"]  
    list_filter = ["is_staff", "is_active", "role"]  
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("role", "avatar")}),  
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("role", "avatar")}),
    )