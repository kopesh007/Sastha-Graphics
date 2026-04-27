from django.shortcuts import render
from django.http import HttpResponse 
from website.models import store_data,user_data
from website.form import ContactForm

def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def banner_page(request):

    ban=store_data.objects.filter(topic="banner")
    pos=store_data.objects.filter(topic="poster")

    return render(request,"banner.html",{"banners":ban,"posters":pos})

def invites(request):
    data=store_data.objects.filter(topic="invitation")
    return render(request, "invitation.html",{"data":data})

def arts(request):
    data=store_data.objects.filter(topic="digital art")
    return render(request,"art.html",{"data":data})

def explore(request):
    data=store_data.objects.all().order_by('topic')  #  here, data is a list
    return render(request,"explore.html",{"data":data})



def contact(request):
    if request.method=="POST":
        data=ContactForm(request.POST)
        if data.is_valid():
            user_data.objects.create(
                name=data.cleaned_data['name'],
                email=data.cleaned_data['email'],
                contact=data.cleaned_data['number'],
                message=data.cleaned_data['interest']
            )
            msg="Data Has Been Submitted"
            return render(request,"contact.html",{"message":msg})   
        else:
            name=request.POST["name"]
            email=request.POST["email"]
            number=request.POST["number"]
            message=request.POST["interest"]
            msg="Data Hasn't Been Submitted Yet !"
            return render(request,"contact.html",{"data":data,"n_value":name,"e_value":email,"m_value":message,"nu_value":number,"message":msg})
    elif request.method=="GET":
        return render(request,"contact.html")
    
# Create your views here.
