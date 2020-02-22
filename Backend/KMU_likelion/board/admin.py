from django.contrib import admin

from .models import (CareerBoard, Session, NoticeBoard, Submission,
                     NoticeBoardComment, QnABoard, QnABoardComment, Score,
                     StudyBoard, StudyBoardComment)

# boards
admin.site.register(Score)
admin.site.register(Submission)
admin.site.register(Session)
admin.site.register(StudyBoard)
admin.site.register(NoticeBoard)
admin.site.register(QnABoard)
admin.site.register(CareerBoard)

# comments
admin.site.register(StudyBoardComment)
admin.site.register(NoticeBoardComment)
admin.site.register(QnABoardComment)
