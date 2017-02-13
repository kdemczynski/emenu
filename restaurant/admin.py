from django.contrib import admin# pragma: no cover
from .models import Card, CardItems, Dish, Categories# pragma: no cover


class CardItemsInline(admin.TabularInline):# pragma: no cover
    model         = CardItems
    raw_id_fields = ['card']


class CardAdmin(admin.ModelAdmin):# pragma: no cover
    list_display = ['name', 'created', 'updated']
    list_filter = ['name', 'created', 'updated']
    inlines = [CardItemsInline]


class DishAdmin(admin.ModelAdmin):# pragma: no cover
    list_display = ['name', 'price', 'prep_time', 'category', 'vege', 'created', 'updated']
    list_filter = ['category', 'vege', 'created', 'updated']
    list_editable = ('category', 'vege',)
    search_fields = ['name']


class CategoriesAdmin(admin.ModelAdmin):# pragma: no cover
    list_display = ['name', 'description', 'sort', 'created', 'updated']
    list_editable = ('sort',)


admin.site.register(Card, CardAdmin)# pragma: no cover
admin.site.register(Dish, DishAdmin)# pragma: no cover
admin.site.register(Categories, CategoriesAdmin)# pragma: no cover