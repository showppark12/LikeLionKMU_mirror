from django.db import models
from Board.models import *
class HashTag(models.Model):
    board_id=models.ManyToManyField(Board, blank=True,related_name="Board_hashtag")
    Tag=models.CharField(max_length=100,null=True)

