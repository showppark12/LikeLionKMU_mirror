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


class EvaluationSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user_id.username')
    joinform_name = serializers.ReadOnlyField(source = 'joinform_id.name')
    class Meta:
        model = Evaluation
        fields = ['id','user_name','user_id','joinform_name','joinform_id','body','score','pub_date']