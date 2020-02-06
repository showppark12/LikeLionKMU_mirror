from .models import *
from rest_framework import serializers

class JoinFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinForm
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'