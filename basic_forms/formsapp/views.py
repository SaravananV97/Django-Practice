from django.shortcuts import render
from . import the_form
from django.http import HttpResponseRedirect
# Create your views here.
def my_index(request):
    return render(request,'formsapp/index.html')

def form_name_show(request):
    if request.method == "POST":
        form_name = the_form.My_Form(request.POST)
        if form_name.is_valid():
            print("Validation Sucess!")
            print(form_name.cleaned_data['name'])
            print(form_name.cleaned_data['email'])
            print(form_name.cleaned_data['text'])

    else:
        form_name = the_form.My_Form()

    return render(request,'formsapp/form_view.html',{'form':form_name})
