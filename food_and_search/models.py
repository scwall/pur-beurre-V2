from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class Products(models.Model):
    categories = models.ManyToManyField(Categories)
    name = models.CharField(max_length=150)
    link_http = models.CharField(max_length=45)
    description = models.TextField()
    nutrition_grade = models.CharField(max_length=1)
    saturated_fat_100g = models.SmallIntegerField()
    carbohydrates_100g = models.SmallIntegerField()
    energy_100g = models.SmallIntegerField()
    sugars_100g = models.SmallIntegerField()
    sodium_100g = models.SmallIntegerField()
    def __str__(self):
        return self.name