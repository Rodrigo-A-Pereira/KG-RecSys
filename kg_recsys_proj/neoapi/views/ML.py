from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from neoapi.serializer import CardSerializerNeo, PersonSerializerNeo
from neoapi.models import Card, Person
from django.http import Http404
import neomodel


class RecomendationList(APIView):
    def get(self, request, pid_slug, format=None):
        cards = Card.nodes.filter(name__icontains="dragon").all()
        card_serializer = CardSerializerNeo(cards, many=True)

        if request.query_params.get('max_len'):
            data_to_return = card_serializer.data[:int(request.query_params.get('max_len'))]
        else:
            data_to_return =  card_serializer.data
        return Response(data_to_return)