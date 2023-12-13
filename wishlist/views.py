from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Wishlist, Product

class WishlistView(View):
    def get(self, request):

        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        return render(request, 'wishlist.html', {'wishlist': wishlist})

@login_required
def add_to_wishlist(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product not found")

    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    return redirect('wishlist')

@login_required
def remove_from_wishlist(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product not found")

    wishlist = Wishlist.objects.get(user=request.user)
    wishlist.products.remove(product)
    return redirect('wishlist')