from django.db import models

from accounts.models import User


class Application(models.Model):
    REVIWING = "R"
    PASS = "P"
    FAIL = "F"
    STATUS = {
        (REVIWING, "심사중"),
        (PASS, "합격"),
        (FAIL, "불합격"),
    }

    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=50, unique=True)
    student_id = models.CharField(max_length=50, default=None)
    birth = models.DateField()
    sex = models.CharField(max_length=50, null=True)
    major = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    pw = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=1, choices=STATUS, default=REVIWING)
    pub_date = models.DateTimeField(auto_now_add=True)  # 게시물 등록 시간 생성
    update_date = models.DateTimeField(auto_now=True)  # 업데이트 될 때만 정보 바뀔때 마다


class Question(models.Model):
    pass


class Answer(models.Model):
    pass


class Evaluation(models.Model):
    applicationform_id = models.ForeignKey(Application, on_delete=models.CASCADE,
                                           related_name="application_evaluation", default=None)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_evaluation", default=None)
    body = models.TextField()
    score = models.FloatField(default=0.0)
    pub_date = models.DateTimeField(auto_now_add=True)
