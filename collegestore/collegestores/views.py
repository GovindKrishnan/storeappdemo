from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print("User Created")
                return redirect('login')

        else:
            print("Password Not Matching")
            messages.info(request, "Password Not Matching")
            return redirect('register')
    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('order')
        else:
            messages.info(request, "Invalid Credentials")

    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def order(request):
    return render(request, "order.html")


def success(request):
    return render(request, "success.html")
