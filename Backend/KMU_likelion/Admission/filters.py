import django_filters
from django_filters import filters

from .models import Answer, Application, Evaluation, Question


class JoinFormFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Application
        fields = '__all__'


class QuestionFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Question
        fields = '__all__'


class AnswerFilter(django_filters.rest_framework.FilterSet):
    application = filters.NumberFilter(field_name="application_id__id")
    question = filters.NumberFilter(field_name="question_id__id")

    class Meta:
        model = Answer
        fields = '__all__'


class EvaluationFilter(django_filters.rest_framework.FilterSet):
    application_id = filters.NumberFilter(field_name="application_id__id")
    user_id = filters.NumberFilter(field_name="user_id__id")

    class Meta:
        model = Evaluation
        fields = '__all__'
