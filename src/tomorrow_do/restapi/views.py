# coding: utf-8

import django_filters
from rest_framework import viewsets, filters

from core.models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from .permissions import BelongToOwner


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [BelongToOwner, ]

    def get_queryset(self):
        return Project.objects.filter(group__users=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [BelongToOwner, ]

    def get_queryset(self):
        return Task.objects.filter(project__group__users=self.request.user)
