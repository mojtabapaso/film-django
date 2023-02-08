from rest_framework import serializers
from .models import Command


class CommandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = '__all__'
