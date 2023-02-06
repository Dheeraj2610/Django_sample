from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import UserModel

# Create your views here.


def index(request):
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'user_name already exist')
                return redirect(register)
            else:
                new_user = User.objects.create_user(
                    username=user_name, password=password, email=email, first_name=first_name, last_name=last_name,)
                new_user.set_password(password)
                new_user.save()
                print("success")
                return redirect("login_user")
    else:
        print("this is not post method")
        return render(request, "register.html")


def login_user(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        user = authenticate(username=user_name, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login_user')
    else:
        return render(request, "login.html")


def logout_user(request):
    auth.logout(request)
    return redirect('index')
