from django.shortcuts import render
from .models import Service
# Create your views here.


def home(request):
   service_list = Service.objects.all()
   
   data = {'service_list':service_list}
   
   
   return render(request, "home.html",data)