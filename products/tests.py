from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from products.models import Product, Category, Brand, Reviews
from products.views import (
    all_products,
    product_detail,
    add_product,
    edit_product,
    delete_product,
    add_review,
)

from django.shortcuts import get_object_or_404
from django.contrib.messages import get_messages
from urllib.parse import urlencode
from django.core.files.uploadedfile import SimpleUploadedFile


class AllProductsViewTest(TestCase):

    def setUp(self):
        testsuperuser = User.objects.create_superuser(
            username="superuser", password="testpw", email="superuser@example.com"
        )
        testsuperuser.save()


        self.category = Category.objects.create(name="Gaming")
        self.brand = Brand.objects.create(name="Sideshow")
        image_file = SimpleUploadedFile(
            name="box.webp",
            content=open("media/box.webp", "rb").read(),
            content_type="image/png",
        )

        self.product = Product.objects.create(
            name="Test Product",
            sku="123456",
            description="Test description",
            price="9.99",
            image=image_file,
        )

    def test_can_get_products_page(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_all_products_with_search_query(self):
        response = self.client.get("/products/", {"q": ""})
        self.assertRedirects(response, "/products/")
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "You didn't enter any search criteria!")

    def test_can_get_all_products_from_search(self):
        response = self.client.get(
            "/products/",
            {
                "search_term": "anime",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_sort(self):
        response = self.client.get("/products/", {"sort": "name", "direction": "desc"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")


class AddProductTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="superuser",
            password="testpw",
        )
        self.client.login(username="superuser", password="testpw")

        self.category = Category.objects.create(name="Gaming")
        self.brand = Brand.objects.create(name="Sideshow")

    def test_add_product_view_not_superuser(self):
        url = reverse("add_product")
        user = User.objects.create_user(username="regularuser", password="testpw")
        self.client.login(username="regularuser", password="testpw")

        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)

        self.assertFalse(Product.objects.exists())

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Sorry, only store owners can do that.")
        self.assertRedirects(response, reverse("home"))


class ProductDetailTest(TestCase):

    def setUp(self):
        testsuperuser = User.objects.create_superuser(
            username="superuser",
            password="testpw",
        )
        testsuperuser.save()

        self.category = Category.objects.create(name="Gaming")
        self.brand = Brand.objects.create(name="Sideshow")

        image_file = SimpleUploadedFile(
            name="box.webp",
            content=open("media/box.webp", "rb").read(),
            content_type="image/png",
        )

        self.product = Product.objects.create(
            name="Test Product",
            sku="123456",
            description="Test description",
            price="9.99",
            image=image_file,
        )

    def test_product_detail_view(self):
        client = Client()
        url = reverse("product_detail", args=[self.product.id])
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")

        self.assertContains(response, self.product.name)
        self.assertContains(response, self.product.description)

        self.assertIn("related_products", response.context)

        wishlist = response.context.get("wishlist")
        if client.session.get("wishlist"):
            self.assertIsNotNone(wishlist)
        else:
            self.assertIsNone(wishlist)


class EditProductViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="superuser",
            password="testpw",
        )
        self.client.login(username="superuser", password="testpw")

        self.product = Product.objects.create(
            name="Test Product",
            sku="123456",
            description="Test description",
            price="9.99",
        )

    def test_edit_product_view_as_superuser(self):

        url = reverse("edit_product", args=[self.product.id])
        self.client.login(username="superuser", password="testpw")

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "products/edit_product.html")

    def test_edit_product_view_as_non_superuser(self):

        self.user = User.objects.create_user(
            username="regularuser",
            password="testpw",
        )
        self.client.force_login(self.user)

        url = reverse("edit_product", args=[self.product.id])
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))


        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Sorry, only store owners can do that.")


class DeleteProductViewTest(TestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username="superuser",
            password="testpw",
        )
        self.client = Client()

        self.product = Product.objects.create(
            name="Test Product",
            sku="123456",
            description="Test description",
            price="9.99",
        )

    def test_delete_product_view_as_superuser(self):

        url = reverse("delete_product", args=[self.product.id])
        self.client.force_login(self.superuser)

        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("products"))

        self.assertFalse(Product.objects.filter(id=self.product.id).exists())

    def test_delete_product_not_superuser(self):

        self.user = User.objects.create_user(
            username="regularuser",
            password="testpw",
        )
        self.client.force_login(self.user)

        url = reverse("delete_product", args=[self.product.id])
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Sorry, only store owners can do that.")


class AddReviewViewTest(TestCase):


    def setUp(self):
        self.user = User.objects.create_user(
            username="regularuser",
            password="testpw",
        )
        self.client = Client()

        self.product = Product.objects.create(
            name="Test Product",
            sku="123456",
            description="Test description",
            price="9.99",
        )

    def test_add_review_view_user(self):

        url = reverse("add_review", args=[self.product.id])
        self.client.login(username="regularuser", password="testpw")

        form_data = {
            "title": "Test Review",
            "review": "This is a test review.",
        }

        response = self.client.post(url, form_data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("product_detail", args=[self.product.id])
        )

    
        self.assertTrue(
            Reviews.objects.filter(product=self.product, user=self.user).exists()
        )

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Your review has been successfully added!")

    def test_add_review_view_invalid_form(self):

        url = reverse("add_review", args=[self.product.id])
        self.client.login(username="regularuser", password="testpw")

        form_data = {
            "title": "",
            "review": "This is a test review.",
        }

        response = self.client.post(url, form_data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("product_detail", args=[self.product.id])
        )

        self.assertFalse(
            Reviews.objects.filter(product=self.product, user=self.user).exists()
        )

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Your review has not been submitted.")


class UpdateReviewViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="regularuser",
            password="testpw",
        )
        self.client = Client()

        self.product = Product.objects.create(
            name="Test Product",
            sku="123456",
            description="Test description",
            price="9.99",
        )

        self.review = Reviews.objects.create(
            product=self.product,
            user=self.user,
            title="Initial Title",
            review="Initial Review",
        )

    def test_update_review_view(self):

        url = reverse("update_review", kwargs={"pk": self.review.pk})
        self.client.login(username="regularuser", password="testpw")

        form_data = {
            "title": "Updated Title",
            "review": "Updated Review",
        }

        response = self.client.post(url, form_data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("product_detail", kwargs={"product_id": self.product.id})
        )

        self.review.refresh_from_db()

        self.assertEqual(self.review.title, "Updated Title")
        self.assertEqual(self.review.review, "Updated Review")

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Your review was updated!")

    def test_update_review_view_invalid_form(self):

        url = reverse("update_review", kwargs={"pk": self.review.pk})
        self.client.login(username="regularuser", password="testpw")

        form_data = {
            "title": "",
            "review": "Updated Review",
        }

        response = self.client.post(url, form_data)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "products/edit_review.html")

        self.review.refresh_from_db()

        self.assertEqual(self.review.title, "Initial Title")
        self.assertEqual(self.review.review, "Initial Review")


class DeleteReviewViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="regularuser",
            password="testpw",
        )
        self.client = Client()

        self.product = Product.objects.create(
            name="Test Product",
            sku="123456",
            description="Test description",
            price="9.99",
        )

        self.review = Reviews.objects.create(
            product=self.product,
            user=self.user,
            title="Initial Title",
            review="Initial Review",
        )

        def test_delete_review_view(self):

            url = reverse("delete_review", kwargs={"pk": review.pk})
            response = self.client.post(url)

            self.assertEqual(response.status_code, 302)

            self.assertFalse(Reviews.objects.filter(pk=self.review.pk).exists())


            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(str(messages[0]), "Review deleted successfully.")

def tearDown(self):

    User.objects.filter(username="superuser").delete()
    User.objects.filter(username="regularuser").delete()
    Category.objects.filter(name="Gaming").delete()
    Brand.objects.filter(name="Sideshow").delete()
    Product.objects.filter(name="Test Product").delete()



