from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, Client
from django.contrib.messages import get_messages
from django.urls import reverse
from profiles.models import UserProfile
from wishlist.models import Wishlist
from products.models import Product



class ViewWishlistTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def test_authenticated_user_view_wishlist(self):
        user_profile = UserProfile.objects.get_or_create(user=self.user)
        wishlist = Wishlist.objects.create(user=self.user)
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("wishlist"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "wishlist/wishlist.html")
        self.assertEqual(response.context["wishlist"], wishlist)

    def test_unauthenticated_user_view_wishlist(self):
        response = self.client.get(reverse("wishlist"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("account_login"))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn(
            "Sorry, you need to be logged in to add to your Wishlist.", messages
        )


class AddWishlistTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.product = Product.objects.create(
            name="Test Product",
            description="Test description",
            price="9.99",
        )

    def test_authenticated_user_add_wishlist(self):
        user_profile = UserProfile.objects.get_or_create(user=self.user)
        self.client.force_login(self.user)
        response = self.client.post(reverse("add_wishlist", args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url, reverse("products")
        )
        wishlist = Wishlist.objects.get(user=self.user)
        self.assertIn(self.product, wishlist.products.all())
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn(
            f"{self.product.name} has been added to your Wishlist!", messages
        )

    def test_unauthenticated_user_view_wishlist(self):
        response = self.client.get(reverse("wishlist"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("account_login"))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn(
            "Sorry, you need to be logged in to add to your Wishlist.", messages
        )


class RemoveWishlistTest(TestCase):

    def setUp(self):

        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.product = Product.objects.create(
            name="Test Product",
            description="Test description",
            price="9.99",
        )
        self.wishlist = Wishlist.objects.create(user=self.user)
        self.wishlist.products.add(self.product)

    def test_remove_wishlist(self):

        self.client.force_login(self.user)
        response = self.client.post(reverse("remove_wishlist", args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("products"))
        self.assertFalse(self.wishlist.products.filter(pk=self.product.id).exists())
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn(
            f"{self.product.name} has been removed from your Wishlist!", messages
        )

    def test_remove_wishlist_unauthenticated_user(self):
        response = self.client.post(reverse("remove_wishlist", args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("account_login"))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn(
            "Sorry, you need to be logged in to edit your Wishlist.", messages
        )

