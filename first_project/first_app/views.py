from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecords,Topic,Webpage
# Create your views here.

def my_index(request):
    return render(request,"first_app/index.html")

def my_help(request):
    dict1 = {'helper':"Welcome to helper page...We are here to Help You!"}
    return render(request,"first_app/help.html",context = dict1)

def my_records(request):
    webpages_list = AccessRecords.objects.order_by("date")
    date_dict = {'access_records':webpages_list}
    return render(request,"first_app/records.html",context = date_dict)
