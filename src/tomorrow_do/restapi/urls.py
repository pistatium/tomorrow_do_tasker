# coding: utf-8


from rest_framework import routers
from .views import ProjectViewSet, TaskViewSet


router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, base_name='projects')
router.register(r'tasks', TaskViewSet, base_name='tasks')
