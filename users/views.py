from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
# Create your views here.


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "users/index.html"
