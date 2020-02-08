from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('study', views.StudyViewSet)
router.register('notice', views.NoticeViewSet)
router.register('QnA', views.QnAViewSet)
router.register('recruit', views.RecuitViewSet)
router.register('study_comment',views.StudyCommentViewSet)
router.register('notice_comment',views.NoticeCommentViewSet)
router.register('QnA_comment',views.QnACommentViewSet)
router.register('Recuit_comment',views.RecuitCommentViewSet)




urlpatterns = [
    path('', include(router.urls)),

] 