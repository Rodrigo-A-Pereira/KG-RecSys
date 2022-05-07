from rest_framework import viewsets
from neoapi.serializer import CardSerializerNeo, PersonSerializerNeo
from neoapi.models import Card, Person

class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializerNeo
    lookup_field = "code"
    #queryset = Card.nodes.all()

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name is not None:
            return Card.nodes.filter(name__icontains=name).all()
        else:
            return Card.nodes.all()

    def get_object(self):
        return Card.nodes.get(code=self.kwargs[self.lookup_field])

class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializerNeo
    lookup_field = "uid"
    queryset = Person.nodes.all()

    def get_object(self):
        return Person.nodes.get(uid=self.kwargs[self.lookup_field])