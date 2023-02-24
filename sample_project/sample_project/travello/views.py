from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth

from .models import Destination

# Create your views here.
def hydvisits(request):
    if request.user.is_authenticated:
        return render(request,'hydvisits.html')
    else:
        return redirect('login')
def index(request):
    #dest1=Destination()
    #dest1.name='Mumbai'
    #dest1.desc='polluted city'
    #dest1.img='destination_1.jpg'
    #dest1.price=900
    #dest1.offer=False
    #est2=Destination()
    #dest2.name='Hyderabad'
    #dest2.desc='Biryani ka baap'
    #dest2.img='destination_2.jpg'
    #dest2.price=1200
    #dest2.offer=True
    #dest3=Destination()
    #dest3.name='Banglore'
    #dest3.desc='highly traffic city'
    #dest3.img='destination_3.jpg'
    #dest3.price=700
    #dest3.offer=False
    #dests=[dest1,dest2,dest3]
    dests=Destination.objects.all()
    return render(request,'index.html',{'dests':dests})
