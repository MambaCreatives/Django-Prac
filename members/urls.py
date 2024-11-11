from django.urls import path 
from members import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/details/<int:id>/', views.details, name='details'),
    path('members/',views.members, name='members')
   
   
]





