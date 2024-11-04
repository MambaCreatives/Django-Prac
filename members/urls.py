from django.urls import path # type: ignore
from members import views

urlpatterns = [
    path('', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
]



