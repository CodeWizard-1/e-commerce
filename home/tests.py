from django.test import TestCase
from django.urls import reverse
from django.core import mail
from django.contrib.messages import get_messages
from products.models import Product


class HomeViewTest(TestCase):

    def test_home_view(self):

        Product.objects.create(
            name="Product 1", description="Description 1", price=9.99
        )
        Product.objects.create(
            name="Product 2", description="Description 2", price=19.99
        )


        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)


        self.assertTemplateUsed(response, "home/index.html")

        products = response.context["products"]
        self.assertEqual(products.count(), 2)




class PrivacyPolicyViewTest(TestCase):


    def test_privacy_policy_view(self):
        response = self.client.get(reverse("privacy_policy"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/privacy_policy.html")


class ContactViewTest(TestCase):

    def test_contact_view_get(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/contact.html")

    def test_contact_view_post(self):
        response = self.client.post(
            reverse("contact"),
            {
                "name": "Test User",
                "email": "test@test.com",
                "message": "This is a test message.",
            },
        )

        self.assertEqual(response.status_code, 302)

        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn(
            "Thank you, your email has been sent. We will contact you shortly.",
            messages,
        )