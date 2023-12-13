from django.urls import path
from . import views
from .views import WishlistView, add_to_wishlist, remove_from_wishlist

urlpatterns = [
    path('', views.WishlistView.as_view(), name='wishlist'),
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]
