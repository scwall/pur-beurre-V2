from django.test import TestCase

# Create your tests here.
from food_and_search.models import Product, Categorie


class AnimalTestCase(TestCase):
    def setUp(self):
        Categorie.objects.create(name='fruit')
        Product.objects.create(name="pomme", description="une pomme")


    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        product = Product.objects.get(name="pomme")
        self.assertEqual(product.description , 'une pomme')
