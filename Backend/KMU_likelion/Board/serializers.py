from rest_framework import serializers

from .models import (NoticeBoard, NoticeComment, QnABoard, QnAComment, StudyBoard, StudyComment)


# 스터디 게시판 Serializer
class StudySerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')
    group_name = serializers.ReadOnlyField(source='group_id.name')

    class Meta:
        model = StudyBoard
        fields = ['id', 'author_name', 'body', 'user_id', 'title', 'pub_date', 'update_date',
                  'like', 'total_likes', 'study_type', 'personnel', 'group_name', 'group_id']


# 공지 게시판 Serializer
class NoticeSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = NoticeBoard
        fields = ['id', 'author_name', 'body', 'user_id', 'title', 'pub_date',
                  'update_date', 'like', 'total_likes', 'notice_date', 'is_valid_date']


# QnA 게시판 Serializer
class QnASerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = QnABoard
        fields = ['id', 'author_name', 'body', 'user_id', 'title',
                  'subject', 'pub_date', 'update_date', 'like', 'total_likes']


# 스터디 댓글 Serializer
class StudyCommentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')
    user_img = serializers.ImageField(source='user_id.img', read_only=True, use_url=True)

    class Meta:
        model = StudyComment
        fields = ['id', 'author_name', 'body', 'user_id', 'board', 'pub_date', 'update_date', 'user_img']


# 공지 댓글 Serializer
class NoticeCommentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')
    user_img = serializers.ImageField(source='user_id.img', read_only=True, use_url=True)

    class Meta:
        model = NoticeComment
        fields = ['id', 'author_name', 'body', 'user_id', 'board', 'pub_date', 'update_date', 'user_img']


# QnA 댓글 Serializer
class QnACommentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')
    user_img = serializers.ImageField(source='user_id.img', read_only=True, use_url=True)

    class Meta:
        model = QnAComment
        fields = ['id', 'author_name', 'body', 'user_id', 'board', 'pub_date', 'update_date', 'user_img']
