from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from . import views

app_name = "organizations"

urlpatterns = [
    path('', views.IndexView.as_view(), name="orgs-index"),
]