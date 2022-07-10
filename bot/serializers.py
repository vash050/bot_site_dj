from rest_framework import serializers

from bot.models import ObjectPart, Block


class ObjectPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectPart
        fields = ['name', 'height', 'width', 'owner', 'order_number', 'data', 'type']


class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['name',]