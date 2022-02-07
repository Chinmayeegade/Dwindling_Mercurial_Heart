from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def pgs(request):
    return render(request, "pgs.html")
