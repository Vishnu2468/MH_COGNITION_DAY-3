from django.urls import path
from . import views

urlpatterns = [
    path('groceries/',views.groceries,name='groceries'),
]