# coding: utf-8

from rest_framework import permissions

from django.http import HttpRequest

from core.models import Task, Project


class BelongToOwner(permissions.BasePermission):

    def has_object_permission(self, request: HttpRequest, view, obj):
        if isinstance(obj, Task):
            users = obj.project.group.users
            return self._check_user(request, users)
        if isinstance(obj, Project):
            users = obj.group.users
            return self._check_user(request, users)
        raise NotImplementedError()

    @staticmethod
    def _check_user(request: HttpRequest, users):
        return users.filter(username=request.user.username).count() > 0
