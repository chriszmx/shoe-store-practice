from django.db import models
# from django.contrib.auth.models import User


# Create your models here.
class ShoeInventory(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    size = models.DecimalField(max_digits=3, decimal_places=1)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField(blank=True)
    sku = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ShoppingCart(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart #{self.pk}"

    def get_extra_data(self, o):
        return {}


class CartItem(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart,
                                      on_delete=models.CASCADE,
                                      related_name='items')
    shoe_inventory = models.ForeignKey(ShoeInventory,
                                       on_delete=models.CASCADE,
                                       related_name='cart_items')
    size = models.DecimalField(max_digits=3, decimal_places=1)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.shoe_inventory.name} ({self.size}) x {self.quantity}"
