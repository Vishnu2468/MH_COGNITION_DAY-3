from django.shortcuts import render

# Create your views here.

from .models import mobile

def mobiles(request):
    elects=mobile.objects.all()
    return render(request,'electronics.html',{'ele':elects})