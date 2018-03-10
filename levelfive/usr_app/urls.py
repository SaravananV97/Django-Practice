from django.urls import path
from usr_app import views

app_name = 'usr_app'

urlpatterns = [path("register/",views.register,name = 'register'),
               path("login/",views.usr_login,name = "login"),
                ]
