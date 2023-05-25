from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        user = request.POST['username']
        first = request.POST['first_name']
        last = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1==pass2:
            if User.objects.filter(username=user).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                  messages.info(request,"Email Taken")
                  return redirect('register')
            else:
                user=User.objects.create_user(username=user,password=pass1,first_name=first,last_name=last,email=email)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')