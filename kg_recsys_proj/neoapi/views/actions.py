from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from neoapi.serializer import CardSerializerNeo, PersonSerializerNeo
from neoapi.models import Card, Person
from django.http import Http404
import neomodel
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def buy_card(request):
    try:
        person = Person.nodes.get(uid=request.data["uid"])
        card = Card.nodes.get(code=request.data["card_code"])
        res = person.card.connect(card)
        response = {"result": res}
        return Response(response, status=status.HTTP_201_CREATED)
    except:
        return Response({"error": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)