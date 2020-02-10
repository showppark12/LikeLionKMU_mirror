from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from rest_framework.decorators import action,api_view
from rest_framework.response import Response

# Create your views here.
class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]     



