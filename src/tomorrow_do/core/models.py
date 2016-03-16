# coding: utf-8

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(blank=True)
    icon = models.ImageField(null=True, blank=True)


class Auth(models.Model):
    user = models.ForeignKey(User, related_name="auth_accounts")
    type = models.CharField(max_length=100)
    client_id = models.CharField(max_length=512)
    client_secret = models.CharField(max_length=512)


class Group(models.Model):
    name = models.CharField(max_length=128)
    users = models.ManyToManyField(User, related_name="groups")


class Project(models.Model):
    name = models.CharField(max_length=128)
    group = models.ForeignKey(Group, related_name="projects")


class Task(models.Model):
    title = models.CharField(max_length=256)
    group = models.ForeignKey(Project, related_name="tasks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_at = models.DateTimeField(null=True, blank=True)
    assignee = models.ManyToManyField(User, related_name="assigned_tasks")
    creator = models.ForeignKey(User, related_name="created_tasks")
