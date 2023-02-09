from rest_framework import serializers
from .custom_relational_fields import UserProfileNameRetionalFields
from .models import Command


class CommandSerializers(serializers.ModelSerializer):
    user = UserProfileNameRetionalFields(read_only=True)

    class Meta:
        model = Command
        fields = '__all__'


class CreateCommandSerializers(serializers.Serializer):
    text = serializers.CharField()
    score = serializers.IntegerField()


class CreateAnswerCommandSerializers(serializers.Serializer):
    text = serializers.CharField()
