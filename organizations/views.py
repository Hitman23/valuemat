from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, FormView, DeleteView
from . import models

# Create your views here.

class IndexView(TemplateView):
    template_name = "orgs/index.html"


class OrganizationCreateView(CreateView):
    pass


class OrganizationUpdateView(UpdateView):
    pass


class OrganizationDeleteView(DeleteView):
    pass