from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('study', views.StudyViewSet)
router.register('notice', views.NoticeViewSet)
router.register('QnA', views.QnAViewSet)
router.register('recuit', views.RecuitViewSet)


urlpatterns = [
    path('', include(router.urls)),
 
] 