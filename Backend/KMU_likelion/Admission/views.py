from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
# Create your views here.


class JoinFormViewSet(viewsets.ModelViewSet):
    queryset = JoinForm.objects.all()
    serializer_class = JoinFormSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_queryset(self):
        qs=super().get_queryset()
        joinform = self.request.query_params.get('joinform','')
        question = self.request.query_params.get('question','')
        if joinform:
            qs=qs.filter(belong_to_join=joinform)
        elif question:
            qs=qs.filter(belong_to_question = question)
        return qs

class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer




