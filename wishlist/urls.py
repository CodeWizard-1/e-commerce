from django.urls import path
from .views import WishlistView, add_to_wishlist, remove_from_wishlist

urlpatterns = [
    path('', WishlistView.as_view(), name='wishlist'),
    path('add-to-wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:product_id>/', remove_from_wishlist, name='remove_from_wishlist'),
]

