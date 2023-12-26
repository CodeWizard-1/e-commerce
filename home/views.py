from django.shortcuts import render, redirect
from products.models import Product
from .forms import ContactForm
from django.contrib import messages
import random


def index(request):

    products = Product.objects.all()

    featured_products = list(Product.objects.filter(is_featured=True))
    if len(featured_products) > 5:
        featured_products = random.sample(featured_products, 5)

    context = {
        "products": products,
        "featured_products": featured_products,
    }
    return render(request, "home/index.html", context)






def privacy_policy(request):

    return render(request, "home/privacy_policy.html")

def returns(request):

    return render(request, "home/returns.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you, your email has been sent. We will contact you shortly.",
            )
            return redirect("contact")
        else:
            messages.error(
                request, "Form submission failed. Please check the form and try again."
            )
    else:
        form = ContactForm()

    context = {
        "form": form,
    }

    return render(request, "home/contact.html", context)
