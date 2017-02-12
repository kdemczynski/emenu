from django.test import TestCase
from .models import CardItems, Card, Dish, Categories
from django.utils import timezone


class CardTestCase(TestCase):
    def setUp(self):
        Card.objects.create(name="Test", description="Karta utworzona na potrzeby testow")

    def test_card_query(self):
        card = Card.objects.get(name="Test")
        self.assertEqual(card.description, 'Karta utworzona na potrzeby testow')

    def test_card_timezone(self):
        card = Card.objects.get(name="Test")
        self.assertEqual(card.created, timezone.now())