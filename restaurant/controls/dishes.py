# -*- coding: utf-8 -*-
from restaurant.views import BasicView
from django.shortcuts import render
from django.db import connection
from restaurant.models import CardItems, Categories

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class DishList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'restaurant/dish_detail.html'

    def get(self, request, pk):
        card_items = CardItems.objects.select_related().filter(card = pk).order_by('dish__price', 'dish__name')
        cat = Categories.objects.select_related().all().order_by('sort')

        return Response({'dishes': card_items,
                         'categories': cat})


class DishView(BasicView):

    def get_context_data(self, **kwargs):
        self.context = super(DishView, self).get_context_data(**kwargs)
        self.template_name = "restaurant/dish_detail.html"

        card_id = self.context.get('pk')
        dishes = self.context['dishes'] = CardItems.objects.select_related().filter(card = card_id).order_by('dish__price', 'dish__name')
        categories = self.context['categories'] = Categories.objects.select_related().all().order_by('sort')

        # wylacznie do wyswietlanie ilosci zapytan i czasu ladowania strony
        # self.context['admin_queries'] = connection.queries
        # time = 0
        # for t in self.context['admin_queries']:
        #     time += float(t['time'])
        # self.context['queries_time'] = time
        # self.context['queries_size'] = len(connection.queries)
        # print('ilosc zapytan:', len(connection.queries))

        return self.context


    def post(self, request, *args, **_kwargs):
        super(DishView, self).post(request, *args, **_kwargs)


        return render(request, 'restaurant/dish_detail.html', self.context)

