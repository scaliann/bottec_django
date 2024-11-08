from django.contrib import admin
from .models import Category, SubCategory, Product, Cart, CartItem

# Регистрация модели Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)

# Регистрация модели SubCategory
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    ordering = ('category', 'name')

# Регистрация модели Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory', 'price', 'created_at')
    search_fields = ('name', 'subcategory__name')
    list_filter = ('subcategory',)
    ordering = ('subcategory', 'name')
    readonly_fields = ('created_at',)

# Регистрация модели Cart
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'is_confirmed')
    list_filter = ('is_confirmed',)
    search_fields = ('user__username',)
    ordering = ('-created_at',)

# Регистрация модели CartItem
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    search_fields = ('cart__user__username', 'product__name')
    ordering = ('cart',)


