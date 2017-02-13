from django.test import TestCase
from .models import CardItems, Card, Dish, Categories
from .views import CardList, DishList
from django.db import models
from django.test import RequestFactory
from django.db.models import ImageField


# models.py
class CardModelTestCase(TestCase):
    def setUp(self):
        Card.objects.create(name="Test", description="Karta utworzona na potrzeby testow")
        Dish.objects.create(name="Danie1", price='1', prep_time='1')
        card = Card.objects.get(name="Test")
        dish = Dish.objects.get(name="Danie1")
        CardItems.objects.create(card_id = card.id, dish_id = dish.id)

    def test_card_query(self):
        card = Card.objects.get(name="Test")
        self.assertEqual(card.description, 'Karta utworzona na potrzeby testow')

    def test_get_dishes_func(self):
        card = CardItems.objects.get(card_id = 1, dish_id=1)
        test = card.card.get_dishes_card()
        self.assertEqual(type(test), models.query.QuerySet)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Card._meta.verbose_name_plural), "karty menu")

    def test_string_representation(self):
        entry1 = Card(name="Tested")
        self.assertEqual(str(entry1), entry1.name)


class DishModelTestCase(TestCase):

    def test_string_representation(self):
        entry1 = Dish(name="Tested")
        field = Dish._meta.get_field('image')
        self.assertEqual(str(entry1), entry1.name)
        self.assertTrue(isinstance(field, ImageField))

    def test_verbose_name_plural(self):
        self.assertEqual(str(Dish._meta.verbose_name_plural), "dania")

    def test_verbose_name(self):
        self.assertEqual(str(Dish._meta.verbose_name), "danie")


class CategoriesModelTestCase(TestCase):

    def test_string_representation(self):
        entry1 = Categories(name="Tested")
        self.assertEqual(str(entry1), entry1.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Categories._meta.verbose_name_plural), "kategorie")


# views.py
class CardListTestCase(TestCase):
    def test_get(self):
        request = RequestFactory().get('/')
        view = CardList.as_view(template_name='restaurant/cards.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)


class DishListTestCase(TestCase):
    def test_get(self):
        request = RequestFactory().get('/card/1')
        view = DishList.as_view(template_name='restaurant/dish_detail.html')
        response = view(request, 1)
        self.assertEqual(response.status_code, 200)
