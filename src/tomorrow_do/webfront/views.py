# coding: utf-8

from django.views.generic import View
from django.shortcuts import render


class RootView(View):
    def get(self, request):
        return render(request, "index.html")