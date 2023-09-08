from .models import Project
from rest_framework import viewsets, permissions
from .serializers import  Project_serializer


class Project_View_Set (viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Project_serializer
    