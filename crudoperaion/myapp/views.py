from django.shortcuts import render, redirect
from django.contrib import admin
from myapp.models import User


# Create your views here.
def INDEX(request):
    emp = User.objects.all()
    context = {
        'emp': emp,
    }
    return render(request, 'index.html', context)


def ADD(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        emp = User(
            name=name,
            email=email,
            password=password,
        )
        emp.save()
        return redirect('home')

    return render(request, 'index.html')


def EDIT(request):
    emp = User.objects.all()
    context = {
        'emp': emp,
    }
    return redirect(request, 'index.html', context)


def UPDATE(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        emp = User(
            id=id,
            name=name,
            email=email,
            password=password,
        )
        emp.save()
        return redirect('home')
    return redirect(request, 'index.html')


def DELETE(request, id):
    emp = User.objects.filter(id=id)
    emp.delete()
    context = {
        'emp': emp,
    }
    return redirect('home')
    # return redirect(request, 'index.html', context)
