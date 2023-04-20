from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Doctor, Patient
import os

def HomePage(request):
    return render(request, 'home.html')

def SignupPageForDoctor(request):
    if request.method == 'POST':
        data = Doctor()
        if request.POST.get('password1') != request.POST.get('password2'):
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            data.firstname = request.POST.get('firstname')
            data.lastname = request.POST.get('lastname')
            data.profile_picture = request.POST.get('profile')
            data.username = request.POST.get('username')
            data.email = request.POST.get('email')
            data.address = request.POST.get('address')
            data.password = request.POST.get('password1')
            data.confirm_password = request.POST.get('password2')
            data.save()
            return redirect('loginDoctor')
    return render(request, 'signupDoctor.html')

def SignupPageForPatient(request):
    if request.method == 'POST':
        data = Patient()
        if request.POST.get('password1') != request.POST.get('password2'):
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            data.firstname = request.POST.get('firstname')
            data.lastname = request.POST.get('lastname')
            data.profile_picture = request.POST.get('profile')
            data.username = request.POST.get('username')
            data.email = request.POST.get('email')
            data.address = request.POST.get('address')
            data.password = request.POST.get('password1')
            data.confirm_password = request.POST.get('password2')
            data.save()
            return redirect('loginPatient')
    return render(request, 'signupPatient.html')

@csrf_protect
def LoginPageForDoctor(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('pass')
        data = Doctor.objects.get(username=uname)
        if data.username == uname and data.password == pass1:
            return render(request, 'showdata.html', {'bio':'Doctor Detail','detail':data})

        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'loginDoctor.html')

def LoginPageForPatient(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('pass')
        data = Patient.objects.get(username=uname)
        if data.username == uname and data.password == pass1:
            return render(request, 'showdata.html', {'bio': 'Patient Detail', 'detail': data})

        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'loginPatient.html')
