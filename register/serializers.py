import random
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from .models import UserConfirmationCode


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField()

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise ValidationError("Пользователь с таким именем уже существует!")
        return username

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_active = False
        user.save()
        confirmation_code = str(random.randint(100000, 999999))
        UserConfirmationCode.objects.create(user=user, code=confirmation_code)
        return user


class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField()

    def validate(self, data):
        user = User.objects.filter(username=data['username']).first()
        if not user or not user.check_password(data['password']):
            raise ValidationError("Неверное имя пользователя или пароль.")

        if not user.is_active:
            raise ValidationError("Аккаунт не активирован. Пожалуйста, подтвердите свой email.")

        token, created = Token.objects.get_or_create(user=user)
        return {'token': token.key}


class UserConfirmSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        code = data.get("code")
        user = self.context.get("request").user
        try:
            confirmation_entry = UserConfirmationCode.objects.get(user=user, code=code)
        except UserConfirmationCode.DoesNotExist:
            raise ValidationError("Неверный код подтверждения.")
        user.is_active = True
        user.save()
        confirmation_entry.delete()
        return {"message": "Пользователь успешно подтверждён."}
