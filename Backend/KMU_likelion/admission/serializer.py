from rest_framework import serializers

from .models import Answer, Application, Evaluation, Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(source= "application_answer", many = True, read_only = True)

    class Meta:
        model = Application
        fields = ['id', 'name', 'student_id', 'phone_number', 'birth', 'sex',
                  'major', 'email', 'pw', 'status', 'pub_date', 'update_date', 'answer']


class EvaluationSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user_id.username')
    application_name = serializers.ReadOnlyField(source='application_id.name')
    user_img = serializers.ImageField(
        source='user_id.img', read_only=True, use_url=True)

    class Meta:
        model = Evaluation
        fields = ['id', 'user_name', 'user_id','full_name','application_name', 'application_id', 'body', 'score', 'pub_date','user_img']
