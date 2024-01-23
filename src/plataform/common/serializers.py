from django.db.models import fields
from rest_framework import serializers
from .models import Log, AuthorizedNumber, Item


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'


class AuthorizedNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorizedNumber
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
