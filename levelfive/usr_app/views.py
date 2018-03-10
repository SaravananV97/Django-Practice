from django.shortcuts import render
from usr_app.forms import UserFieldInfoForm,UserForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,"usr_app/index.html")

def usr_login(request):
    if request.method == "POST":
        usr_name = request.POST.get('usrname')
        password = request.POST.get('pwd')
        user = authenticate(username = usr_name,password = password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponseRedirect("Error: Account not Active!")
        else:
            print("Someone tried to login and failed")
            print("Username: {} Password: {}".format(usr_name,password))
            return HttpResponseRedirect("Login Failed!")
    else:
        return render(request,"usr_app/login.html",{})

@login_required
def usr_logout(request):
    logout(request)
    return render(request,"usr_app/logout.html",{})

@login_required
def special(request):
    return render(request,"usr_app/special.html",{})

def register(request):
    registered = False
    if request.method == "POST": # if submitted
        user_form = UserForm(data = request.POST) # get username,email,password
        profile_form = UserFieldInfoForm(data = request.POST) # get url,profile pic

        if user_form.is_valid() and profile_form.is_valid():

            usr_db = user_form.save() #save the form in db
            usr_db.set_password(usr_db.password)#hash password
            usr_db.save()#save password in db

            profile_db = profile_form.save(commit = False) # save after making changes
            profile_db.usr = usr_db # link user form and profile form

            if 'profile_pic' in request.FILES: # if http had picture
                profiledb.profile_pic = request.Files['profile_pic'] # make it ready to store it in db

            profile_db.save()# save in db

            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm() # Refreshed or first time visit
        profile_form = UserFieldInfoForm()

    return render(request,"usr_app/Registration.html",{'user_form':user_form,'user_profile_form':profile_form,"registered":registered})
