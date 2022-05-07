from rest_framework import serializers

class CardSerializerNeo(serializers.Serializer):
    name = serializers.CharField()
    code = serializers.CharField()
    r_set = serializers.CharField()
    image_url = serializers.CharField()


class PersonSerializerNeo(serializers.Serializer):
    uid = serializers.CharField()
    name = serializers.CharField()