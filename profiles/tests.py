from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from profiles.models import UserProfile
from profiles.views import profile, order_history
from profiles.forms import UserProfileForm
from checkout.models import Order
from django.urls import reverse
from django.shortcuts import get_object_or_404


class TestProfilesViews(TestCase):
    # Set up a test user for authentication
    def setUp(self):
        testuser = User.objects.create_user(
            username="test_username", password="secret", email="testuser@email.com"
        )
        testuser.save()

    # Test the GET request for the profile page
    def test_get_profile_page(self):
        self.client.login(username="test_username", password="secret")
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")

    # Test the POST request for the profile page
    def test_post_profile_page(self):
        self.client.login(username="test_username", password="secret")

        response = self.client.post(reverse("profile"))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "profiles/profile.html")

    # Test unauthorized POST request for the profile page
    def test_unauthorized_post_profile_page(self):

        response = self.client.post(reverse("profile"))

        self.assertEqual(response.status_code, 302)

        expected_url = f"{reverse('account_login')}?next={reverse('profile')}"
        self.assertRedirects(response, expected_url)


# Set up necessary data for order history view tests
class OrderHistoryViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.order = Order.objects.create(
            order_number="1234567890",
            user_profile=UserProfile.objects.get(user=self.user),
            full_name="Test User",
            email="testuser@email.com",
            phone_number="12345678",
            country="IE",
            postcode="12345",
            town_or_city="Dublin",
            street_address1="My Street",
            county="Anywhere",
        )

    # Test the order history view
    def test_order_history_view(self):
        self.client.login(username="testuser", password="testpass")

        response = self.client.get(reverse("order_history", args=["1234567890"]))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "checkout/checkout_success.html")
        order = response.context["order"]
        self.assertEqual(order, self.order)

        messages = [m.message for m in get_messages(response.wsgi_request)]
        expected_message = f"This is a past confirmation for order number {self.order.order_number}. A confirmation email was sent on the order date."
        self.assertIn(expected_message, messages)

