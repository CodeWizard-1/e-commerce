from django.shortcuts import render, redirect
from products.models import Product
from .forms import ContactForm
from django.contrib import messages
import random

# View for rendering the home page
def index(request):
    # Retrieve all products from the database
    products = Product.objects.all()
    # Retrieve featured products and limit to 5 if more than 5 are available
    featured_products = list(Product.objects.filter(is_featured=True))
    if len(featured_products) > 5:
        featured_products = random.sample(featured_products, 5)

    context = {
        "products": products,
        "featured_products": featured_products,
    }
    return render(request, "home/index.html", context)

# View for rendering the privacy policy page
def privacy_policy(request):

    return render(request, "home/privacy_policy.html")

# View for rendering the returns page
def returns(request):

    return render(request, "home/returns.html")

# View for handling the contact form submission
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you, your email has been sent. We will contact you shortly.",  # noqa
            )
            return redirect("contact")
        else:
            messages.error(
                request, "Form submission failed. Please check the form and try again."  # noqa
            )
    else:
        form = ContactForm()

    context = {
        "form": form,
    }

    return render(request, "home/contact.html", context)
