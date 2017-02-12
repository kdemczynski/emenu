from django.conf.urls import url
from .views import CardList, DishList


urlpatterns = [
    url(r'^$', CardList.as_view(), name='card'),
    url(r'^card/(?P<pk>[0-9]+)/$', DishList.as_view(), name='card_detail'),
]
