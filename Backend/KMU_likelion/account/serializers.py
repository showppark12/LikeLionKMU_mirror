from rest_framework import serializers
from .models import Profile
from django.contrib.auth import authenticate


#회원가입
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = Profile.objects.create_user(
            validated_data["username"], None, validated_data["password"]
        )
        return user

# 접속 유지중인지 확인
class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = Profile
         fields = '__all__'

#로그인
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")