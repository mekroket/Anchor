from django.shortcuts import render

def Register(request):
    return render(request,"pages/register.html")