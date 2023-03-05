

from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect




# Create your views here.
def login(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('button')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')

    return render(request,"login.html")

def register(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"USername already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password)
            user.save();
            print("USER CREATED")
            return redirect('login')
        else:
            messages.info(request,"password mismatch")
            return redirect('register')
        return redirect('login')

    return render(request,"register.html")

def button(request):
    return render(request,"button.html")

def form(request):
    return render(request,"form.html")

def msg(request):
    return render(request,"msg.html")





def logout(request):
    auth.logout(request)
    return redirect('/')