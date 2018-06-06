from django.conf import settings
from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150)
    id_category = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Products(models.Model):
    product_favourite = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='product_favourite')
    categories = models.ManyToManyField(Categories)
    name = models.CharField(max_length=150)
    link_http = models.CharField(max_length=150)
    description = models.TextField()
    nutrition_grade = models.CharField(max_length=1)
    saturated_fat_100g = models.FloatField()
    carbohydrates_100g = models.FloatField()
    energy_100g = models.FloatField()
    sugars_100g = models.FloatField()
    sodium_100g = models.FloatField()
    def __str__(self):
        return self.name

