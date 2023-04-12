from django.db import models

# Create your models here.


class ShoppingCartVO(models.Model):
    import_href = models.CharField(max_length=200)
    name = models.CharField(max_length=200)


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
