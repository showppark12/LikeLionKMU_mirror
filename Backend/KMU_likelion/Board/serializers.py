from .models import *
from rest_framework import serializers

#스터디 게시판 Serializer
class StudySerializer(serializers.ModelSerializer):
     author_name = serializers.ReadOnlyField(source='user_id.username')
     group_name = serializers.ReadOnlyField(source='group_id.username')
     class Meta:
         model = StudyBoard
         fields =  ['id','author_name','body','user_id','title','pub_date','update_date','like','total_likes','study_type','personnel','group_id']

#공지 게시판 Serializer
class NoticeSerializer(serializers.ModelSerializer):
     author_name = serializers.ReadOnlyField(source='user_id.username')
     class Meta:
         model = NoticeBoard
         fields = ['id','author_name','body','user_id','title','pub_date','update_date','like','total_likes','notice_date']

#QnA 게시판 Serializer
class QnASerializer(serializers.ModelSerializer):
     author_name = serializers.ReadOnlyField(source='user_id.username')
     class Meta:
         model = QnABoard
         fields = ['id','author_name','body','user_id','title','subject','pub_date','update_date','like','total_likes']
#질문 게시판 Serializer
class RecruitSerializer(serializers.ModelSerializer): 
     author_name = serializers.ReadOnlyField(source='user_id.username')
     class Meta:
         model = RecruitBoard
         fields = ['id','author_name','body','user_id','title','pub_date','update_date','like','total_likes','purpose']


#밑에는 댓글이염

#스터디 댓글 Serializer
class StudyCommentSerializer(serializers.ModelSerializer):     
     author_name = serializers.ReadOnlyField(source='user_id.username')
     class Meta:
         model = StudyComments
         fields = ['id','author_name','body','user_id','board','pub_date','update_date']

#공지 댓글 Serializer
class NoticeCommentSerializer(serializers.ModelSerializer):
     author_name = serializers.ReadOnlyField(source='user_id.username')
     class Meta:
         model = NoticeComments
         fields = ['id','author_name','body','user_id','board','pub_date','update_date']

#QnA 댓글 Serializer
class QnACommentSerializer(serializers.ModelSerializer):
     author_name = serializers.ReadOnlyField(source='user_id.username')
     class Meta:
         model = QnAComments
         fields = ['id','author_name','body','user_id','board','pub_date','update_date']

#질문 댓글 Serializer
class RecruitCommentSerializer(serializers.ModelSerializer):
     author_name = serializers.ReadOnlyField(source='user_id.username')
     class Meta:
         model = RecruitComments
         fields = ['id','author_name','body','user_id','board','pub_date','update_date']



