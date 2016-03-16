# coding: utf-8

from rest_framework import serializers

from core.models import Project, Task


"""
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')
"""


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'group')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'group', 'created_at', 'updated_at', 'due_at',
                  'assignee', 'creator')
