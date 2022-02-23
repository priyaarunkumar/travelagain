from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import travel
from . models import cricket

# Create your views here.
def fun(request):
    result=travel.objects.all()
    re=cricket.objects.all()

    return render(request,"index.html",{'result':result,'re':re})

def regi(request):



     if request.method == 'POST':

         username = request.POST['username']
         password = request.POST['password']
         first_name = request.POST['first_name']
         con = request.POST['con']

         if (password == con):



             if User.objects.filter(username=username).exists():





                messages.info(request, "username already taken")

                return redirect('regi')
             else:


                user = User.objects.create_user(username=username, password=password, first_name=first_name)
                user.save()
                messages.info(request, "user creatted")

                return redirect('priyaapp/login')








     return render(request, "register.html")


# def search(request):
#     return render(request,"search.html")
