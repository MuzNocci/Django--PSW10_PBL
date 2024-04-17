from django.urls import path
from paciente import views



urlpatterns = [

    path('home/', views.home, name="home"),

]