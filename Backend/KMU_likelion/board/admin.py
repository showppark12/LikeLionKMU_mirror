from django.contrib import admin

from . import models

# boards
admin.site.register(models.Score)
admin.site.register(models.Submission)
admin.site.register(models.Session)
admin.site.register(models.StudyBoard)
admin.site.register(models.NoticeBoard)
admin.site.register(models.QnABoard)
admin.site.register(models.CareerBoard)

# comments
admin.site.register(models.StudyBoardComment)
admin.site.register(models.NoticeBoardComment)
admin.site.register(models.QnABoardComment)
