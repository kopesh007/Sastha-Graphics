from django.shortcuts import render
from django.http import HttpResponse 
from website.models import store_data

def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def banner_page(request):

    ban=store_data.objects.filter(topic="banner")
    pos=store_data.objects.filter(topic="poster")

    return render(request,"banner.html",{"banners":ban,"posters":pos})

def invites(request):
    return render(request, "invitation.html")

def arts(request):
    return render(request,"art.html")

def explore(request):
    return render(request,"explore.html")
# Create your views here.
