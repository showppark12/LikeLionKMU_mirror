from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate


#회원가입
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"], None, validated_data["password"]
        )
        return user

# 접속 유지중인지 확인
class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
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


class StudyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields  = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields  = '__all__'



class Group_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group_User
        fields  = '__all__'
