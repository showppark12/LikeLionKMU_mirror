from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('user', views.UserViewSet)
router.register('studygroup',views.StudyGroupViewSet)
router.register('studygroup_user',views.StudyGroup_UserViewSet)
urlpatterns = [
    path("hello/", HelloAPI),
    path("auth/register/", RegistrationAPI.as_view()),
    path("auth/login/", LoginAPI.as_view()),
    path('', include(router.urls)),
]