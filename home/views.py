from django.shortcuts import render, redirect
from products.models import Product
from .forms import ContactForm
from django.contrib import messages


def index(request):
    return render(request, 'home/index.html')

def privacy_policy(request):
    """
    FAQs Page
    """
    return render(request, "home/privacy_policy.html")


def contact(request):
    """
    View to return Contact Us form
    """

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
