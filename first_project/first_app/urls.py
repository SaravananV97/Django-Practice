from django.urls import path
from . import views
urlpatterns = [
    path("",views.my_records,name = "records")
    ,path("",views.my_help,name = "help")]
