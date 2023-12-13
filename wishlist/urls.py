from django.urls import path
from . import views
from .views import WishlistView, add_to_wishlist, remove_from_wishlist

urlpatterns = [
    path('', views.WishlistView.as_view(), name='wishlist'),
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]


# urlpatterns = [
#     path('', views.checkout, name='checkout'),
#     path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
#     path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
#     path('wh/', webhook, name='webhook'),
# ]

# urlpatterns = [
#     path('', views.view_bag, name='view_bag'),
#     path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
#     path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
#     path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
# ]

# urlpatterns = [
#     path('', views.all_products, name='products'),
#     path('<int:product_id>/', views.product_detail, name='product_detail'),
#     path('add/', views.add_product, name='add_product'),
#     path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
#     path('delete/<int:product_id>/', views.delete_product, name='delete_product'),

# ]