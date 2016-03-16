# coding: utf-8

from rest_framework import permissions

from core.models import Task, Project


class BelongToOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Task):
            users = obj.project.group.users
            return self._check_user(request, users)
        if isinstance(obj, Project):
            users = obj.group.users
            return self._check_user(request, users)
        raise NotImplementedError()

    @staticmethod
    def _check_user(request, users):
        return users.filter(name=request.user).count() > 0
