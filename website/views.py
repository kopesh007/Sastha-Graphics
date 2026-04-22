from django.shortcuts import render
from django.http import HttpResponse 

def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def banner_page(request):
    return render(request,"banner.html")

def invites(request):
    return render(request, "invitation.html")

def arts(request):
    return render(request,"art.html")
# Create your views here.
