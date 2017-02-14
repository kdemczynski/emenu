from django.test import TestCase
from .models import CardItems, Card, Dish, Categories
from .views import CardList, DishList
from django.db import models, IntegrityError
from django.test import RequestFactory
from django.db.models import ImageField
from django.core.urlresolvers import reverse


# models.py
class CardModelTestCase(TestCase):
    fixtures = ['fix.json']

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
        self.assertEqual(test[0].card.id, 1)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Card._meta.verbose_name_plural), "karty menu")

    def test_string_representation(self):
        entry1 = Card(name="Tested")
        self.assertEqual(str(entry1), entry1.name)

    def test_unique_card_name(self):
        with self.assertRaises(IntegrityError):
            Card.objects.create(name="Test")


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
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_bad_link(self):
        resp = self.client.get('/card/1/blahblah')
        self.assertEqual(resp.status_code, 404)

    def test_bad_pk(self):
        resp = self.client.get('/card/123456/')
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get('/card/abcde/')
        self.assertEqual(resp.status_code, 404)


class DishListTestCase(TestCase):
    fixtures = ['fix.json']

    def test_get(self):
        request = RequestFactory().get('/card/1')
        view = DishList.as_view(template_name='restaurant/dish_detail.html')
        response = view(request, 1)
        get = self.client.get(reverse('restaurant:card_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(get.context['dishes']), 18)


# urls.py
class UrlsNamedLinksTestCase(TestCase):
    fixtures = ['fix.json']

    def test_index(self):
        resp = self.client.get(reverse('restaurant:card'))
        self.assertEqual(resp.status_code, 200)

    def test_detail(self):
        resp = self.client.get(reverse('restaurant:card_detail', kwargs={'pk': 1}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['dishes'][0].card.id, 1)
