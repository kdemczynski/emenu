from django.conf.urls import url
from restaurant.controls.dishes import DishView
from restaurant.controls.cards import CardView
from restaurant.controls.cards import CardList
from restaurant.controls.dishes import DishList


urlpatterns = [
    url(r'^$', CardList.as_view(), name='card'),
    url(r'^card/(?P<pk>[0-9]+)/$', DishList.as_view(), name='card_detail'),
]

# urlpatterns = [
#     url(r'^$', CardView.as_view(), name='card'),
#     url(r'^card/(?P<pk>[0-9]+)/$', DishView.as_view(), name='card_detail'),
# ]