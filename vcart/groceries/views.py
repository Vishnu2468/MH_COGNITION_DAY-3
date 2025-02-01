from django.shortcuts import render

# Create your views here.

from .models import Grocery
def groceries(request):
    groce=Grocery.objects.all()
    return render(request,'groceries.html',{'groce':groce})