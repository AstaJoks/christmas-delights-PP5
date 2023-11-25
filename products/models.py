from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=4, decimal_places=2)
    discount = models.IntegerField(
        default=10,
        help_text="Discount in Percentage",
        verbose_name="Discount If Product On Sale",
    )
    discounted_price = models.IntegerField(null=True)

    @property
    def discounted_price(self):
        return ((self.price) * (self.discount)) / 100

    @property
    def sale_price(self):
        return (self.price) - (self.discounted_price)

    def __str__(self):
        return self.title
