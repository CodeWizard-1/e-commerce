from django.contrib import admin
from .models import Product, Category, ProductVariant, Brand, Reviews

class ProductVariantInline(admin.StackedInline):
    model = ProductVariant
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'sale_price',
        'rating',
        'brand',
        'on_sale',
        'discount',
        'discounted_price',
        'created_on',
    )

    ordering = ('sku',)
    inlines = [ProductVariantInline]

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductVariantAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'clothing_size',
        'men_shoe_size',
        'women_shoe_size',
        'child_shoe_size',
        'color',
        'stock_quantity',
        'gender',
    )

class BrandAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )

class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "user",
        "title",
        "review",
        "created_on",
        "updated_on",
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductVariant, ProductVariantAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Reviews, ReviewsAdmin)

