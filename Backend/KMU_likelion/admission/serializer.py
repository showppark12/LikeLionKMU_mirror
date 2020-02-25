from rest_framework import serializers

from .models import Answer, Application, Evaluation, Question


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
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
    application_name = serializers.ReadOnlyField(source='application_id.name')

    class Meta:
        model = Evaluation
        fields = ['id', 'user_name', 'user_id','full_name','application_name', 'application_id', 'body', 'score', 'pub_date']
