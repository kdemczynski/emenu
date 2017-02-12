from django.contrib import admin
from .models import Card, CardItems, Dish, Categories


class CardItemsInline(admin.TabularInline):
    model         = CardItems
    raw_id_fields = ['card']


class CardAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated']
    list_filter = ['name', 'created', 'updated']
    inlines = [CardItemsInline]


class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'prep_time', 'category', 'vege', 'created', 'updated']
    list_filter = ['category', 'vege', 'created', 'updated']
    list_editable = ('category', 'vege',)


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'sort', 'created', 'updated']
    list_editable = ('sort',)


admin.site.register(Card, CardAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(Categories, CategoriesAdmin)