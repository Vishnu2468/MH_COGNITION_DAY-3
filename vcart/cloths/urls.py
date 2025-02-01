from django.urls import path
from . import views

urlpatterns = [
    path('cloths/',views.cloth,name='cloths'),
    path('cloths/add/', views.cloth_add, name='cloth-add'),
    path('cloths/edit/<int:cloth_id>/', views.cloth_edit, name='cloth-edit'),
    path('cloths/delete/<int:cloth_id>/', views.cloth_delete, name='cloth-delete'),
]