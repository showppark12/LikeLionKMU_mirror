from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('study', views.StudyViewSet)
router.register('notice', views.NoticeViewSet)
router.register('qna', views.QnAViewSet)
router.register('study_comment', views.StudyCommentViewSet)
router.register('notice_comment', views.NoticeCommentViewSet)
router.register('qna_comment', views.QnACommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
