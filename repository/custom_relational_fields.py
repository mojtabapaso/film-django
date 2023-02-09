from rest_framework import serializers


class GenreShowRelational(serializers.RelatedField):
    def to_representation(self, value):
        print(value)
        var = []
        for i in value.all():
            var.append(i.name)
        return var



