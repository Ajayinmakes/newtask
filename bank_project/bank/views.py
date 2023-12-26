from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from bank.models import Examble


# Create your views here.


def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username=username,password=password)
        user.save()

        return redirect('login')

    return render(request, 'register.html')


def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('new page')

        else:
            return redirect('.')

    return render(request, "loginn.html")


def registrationform(request):
    if request.method == 'POST':
        name = request.POST.get('full name',)
        email= request.POST.get('email address',)
        number = request.POST.get('phone number',)
        dob = request.POST.get('date of birth',)
        gender = request.POST.get('gender',)
        materials = request.POST.get('materials provide',)
        address = request.POST.get('address',)
        district = request.POST.get('district',)
        branches = request.POST.get('branches',)
        account = request.POST.get('account',)

        registerform = Examble(name=name,email=email,number=number,dob=dob,gender=gender,materials=materials,
                           address=address,district=district,branches=branches,account=account)
        registerform.save()
        return render(request,'confirmation.html')
    return render(request, 'registrationform.html')


def newpage(request):
    return render(request,"newpage.html")


def thrissur(request):
    return render(request,"thrissur.html")


def kollam(request):
    return render(request,"kollam.html")


def palakkad(request):
    return render(request,"palakkad.html")


def Eranamkulam(request):
    return render(request, "Eranamkulam.html")


def wayanad(request):
    return render(request, "wayanad.html")