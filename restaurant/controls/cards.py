# -*- coding: utf-8 -*-
from restaurant.views import BasicView
from django.shortcuts import render
from django.db import connection
from restaurant.models import Card

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class CardList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'restaurant/cards.html'

    def get(self, request):
        queryset = Card.objects.all()
        return Response({'cards': queryset})




class CardView(BasicView):

    def get_context_data(self, **kwargs):
        self.context = super(CardView, self).get_context_data(**kwargs)
        self.template_name = "restaurant/cards.html"

        self.context['cards'] = Card.objects.select_related().all().order_by('id')


        # wylacznie do wyswietlanie ilosci zapytan i czasu ladowania strony
        self.context['admin_queries'] = connection.queries
        time = 0
        for t in self.context['admin_queries']:
            time += float(t['time'])
        self.context['queries_time'] = time
        self.context['queries_size'] = len(connection.queries)
        print('ilosc zapytan:', len(connection.queries))

        return self.context


    def post(self, request, *args, **_kwargs):
        super(CardView, self).post(request, *args, **_kwargs)


        return render(request, 'base.html', self.context)

