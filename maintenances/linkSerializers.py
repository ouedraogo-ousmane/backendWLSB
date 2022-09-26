from nbformat import read
from rest_framework import serializers

class RelatedPiecesEchangeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(read_only=True)
