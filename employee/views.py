from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def index(request):
    return render(request, 'index.html')


def admin_login(request):
    return render(request, 'admin_login.html')


def emp_login(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username = username, password=password)
        if user:
            login(request, user)
        else:
            print('Error')
    return render(request, 'emp_login.html', locals())


def emp_home(request):
    return render(request, 'emp_home.html')