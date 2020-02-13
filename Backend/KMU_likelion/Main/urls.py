from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('career', views.CareerViewSet)
router.register('calendar',views.CalendarViewSet)


urlpatterns = [
    path('', include(router.urls)),

] 