from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from typing import Optional
from rest_framework.generics import UpdateAPIView
from .models import User
from . import serializers

# Create your views here.
def user_list(request):
    users=User.objects.all()
    #user_cnt=users.count()
    context={'users':users}#,'user_cnt':user_cnt
    return render(request,'user/user_list.html',context)

def login_view(request):
    error_message=None
    #Unbound state of our form
    form=AuthenticationForm()
    if request.method=='POST':#if user submits the form
        #breakpoint()
        #Bound state of our form
        form=AuthenticationForm(data=request.POST)
        
        #Validate the data
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            
            #Authenticate the user
            user:Optional[User]=authenticate(
                username=username,
                password=password,
            )
            if user is not None:
                #use the session to keep the authenticated user's id
                login(request,user)
                #Redirect the user to his profile page
                #the url name
                redirect('profile')
                #if user is not authenticated,what should u do
        else:
            #user's data is not valid,set an error msg to be displayed
            error_message='Sorry,something went wrong.Try again..'
    context={'form':form,'error_message':error_message}
    return render(request,'user/login.html',context)
def profile(request):
    return render(request,'user/profile.html')
class UpdateUser(UpdateAPIView):
    lookup_field='id'
    queryset=User.objects.all()
    serializer_class=serializers.UserModelSerializer
            
            
        