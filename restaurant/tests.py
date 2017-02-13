from django.test import TestCase
from .models import CardItems, Card, Dish, Categories
from .views import CardList, DishList
from django.db import models
from django.test import RequestFactory
from restaurant import admin
from django.db.models import ImageField

# models.py
class CardModelTestCase(TestCase):
    def setUp(self):
        Card.objects.create(name="Test", description="Karta utworzona na potrzeby testow")
        Dish.objects.create(name="Danie1", price='1', prep_time='1')
        card = Card.objects.get(name="Test")
        dish = Dish.objects.get(name="Danie1")
        CardItems.objects.create(card_id = card.id, dish_id = dish.id)
        print('tsetsd')

    def test_card_query(self):
        card = Card.objects.get(name="Test")
        self.assertEqual(card.description, 'Karta utworzona na potrzeby testow')

    # def test_card_timezone(self):
    #     card = Card.objects.get(name="Test")
    #     self.assertEqual(card.created, timezone.now())

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


# class TestY(TestCase):
#
#     def test_model_relation(self):
#         x = Dish.objects.create(name="test1")
#         y = Y(event=X.objects.create(name="test2"))
#         y.full_clean()  # `event` correctly set. This should pass
#         y.save()
#         self.assertEqual(Y.objects.filter(event__name="test2").count(), 1)
#
#     def test_model_relation__event_missing(self):
#         x = X.objects.create(name="test1")
#         y = Y()  # Y without `event` set
#         with self.assertRaises(ValidationError):
#             y.full_clean()
#             y.save()
#         self.assertEqual(Y.objects.filter(event__name="test2").count(), 0)


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


# admin.py
# class TestAdminConfig(TestCase):
#
#     def test_admin_fieldname_lists(self):
#         model_classnames = ['CardAdmin']
#         admin_fieldname_lists = ['list_display']
#
#         for model_classname in model_classnames:
#             model_class = locate("restaurant.models.%s" % model_classname)
#             admin_class = locate("restaurant.admin.%s" % model_classname)
#             # #print("classes: %s, %s" % (model_class.__name__, admin_class.__name__))
#             for list_name in admin_fieldname_lists:
#                 #print("    list: %s" % list_name)
#                 for fieldname in getattr(admin_class, list_name):
#                     fieldname = fieldname.replace("^", "")
#                     #print("       field: %s" % fieldname)
#                     if fieldname in dir(model_class): continue
#                     if fieldname in dir(admin_class): continue
#                     model_class.objects.filter(**{fieldname:None})