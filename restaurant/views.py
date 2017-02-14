from restaurant.models import Card
from restaurant.models import CardItems, Categories
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class CardList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'restaurant/cards.html'

    def get(self, request):
        queryset = Card.objects.all().order_by('id')
        return Response({'cards': queryset})


class DishList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'restaurant/dish_detail.html'

    def get(self, request, pk):
        card_items = CardItems.objects.select_related('dish', 'card').filter(card = pk).order_by('dish__price', 'dish__name')
        cat = Categories.objects.select_related().all().order_by('sort')

        return Response({'dishes': card_items,
                         'categories': cat})