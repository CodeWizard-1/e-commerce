from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages

from django.contrib.auth.models import User
from products.models import Product
from bag.views import view_bag, add_to_bag


class BagViewTest(TestCase):

    def test_view_bag(self):
        response = self.client.get(reverse("view_bag"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bag/bag.html")


class AddToBagViewTest(TestCase):


    def setUp(self):
        self.user = User.objects.create_user(
            username="regularuser",
            password="testpw",
        )
        self.client.force_login(self.user)
        self.product = Product.objects.create(name="Test Product", price=9.99)

    def test_add_to_bag(self):
        url = reverse("add_to_bag", args=[self.product.id])
        form_data = {
            "quantity": 2,
            "redirect_url": reverse("product_detail", args=[self.product.id]),
        }

        response = self.client.post(url, data=form_data)
        self.assertRedirects(
            response, reverse("product_detail", args=[self.product.id])
        )

        bag = self.client.session.get("bag", {})
        self.assertEqual(bag[str(self.product.id)], 2)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), f"Added {self.product.name} to your bag")


class AdjustBagTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="regularuser",
            password="testpw",
        )
        self.client.force_login(self.user)
        self.product = Product.objects.create(name="Test Product", price=9.99)

    def test_adjust_bag(self):

        form_data = {
            "quantity": 3,
        }
        response = self.client.post(
            reverse("adjust_bag", args=[self.product.id]), data=form_data
        )


        self.assertEqual(response.status_code, 302)

        bag = self.client.session.get("bag", {})
        self.assertEqual(bag[str(self.product.id)], 3)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), f"Updated {self.product.name} quantity to 3"
        )


class RemoveFromBagTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(name="Test Product", price=9.99)

    def test_can_remove_product_from_bag(self):
        self.client.post(
            f"/bag/add/{str(self.product.id)}/",
            {"quantity": 2, "redirect_url": "view_bag"},
        )
        self.client.get(reverse("view_bag"))

        response = self.client.post(f"/bag/remove/{str(self.product.id)}/")
        self.assertEqual(response.status_code, 200)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), f"Removed {self.product.name} from your bag")