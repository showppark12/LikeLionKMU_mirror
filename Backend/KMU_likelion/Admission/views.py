from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
import json
# Create your views here.


class JoinFormViewSet(viewsets.ModelViewSet):
    queryset = JoinForm.objects.all()
    serializer_class = JoinFormSerializer
    @action(detail=True)
    def count_score(self,request, *args, **kwargs):
        joinform = self.get_object()
        evaluations = joinform.join_evaluation.all()
        total_score = 0.0
        count = 0.0
        for evaluation in evaluations:
            total_score = total_score +evaluation.score
            count += 1
     
        average_score = total_score/count

        return Response({'total_score': total_score,'average_score':average_score})

    @action(detail = False, methods = ['POST'])
    def get_joinform(self,request,*args, **kwargs):
        json_joinform = request.body
        join = json.loads(json_joinform)
        number = join['number']
        password = join['password'] 
        try:
            joinform = JoinForm.objects.filter(phone_number = number)
            joinform = joinform[0]
        except:
            return Response({'joinform':'이 번호는 없는 전화번호입니다.'})
        

        if joinform.pw == password:
            serializer = JoinFormSerializer(joinform)
            return Response(serializer.data)
        
        else: 
            return Response({'joinform':'잘못된 비밀번호 입니다.'})
        



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
            qs=qs.filter(joinform_id = joinform)
        elif question:
            qs=qs.filter(question_id = question)

        return qs

class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        joinform_id = self.request.query_params.get('joinform_id','')
        user_id = self.request.query_params.get('user_id','')
        if joinform_id:
            qs = qs.filter(joinform_id = joinform_id)
        elif user_id:
            qs = qs.filter(user_id = user_id)
        return qs
    
    # @action(detail=False)
    # def count_score(self,request, *args, **kwargs):
    #     # print("제이슨:___", request.body)
    #     # json_object = json.loads(request.body)
    #     # joinform_id = json_object['pk']
    #     qs = super().get_queryset()
    #     evaluations = qs.filter(joinform_id = pk)
    #     total_score = 0.0
    #     for  evaluation in evaluations:
    #         total_score = total_score +evaluation.score
    #     rater = evaluations.user_id.count()
        
    #     average_score = total_score/rater

    #     return Response({'total_score': total_score,'average_score':average_score})
  




