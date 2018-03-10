from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.signing_Up,name = "users"),
]
