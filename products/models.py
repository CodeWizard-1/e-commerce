from django.db import models

from django.utils import timezone
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User
from profiles.models import UserProfile


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    GENDER_CHOICES = [
        ('men', 'men'),
        ('women', 'women'),
        ('kids', 'kids'),
    ]
    FIT_CHOICES = [
        ('Regular (Classic)', 'Regular (Classic)'),
        ('Slim', 'Slim'),
        ('Loose', 'Loose'),
        ('Athletic', 'Athletic'),
        ('Relaxed', 'Relaxed'),
        ('Skinny', 'Skinny'),
    ]
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2,
                                     null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    brand = models.ForeignKey("Brand", null=True, blank=True,
                              on_delete=models.SET_NULL)
    on_sale = models.BooleanField(default=False)
    discount = models.IntegerField(
        default=10,
        help_text="Discount in Percentage",
        verbose_name="Discount If Product On Sale",
    )
    discounted_price = models.IntegerField(null=True)
    created_on = models.DateField(default=timezone.now)
    average_rating = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,
                              null=True, blank=True)
    is_featured = models.BooleanField(
        default=False, verbose_name="Feature on Home Page"
    )
    fit = models.CharField(max_length=60, choices=FIT_CHOICES,
                              null=True, blank=True)
    materials = models.TextField(null=True, blank=True)

    def clean(self):
        if self.price < 0:
            raise ValidationError("Price cannot be negative.")

    @property
    def discounted_price(self):
        return ((self.price) * (self.discount)) / 100

    @property
    def sale_price(self):
        return (self.price) - (self.discounted_price)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    CLOTHING_SIZE_CHOICES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
        ('3XL', 'Triple Extra Large'),
    ]
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    clothing_size = models.CharField(max_length=10,
                                     choices=CLOTHING_SIZE_CHOICES,
                                     null=True, blank=True)
    men_shoe_size = models.CharField(max_length=10, null=True, blank=True)
    women_shoe_size = models.CharField(max_length=10, null=True, blank=True)
    child_shoe_size = models.CharField(max_length=10, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    stock_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.product.name} - Clothing Size: {self.clothing_size}, \
            Men Shoe Size: {self.men_shoe_size}, Women Shoe Size: \
                {self.women_shoe_size}, \
                    Child Shoe Size: {self.child_shoe_size}, \
                        Color: {self.color}'


class Brand(models.Model):
    class Meta:
        verbose_name_plural = "Brands"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Reviews(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=1500, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "product"],
                                    name="reviews_per_user")
        ]
        verbose_name_plural = "Reviews"

    def __str__(self):
        return self.title
