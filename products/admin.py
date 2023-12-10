from django.contrib import admin
from .models import Product, Category, ProductVariant

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
        'image',
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


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductVariant, ProductVariantAdmin)

