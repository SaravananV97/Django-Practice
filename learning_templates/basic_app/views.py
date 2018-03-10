from django.shortcuts import render

# Create your views here.

def my_index(request):
    my_context_dict = {'django':" i am a one in 10000 nigger ",'killed':'04/14/1865'}
    return render(request,"basic_app/index.html",my_context_dict)

def my_other(request):
    return render(request,"basic_app/other.html")

def my_relative_url(request):
    return render(request,"basic_app/relative_url_template.html")
