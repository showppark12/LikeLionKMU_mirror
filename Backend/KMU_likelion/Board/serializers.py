from .models import *
from rest_framework import serializers

#스터디 게시판 Serializer
class StudySerializer(serializers.ModelSerializer):
     class Meta:
         model = StudyBoard
         fields = '__all__'

#공지 게시판 Serializer
class NoticeSerializer(serializers.ModelSerializer):
     class Meta:
         model = NoticeBoard
         fields = '__all__'

#QnA 게시판 Serializer
class QnASerializer(serializers.ModelSerializer):
     class Meta:
         model = QnABoard
         fields = '__all__'

#질문 게시판 Serializer
class RecruitSerializer(serializers.ModelSerializer):
     class Meta:
         model = RecruitBoard
         fields = '__all__'


#밑에는 댓글이염

#스터디 댓글 Serializer
class StudyCommentSerializer(serializers.ModelSerializer):     
     class Meta:
         model = StudyComments
         fields = '__all__'

#공지 댓글 Serializer
class NoticeCommentSerializer(serializers.ModelSerializer):
     author_name = serializers.ReadOnlyField(source='user_id.username')
     class Meta:
         model = NoticeComments
         fields = ['id','author_name','body','user_id','board']

#QnA 댓글 Serializer
class QnACommentSerializer(serializers.ModelSerializer):
     class Meta:
         model = QnAComments
         fields = '__all__'

#질문 댓글 Serializer
class RecruitCommentSerializer(serializers.ModelSerializer):
     class Meta:
         model = RecruitComments
         fields = '__all__'


