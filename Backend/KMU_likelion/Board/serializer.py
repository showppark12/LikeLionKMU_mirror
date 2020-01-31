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
class RecuitSerializer(serializers.ModelSerializer):
     class Meta:
         model = RecuitBoard
         fields = '__all__'