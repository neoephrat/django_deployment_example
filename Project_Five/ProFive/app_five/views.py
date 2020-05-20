from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_five.form import UserProfileInfoForm, UserForm
from .import form
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout

# Create your views here.

def index(request):
    return render(request,'my_pages/index.html')



    #user login
#login_required
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get ('username')
        password = request.POST.get ('password')
        user= authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return render(request,'my_pages/index.html')
            else:
                return HttpResponse ('ACCOUNT NOT ACTIVE!')
        else:
            print('Someone tried to login and failed')
            print("Username:{} and Password:{}".format(username,password))
            return HttpResponse('Invalid login detail supplied!')
    else:
        #return HttpResponse ('ACCOUNT NOT ACTkkhkhIVE!')
        return render(request,'my_pages/login.html')


#user logout
@login_required
def user_logout(request):
    logout(request)
    return render(request,'my_pages/thank_you.html')

def thank_you(request):
    return render(request, 'my_pages/thank_you.html')




def regestration(request):
    user_form= UserForm()
    profile_form= UserProfileInfoForm()
    regestred= False
    if request.method == 'POST':
        user_form= UserForm(data=request.POST)
        profile_form= UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user= user_form.save()
        #grabbing the password for the user form and hashing it for security
            user.set_password(user.password)
            user.save()

 #commiting it to false first so that it wont create errors
            profile=profile_form.save(commit=False)
            #setting up onetoone relashionship
            profile.user=user


            #checking if the user provided a profile_pic

        if 'profile_pic' in request.FILES:
            profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            regestred=True
        else:
            print(user_form.errors, profile_form.errors)
    else:
      user_form=UserForm()
      profile_form=UserProfileInfoForm()
    return render(request,'my_pages/regestration.html',{'regestred':regestred,
                                                        'user_form':user_form,
                                                        'profile_form':profile_form})
