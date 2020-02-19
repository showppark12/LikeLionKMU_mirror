from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Sum

from accounts.models import StudyGroup

User = get_user_model()


class AbstractBaseBoard(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)  # 게시물 등록 시간 생성
    update_date = models.DateTimeField(auto_now=True)  # 업데이트 될 때만 정보 바뀔때 마다
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    class Meta:
        abstract = True


class Score(models.Model):
    score_type = models.CharField()
    score = models.PositiveIntegerField()


class LectureBoard(AbstractBaseBoard):
    scores = models.ManyToManyField(Score, blank=True, related_name="+", symmetrical=False)

    @property
    def total_score(self):
        self.scores.aggregate(Sum('score'))


class StudyBoard(AbstractBaseBoard):
    study_type = models.IntegerField(default=0)  # 0: 공식모임, 1: 정보공유 2: etc
    personnel = models.IntegerField(default=0)
    group_id = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, related_name="group_board", default=None)
    like = models.ManyToManyField(User, blank=True, related_name="study_like")

    @property
    def total_likes(self):
        return self.like.count()


class NoticeBoard(AbstractBaseBoard):
    notice_date = models.DateField(null=True)
    like = models.ManyToManyField(User, blank=True, related_name="notice_like")
    is_valid_date = models.BooleanField(default=False)

    @property
    def total_likes(self):
        return self.like.count()


class QnABoard(AbstractBaseBoard):
    subject = models.CharField(max_length=200)
    like = models.ManyToManyField(User, blank=True, related_name="qna_like")

    @property
    def total_likes(self):
        return self.like.count()


class AbstractBaseComment(models.Model):
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    class Meta:
        abstract = True


class StudyBoardComment(AbstractBaseComment):
    board = models.ForeignKey(StudyBoard, on_delete=models.CASCADE, related_name="study_comments")


class NoticeBoardComment(AbstractBaseComment):
    board = models.ForeignKey(NoticeBoard, on_delete=models.CASCADE, related_name="notice_comments")


class QnABoardComment(AbstractBaseComment):
    board = models.ForeignKey(QnABoard, on_delete=models.CASCADE, related_name="QnA_comments")
