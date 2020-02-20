from django.contrib import admin

from .models import (LectureBoard, NoticeBoard, NoticeBoardComment, QnABoard,
                     QnABoardComment, Score, StudyBoard, StudyBoardComment)

# boards
admin.site.register(Score)
admin.site.register(LectureBoard)
admin.site.register(StudyBoard)
admin.site.register(NoticeBoard)
admin.site.register(QnABoard)

# comments
admin.site.register(StudyBoardComment)
admin.site.register(NoticeBoardComment)
admin.site.register(QnABoardComment)
