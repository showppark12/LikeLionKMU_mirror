from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from . import views
from knox import views as knox_views

router = DefaultRouter()
router.register('user', views.UserViewSet)
router.register('studygroup',views.StudyGroupViewSet)
router.register('portfolio',views.PortfolioViewSet)
router.register('group_user',views.Group_UserViewSet)

urlpatterns = [
    # path("hello/", HelloAPI),
    # path('auth/', include('knox.urls')),
    path("auth/register/", RegistrationAPI.as_view()),
    path("auth/login/", LoginAPI.as_view()),
    path("auth/logout/", knox_views.LogoutView.as_view(), name='knox_logout'),
    path('', include(router.urls)),
]