from django.contrib import admin
from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):

    search_fields = [
        "user",
    ]

    filter_horizontal = ("products",)
    list_display = (
        "user",
        "date_added",
    )

    ordering = ("user",)


admin.site.register(Wishlist, WishlistAdmin)
