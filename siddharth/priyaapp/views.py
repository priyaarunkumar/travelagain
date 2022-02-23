from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)

            return redirect('/')
        else:
            return redirect('login')

    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        first_name=request.POST['first_name']
        con=request.POST['con']
        if(password==con):
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('register')
            else:




              user=User.objects.create_user(username=username,password=password,first_name=first_name)
              user.save()
              messages.info(request,"user creatted")
              return redirect('login')
        else:
            messages.info(request,"not saved")

    return render(request,"register.html")
