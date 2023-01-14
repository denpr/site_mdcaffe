from rest_framework import serializers
from .models import IncomingMessage


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomingMessage
        fields = '__all__'
