from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from food_and_search.models import Product, Categorie


class ProductTestCase(TestCase):
    def setUp(self):
        Categorie.objects.create(name='fruit',id_category='fruit_id')
        Product.objects.create(name="pomme",
                               description="une pomme",
                               nutrition_grade='a',
                               saturated_fat_100g='9.9',
                               carbohydrates_100g='9.9',
                               energy_100g='9.9',
                               sugars_100g='9.9',
                               sodium_100g='9.9')
    def test_categorie(self):
        categorie = Categorie.objects.get(id_category='fruit_id')
        self.assertEqual(categorie.id_category, 'fruit_id')
        self.assertEqual(categorie.id, 1)
    def test_product(self):
        product = Product.objects.get(name="pomme")
        self.assertEqual(product.description , 'une pomme')
        self.assertEqual(product.nutrition_grade , 'a')
        self.assertEqual(product.saturated_fat_100g, 9.9)
        self.assertEqual(product.carbohydrates_100g, 9.9)
        self.assertEqual(product.energy_100g, 9.9)
        self.assertEqual(product.sugars_100g,9.9)
        self.assertEqual(product.sodium_100g,9.9)


    def test_index(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('food_and_search:index'))
        self.assertEqual(response.status_code, 200)
