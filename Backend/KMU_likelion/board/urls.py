from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('images', views.ImageViewset)

router.register('session', views.SessionViewSet)
router.register('submission', views.SubmissionViewSet)
router.register('study', views.StudyViewSet)
router.register('notice', views.NoticeViewSet)
router.register('qna', views.QnAViewSet)
router.register('career', views.CareerViewSet)

router.register('session_comment', views.SessionCommentViewSet)
router.register('submission_comment', views.SubmissionCommentViewSet)
router.register('study_comment', views.StudyCommentViewSet)
router.register('notice_comment', views.NoticeCommentViewSet)
router.register('qna_comment', views.QnACommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
