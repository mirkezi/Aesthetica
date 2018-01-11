from rest_framework import serializers
from inventario.models import Articolo

class ArticoloSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ean = serializers.IntegerField(default=0)
    nome = serializers.CharField(max_length=64)
    descrizione = serializers.CharField(max_length=512, blank=True, null=True)
    prezzo = serializers.FloatField(default=0)


    def create(self, validated_data):

        return Articolo.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.ean = validated_data.get('ean', instance.ean)
        instance.nome = validated_data.get('nome', instance.nome)
        instance.descrizione = validated_data.get('descrizione', instance.descrizione)
        instance.prezzo = validated_data.get('prezzo', instance.prezzo)
        instance.save()
        return instance
