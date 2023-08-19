from django.shortcuts import render
from .models import Advertisement

def index (request):
    adverts = Advertisement.objects.all()
    context = {'adverts': adverts}
    return render(request,'index.html', context)

def topSellers (request):
    return render(request,'top-sellers.html')

def advertisement_post (request):
    return render(request,'advertisement-post.html')

def register (request):
    return render(request,'register.html')

def login (request):
    return render(request,'login.html')

def profile (request):
    return render(request,'profile.html')

def advertisement_detail (request):
    return render(request,'advertisement.html')

def back (request):
    return render(request,'index.html')