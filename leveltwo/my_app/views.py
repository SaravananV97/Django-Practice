from django.shortcuts import render
from my_app.signup_form import signup
# Create your views here.

def my_index(request):
    return render(request,"my_app/index.html")

def signing_Up(request):
    if request.method == "POST":
        form = signup(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return my_index(request)

    else:
        form = signup()

    return render(request,"my_app/users.html",{'form': form})
