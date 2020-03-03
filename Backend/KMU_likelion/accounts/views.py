# api/views.py
import json

from django.contrib.auth import get_user_model
from knox.models import AuthToken
from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializers
from .filters import (GroupUserFilter, MentoringFilter, PortfolioFilter,
                      StudyGroupFilter, UserFilter)
from .models import GroupUser, Mentoring, Portfolio, StudyGroup
from board.models import Session,Submission
User = get_user_model()

class RegistrationAPI(generics.GenericAPIView):
    serializer_class = serializers.CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data["username"]) < 4 or len(request.data["password"]) < 6:
            body = {"message": "short field"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"user": serializers.UserSerializer(user, context=self.get_serializer_context()).data,
                         "token": AuthToken.objects.create(user)[1], })


class LoginAPI(generics.GenericAPIView):
    serializer_class = serializers.LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({"user": serializers.UserSerializer(user, context=self.get_serializer_context()).data,
                         "token": AuthToken.objects.create(user)[1], })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    action_serializer_classes = {"activity": serializers.UserActivitySerializer}
    filter_class = UserFilter

    def get_serializer_class(self):
        return self.action_serializer_classes.get(self.action, self.serializer_class)

    @action(detail=True, methods=["GET"])
    def activity(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"])
    def get_mymentees(self, request, *args, **kwargs):
        mentor = self.get_object()
        mentees = Mentoring.objects.filter(mentor=mentor.id)
        serializer = serializers.MenteeSerializer(mentees, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"])
    def get_mymentors(self, request, *args, **kwargs):
        mentee = self.get_object()
        mentors = Mentoring.objects.filter(mentee=mentee.id)
        serializer = serializers.MentorSerializer(mentors, many=True)
        return Response(serializer.data)
    
    @action(detail = False, methods=["POST"])
    def delete_mentoring(self, request, *args, **kwargs):
        json_mentoring = request.body
        mentoring = json.loads(json_mentoring)
        mentor = mentoring['mentor_id']
        mentee = mentoring['mentee_id']
        try:
            obj_mentoring = Mentoring.objects.get(mentor=mentor,mentee = mentee)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        obj_mentoring.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail = True, methods = ["GET"])
    def get_mygroup(self,request, *args, **kwargs):
        myuser = self.get_object()
        studygroups =  GroupUser.objects.filter(user_id = myuser)
        serializer = serializers.MyGroupSerializer(studygroups, many = True)
        return Response(serializer.data)
    
    @action(detail = True, methods = ["POST"])
    def get_submit_status(self,request, *args, **kwargs):
        get_user = self.get_object()
        json_assignment = request.body
        assignment = json.loads(json_assignment)
        assignment_id = assignment['session_id']
        try:
           get_assignment = Session.objects.get(id = assignment_id)
           get_session =  Session.objects.get(id = get_assignment.lecture.id) #해당 lecture 객체 가져오기
           print("유저 기수 :",get_user.start_number)
           print("세션 기수 :",get_session.start_number)
           if get_user.start_number == get_session.start_number: # 해당 기수 멤버의 세션인지 확인 작업
               try:
                   user_submit =  Submission.objects.get(user_id = get_user, lecture = assignment_id)
                   
                   # datefield string으로 형변환(datetimefield 어디 비교 하는거 없나....? 개빡치네)
                   str_user_update = str(user_submit.update_date)
                   str_dead_line = str(get_assignment.deadline) 
                   
                   
                   # 스트링 자르기
                   print("스트링 업데이트 타임:",str_user_update)
                   print("스트링 데드라인:", str_dead_line)
                   user_month = str_user_update.split()
                   session_month = str_dead_line.split()
                   print("스트링 업데이트 타임 스플릿:",user_month)
                   print("스트링 데드라인 스플릿:", session_month)
                   user_split = user_month[0].split('-')
                   user_split2 = user_month[1].split(':')
                   print("스트링 업데이트 타임 스플릿 그 두번째:",user_split, user_split2)
                   session_split = session_month[0].split('-')
                   session_split2 = session_month[1].split(':')
                   print("스트링 데드라인 스플릿:",session_split, session_split2)
                   # 스트링 자르기


                   if int(user_split[0]) > int(session_split[0]) : #년도 비교
                       return  Response({'status': 'LATE'})
                   else:
                       if int(user_split[1]) > int(session_split[1]): # 달 비교
                           return  Response({'status': 'LATE'})
                       else:
                           if int(user_split[1]) == int(session_split[1]) and int(user_split[2]) > int(session_split[2]): # 일 비교
                               return  Response({'status': 'LATE'})
                           
                           else:
                               if int(user_split[2]) == int(session_split[2]) and int(user_split2[0]) > int(session_split2[0]):
                                   return  Response({'status': 'LATE'})
                               else:
                                   if int(user_split2[0]) == int(session_split2[0]):
                                       return  Response({'status': 'LATE'})
                                    
                                   else:
                                         return  Response({'status': 'COMPLETE'})

               except Submission.DoesNotExist:
                   return Response({'status': 'NOT_SUBMIT'})
           else:
               return Response({'status': 'UNQUALIFIED' })

        except:
            return Response({'status': 'NONE'})
        
        def post(self,request, *args, **kwargs):
            serializer = serializers.UserSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = HTTP_201_CREATED)
            else:
                return Response(serializer.error, status = HTTP_400_BAD_REQUEST)


class StudyGroupViewSet(viewsets.ModelViewSet):
    queryset = StudyGroup.objects.all().order_by('pub_date')
    serializer_class = serializers.StudyGroupSerializer
    filter_class = StudyGroupFilter

    @action(detail=True, methods=["GET"])
    def group_users(self, request, *args, **kwargs):
        group = self.get_object()
        group_users = group.groupuser_set.all()
        serializer = serializers.GroupUserSerializer(group_users, many=True)
        return Response(serializer.data)
    @action(detail=True, methods=["GET"])
    def get_captain(self, request, *args, **kwargs):
        group = self.get_object()
        groupuser = GroupUser.objects.filter(group_id = group)
        for checkuser in groupuser:
            if checkuser.is_captain == True:
                serializer = serializers.CaptainSerializer(checkuser)
                return Response(serializer.data)



class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = serializers.PortfolioSerializer
    filter_class = PortfolioFilter


class GroupUserViewSet(viewsets.ModelViewSet):
    queryset = GroupUser.objects.all()
    serializer_class = serializers.GroupUserCreateSerializer
    filter_class = GroupUserFilter


class MentoringViewSet(viewsets.ModelViewSet):
    queryset = Mentoring.objects.all()
    serializer_class = serializers.MentoringSerializer
    filter_class = MentoringFilter

    @action(detail=False, methods=["GET"])
    def get_mentors(self, request, *args, **kwargs):
        queryset = Mentoring.objects.exclude(mentor=None)
        querylist = []
        # 중복제거
        for qs in queryset:
            flags = False
            if not querylist:
                querylist.append(qs)
                flags = True
            else:
                for query in querylist:
                    if query.mentor.id == qs.mentor.id:
                        flags = True
            if not flags:
                querylist.append(qs)

        serializer = serializers.MentorSerializer(querylist, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["GET"])
    def get_mentees(self, request, *args, **kwargs):
        queryset = Mentoring.objects.exclude(mentee=None)
        querylist = []
        # 중복제거
        for qs in queryset:
            flags = False
            if not querylist:
                querylist.append(qs)
                flags = True
            else:
                for query in querylist:
                    if query.mentee.id == qs.mentee.id:
                        flags = True
            if not flags:
                querylist.append(qs)

        serializer = serializers.MenteeSerializer(querylist, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        check = serializer.validated_data
        mentoring_log = Mentoring.objects.filter(mentor=check['mentor'].id)
        for mentor in mentoring_log:
            if mentor.mentee.id == check['mentee'].id:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
