from django.contrib.auth import authenticate, get_user_model, password_validation
from rest_framework import serializers
from .models import Profile

User = get_user_model()


def clean_email(value):
    if User.objects.filter(email=value):
        raise serializers.ValidationError("این ایمیل قبلا ثبت شده است")
    return value


class RegisterSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}, 'email': {'validators': (clean_email,)}}

    def validate_password(self, data):
        password_validation.validate_password(password=data, user=User)
        return data

    def create(self, validated_data):
        del validated_data['password2']
        return User.objects.create_user(**validated_data)


class LoginSerializers(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
        if not user:
            raise serializers.ValidationError("کاربری با این اطلاعات پیدا نشد ")
        data['user'] = user
        return data


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


