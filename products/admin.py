from django.contrib import admin
from .models import Product, Category, ProductVariant, Brand, Reviews
from django_summernote.admin import SummernoteModelAdmin


class ProductVariantInline(admin.StackedInline):
    model = ProductVariant
    extra = 1


class ProductAdmin(SummernoteModelAdmin, admin.ModelAdmin):

    search_fields = [
        'name',
    ]

    list_display = (
        'name',
        'gender',
        'category',
        "is_featured",
        'price',
        'sale_price',
        'rating',
        'brand',
        'on_sale',
        'discount',
        'discounted_price',
        'created_on',
        'fit',
    )
    summernote_fields = ("materials",)
    list_editable = (
        "is_featured",
        "on_sale",
    )

    ordering = ("name",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductVariantAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'clothing_size',
        'stock_quantity',
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
