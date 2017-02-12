from django.db import models


class Card(models.Model):
    name                = models.CharField(max_length=200, unique=True, db_index=True)
    description         = models.TextField(blank=True)
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'karta menu'
        verbose_name_plural = 'karty menu'

    def get_dishes_card(self):
        dishes = CardItems.objects.select_related().filter(card = self.id)
        return dishes

    def __str__(self):
        return self.name


class Dish(models.Model):
    name                = models.CharField(max_length=200)
    description         = models.TextField(blank=True)
    category            = models.ForeignKey('Categories', default=1)
    image               = models.ImageField(upload_to='static/images/dishes', blank=True)
    price               = models.DecimalField(max_digits=10, decimal_places=2)
    prep_time           = models.IntegerField()
    vege                = models.BooleanField(default=True)
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'danie'
        verbose_name_plural = 'dania'

    def __str__(self):
        return self.name


class CardItems(models.Model):
    card                = models.ForeignKey('Card', related_name='card')
    dish                = models.ForeignKey('Dish', related_name='dish')


class Categories(models.Model):
    name                = models.CharField(max_length=200)
    description         = models.CharField(max_length=200, blank=True)
    sort                = models.IntegerField(blank=True, default=1)
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'kategoria'
        verbose_name_plural = 'kategorie'

    def __str__(self):
        return self.name