from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('joinform', views.JoinFormViewSet)
router.register('question', views.QuestionViewSet)
router.register('answer', views.AnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),

] 