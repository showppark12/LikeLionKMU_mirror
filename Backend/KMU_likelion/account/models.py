from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    major = models.CharField(max_length = 200, null=True)
    student_id = models.CharField(max_length = 200, null=True)
    is_manager=models.CharField(max_length = 200, null=True)
    start_number=models.CharField(max_length = 200, null=True)
    sns_id=models.CharField(max_length = 200, null=True)
    
