from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='home'),
    path("privacy_policy", views.privacy_policy, name="privacy_policy"),
    path("returns", views.returns, name="returns"),
    path("contact", views.contact, name="contact"),
]