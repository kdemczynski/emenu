from rest_framework import serializers
from restaurant.models import Card


class CardSerializer(serializers.Serializer):
    class Meta:
        model = Card
        fields = ('id', 'name', 'description', 'created', 'updated', 'style')
