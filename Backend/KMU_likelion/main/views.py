from rest_framework import viewsets, permissions
from .models import *
from .serializer import *
from rest_framework.decorators import action

class HashTagViewSet(viewsets.ModelViewSet):
    queryset = HashTag.objects.all()
    serializer_class = HashTagSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    