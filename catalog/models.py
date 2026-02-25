from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:product_list") + f"?category={self.slug}"

class Product(models.Model):
    CURRENCY_CHOICES = [
        ("RON", "RON"),
        ("EUR", "EUR"),
    ]

    name = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="RON")
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="products/%Y/%m/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["is_active", "created_at"]),
            models.Index(fields=["slug"]),
        ]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:product_detail", args=[self.slug])

    @property
    def is_in_stock(self) -> bool:
        return self.stock > 0 and self.is_active
