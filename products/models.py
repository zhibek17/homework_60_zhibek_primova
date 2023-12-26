from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    description = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    added_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
    image = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name
