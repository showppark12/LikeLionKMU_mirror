from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('joinform', views.JoinFormViewSet)
router.register('question', views.QuestionViewSet)
router.register('answer', views.AnswerViewSet)
router.register('evaluation', views.EvaluationViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
