from rest_framework import viewsets, permissions,status
from .models import *
from .serializer import *
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
import json
from .filterings import *

# Create your views here.


class JoinFormViewSet(viewsets.ModelViewSet):
    queryset = JoinForm.objects.all()
    serializer_class = JoinFormSerializer
    filter_class=JoinFormFilter
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
        email = join['email']
        password = join['password'] 
        print(email)
        try:
            joinform = JoinForm.objects.get(email = email)
            answers=Answer.objects.filter(joinform_id=joinform.id)
            print(answers)
        except:
            return Response({'joinform':'이 이메일은 없는 이메일입니다.'},status=status.HTTP_404_NOT_FOUND)
        

        if joinform.pw == password:
            serializer = JoinFormSerializer(joinform)
            answer_serializer=AnswerSerializer(answers,many=True)
            return Response({"join_forms":serializer.data,"answers":answer_serializer.data})
        
        else: 
            return Response({'joinform':'잘못된 비밀번호 입니다.'},status=status.HTTP_404_NOT_FOUND)
        



class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_class=QuestionFilter

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_class=AnswerFilter

    @action(detail = False, methods = ['POST'])
    def post_answers(self,request,*args, **kwargs):
        json_datas=request.body
        datas=json.loads(json_datas)
        answer_list=datas['answers']
        join_id=datas['joinform_id']
        join_instance=JoinForm.objects.get(id=join_id)
        for question_id,answer in answer_list.items():
         
            tmp=Answer()
            tmp.joinform_id=join_instance
            tmp.question_id=Question.objects.get(id=question_id)
            tmp.body=answer
            tmp.save()
        answers=Answer.objects.filter(joinform_id=join_id)
        serializer=AnswerSerializer(answers,many=True)
        return Response(serializer.data)
        




class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    filter_class=EvaluationFilter

   

