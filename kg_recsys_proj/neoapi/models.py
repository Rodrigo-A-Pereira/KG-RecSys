from django.db import models
from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo,FloatProperty
# Create your models here.


class Card(StructuredNode):
    code = StringProperty(unique_index=True, required=True)
    name = StringProperty(index=True, required=True)
    r_set = StringProperty(required=True)
    image_url = StringProperty(default="https://static.wikia.nocookie.net/mtgsalvation_gamepedia/images/f/f8/Magic_card_back.jpg/revision/latest/scale-to-width-down/200?cb=20140813141013")

    '''
    @property
    def serializer(self):
        return {
            'code': self.code,
            'name': self.name,
            'r_set': self.r_set,
            'image_url': self.image_url
        }
    '''

class Person(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)

    #Relations
    card = RelationshipTo(Card, 'BOUGHT')


    '''
    @property
    def serializer(self):
        return {
            'code': uid,
            'name': self.name,
        }
    '''