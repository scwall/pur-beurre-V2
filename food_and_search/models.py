from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150)
    id_category = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Products(models.Model):
    categories = models.ManyToManyField(Categories)
    name = models.CharField(max_length=150)
    link_http = models.CharField(max_length=45)
    description = models.TextField()
    nutrition_grade = models.CharField(max_length=1)
    saturated_fat_100g = models.FloatField()
    carbohydrates_100g = models.FloatField()
    energy_100g = models.FloatField()
    sugars_100g = models.FloatField()
    sodium_100g = models.FloatField()
    def __str__(self):
        return self.name