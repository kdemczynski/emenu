from django.db import models


class Card(models.Model):
    name                = models.CharField(max_length=200, unique=True, db_index=True, verbose_name='Nazwa')
    description         = models.TextField(blank=True, verbose_name='Opis')
    created             = models.DateTimeField(auto_now_add=True, verbose_name='Utworzono')
    updated             = models.DateTimeField(auto_now=True, verbose_name='Zaktualizowano')

    class Meta:
        ordering = ('name', )
        verbose_name = 'karta menu'
        verbose_name_plural = 'karty menu'

    def get_dishes_card(self):
        dishes = CardItems.objects.select_related().filter(card = self.id)
        return dishes

    def __str__(self):
        return self.name


class Dish(models.Model):# pragma: no cover
    name                = models.CharField(max_length=200, verbose_name='Nazwa')
    description         = models.TextField(blank=True, verbose_name='Opis')
    category            = models.ForeignKey('Categories', default=1, verbose_name='Kategoria')
    image               = models.ImageField(upload_to='static/images/dishes', blank=True, verbose_name='Zdjęcie')
    price               = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Cena')
    prep_time           = models.IntegerField(verbose_name='Czas przygotowania [min.]')
    vege                = models.BooleanField(default=True, verbose_name='Wegetariańskie')
    created             = models.DateTimeField(auto_now_add=True, verbose_name='Utworzono')
    updated             = models.DateTimeField(auto_now=True, verbose_name='Zaktualizowano')

    class Meta:
        ordering = ('name', )
        verbose_name = 'danie'
        verbose_name_plural = 'dania'

    def __str__(self):
        return self.name


class CardItems(models.Model):# pragma: no cover
    card                = models.ForeignKey('Card', related_name='card')
    dish                = models.ForeignKey('Dish', related_name='dish')


class Categories(models.Model):# pragma: no cover
    name                = models.CharField(max_length=200, verbose_name='Nazwa')
    description         = models.CharField(max_length=200, blank=True, verbose_name='Opis')
    sort                = models.IntegerField(blank=True, default=1, verbose_name='Kolejność sortowania')
    created             = models.DateTimeField(auto_now_add=True, verbose_name='Utworzono')
    updated             = models.DateTimeField(auto_now=True, verbose_name='Zaktualizowano')

    class Meta:
        ordering = ('name', )
        verbose_name = 'kategoria'
        verbose_name_plural = 'kategorie'

    def __str__(self):
        return self.name