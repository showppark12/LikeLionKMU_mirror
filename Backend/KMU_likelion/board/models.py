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
    score_types = models.CharField(max_length=10)
    scores = models.PositiveIntegerField()


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
    is_recorded = models.BooleanField(default=False) #달력 기록여부
    event_name = models.CharField(max_length=20, blank=True, null=True) #달력에 표시될 이벤트의 이름

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
    parent_id = models.ForeignKey("self", on_delete = models.CASCADE, null = True, blank = True)
    is_child = models.BooleanField(default = False) #false는 부모 댓글 true는 대댓글, 대대댓글은 안할꼬얌


