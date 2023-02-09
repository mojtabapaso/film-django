from rest_framework import serializers


class UserProfileNameRetionalFields(serializers.RelatedField):
    def to_representation(self, value):
        for i in value.profile.all():
            self.name = i.name
            return f'{self.name}'
        return None
