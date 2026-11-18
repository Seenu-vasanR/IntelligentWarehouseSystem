
from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=150)
    product_code = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    minimum_stock = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

    @property
    def stock_status(self):
        if self.quantity == 0:
            return "Out of Stock"
        elif self.quantity <= self.minimum_stock:
            return "Low Stock"
        return "In Stock"


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    address = models.TextField()

    def __str__(self):
        return self.supplier_name


class StockMovement(models.Model):
    MOVEMENT_CHOICES = [
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    movement_type = models.CharField(
        max_length=3,
        choices=MOVEMENT_CHOICES
    )
    quantity = models.PositiveIntegerField()
    movement_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.product_name + " - " + self.movement_type
