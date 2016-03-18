# coding: utf-8

from rest_framework import serializers

from core.models import Project, Task, Group, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', )


class GroupSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = ('id', 'name', 'users')


class ProjectSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)
    group_id = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), source='group', write_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'group', 'group_id')

    def create(self, validated_data):
        assignee = validated_data.pop('assignee')
        user = self.context['request'].user
        validated_data['creator_id'] = user.id
        task = Task.objects.create(**validated_data)
        for assign_user in assignee:
            task.assignee.add(assign_user)
        return task


class TaskSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    project_id = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), source='project', write_only=True)
    creator = UserSerializer(read_only=True)

    assignee = UserSerializer(read_only=True, many=True)
    assignee_ids = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='assignee', write_only=True, many=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'project_id', 'project', 'created_at', 'updated_at', 'due_at',
                  'assignee', 'assignee_ids', 'creator')

    def create(self, validated_data):
        assignee = validated_data.pop('assignee')
        user = self.context['request'].user
        validated_data['creator_id'] = user.id
        task = Task.objects.create(**validated_data)
        for assign_user in assignee:
            task.assignee.add(assign_user)
        return task
