from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
from food_and_search.models import Product, Categorie


class ProductTestCase(TestCase):
    def setUp(self):
        self.fruit = Categorie.objects.create(name='fruit', id_category='fruit_id')
        self.pomme = Product.objects.create(name="pomme",
                                            description="une pomme",
                                            nutrition_grade='a',
                                            saturated_fat_100g='9.9',
                                            carbohydrates_100g='9.9',
                                            energy_100g='9.9',
                                            sugars_100g='9.9',
                                            sodium_100g='9.9')
        self.poire = Product.objects.create(name="poire",
                                            description="une poire",
                                            nutrition_grade='a',
                                            saturated_fat_100g='9.9',
                                            carbohydrates_100g='9.9',
                                            energy_100g='9.9',
                                            sugars_100g='9.9',
                                            sodium_100g='9.9')
        self.bananne = Product.objects.create(name="bananne",
                                              description="une bananne",
                                              nutrition_grade='a',
                                              saturated_fat_100g='9.9',
                                              carbohydrates_100g='9.9',
                                              energy_100g='9.9',
                                              sugars_100g='9.9',
                                              sodium_100g='9.9')
        self.cerise = Product.objects.create(name="cerise",
                                             description="une cerise",
                                             nutrition_grade='a',
                                             saturated_fat_100g='9.9',
                                             carbohydrates_100g='9.9',
                                             energy_100g='9.9',
                                             sugars_100g='9.9',
                                             sodium_100g='9.9')
        self.groseille = Product.objects.create(name="groseille",
                                                description="une groseille",
                                                nutrition_grade='a',
                                                saturated_fat_100g='9.9',
                                                carbohydrates_100g='9.9',
                                                energy_100g='9.9',
                                                sugars_100g='9.9',
                                                sodium_100g='9.9')
        self.mangue = Product.objects.create(name="mangue",
                                             description="une mangue",
                                             nutrition_grade='a',
                                             saturated_fat_100g='9.9',
                                             carbohydrates_100g='9.9',
                                             energy_100g='9.9',
                                             sugars_100g='9.9',
                                             sodium_100g='9.9')
        self.ananas = Product.objects.create(name="ananas",
                                             description="un ananas",
                                             nutrition_grade='a',
                                             saturated_fat_100g='9.9',
                                             carbohydrates_100g='9.9',
                                             energy_100g='9.9',
                                             sugars_100g='9.9',
                                             sodium_100g='9.9')
        self.pomme.categorie.add(self.fruit)
        self.ananas.categorie.add(self.fruit)
        self.bananne.categorie.add(self.fruit)
        self.cerise.categorie.add(self.fruit)
        self.groseille.categorie.add(self.fruit)
        self.mangue.categorie.add(self.fruit)
        self.poire.categorie.add(self.fruit)
        self.client = Client()
        self.user = User.objects.create_user('foo', 'foo@bar.com', 'foo#')
        self.client.login(username='foo', password='foo#')

    def test_categorie(self):
        categorie = Categorie.objects.get(id_category='fruit_id')
        self.assertEqual(categorie.id_category, 'fruit_id')
        self.assertEqual(categorie.id, 1)
        self.assertEqual(str(categorie), 'fruit')

    def test_product(self):
        product = Product.objects.get(name="pomme")
        self.assertEqual(product.description, 'une pomme')
        self.assertEqual(product.nutrition_grade, 'a')
        self.assertEqual(product.saturated_fat_100g, 9.9)
        self.assertEqual(product.carbohydrates_100g, 9.9)
        self.assertEqual(product.energy_100g, 9.9)
        self.assertEqual(product.sugars_100g, 9.9)
        self.assertEqual(product.sodium_100g, 9.9)
        self.assertEqual(str(product), 'pomme')

    def test_index(self):
        response = self.client.get(reverse('food_and_search:index'))
        self.assertEqual(response.status_code, 200)

    def test_result(self):
        response = self.client.get('/result/', data={'product': 'pomme'})
        self.assertEqual(response.status_code, 200)

    def test_result_raise_error(self):
        response = self.client.get('/result/', data={'product': 'pommier'})
        self.assertEqual(response.status_code, 404)

    def test_save_result_product(self):
        response = self.client.post("/result/",{'product_form': '1'},
                                    content_type="application/x-www-form-urlencoded", follow=True)

    def test_saveproduct(self):
        response = self.client.get(reverse('food_and_search:save_product'))
        self.assertEqual(response.status_code, 200)
