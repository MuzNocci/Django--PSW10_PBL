from django.urls import path
from medico import views



urlpatterns = [

    path('cadastro_medico/', views.cadastro_medico, name="cadastro_medico"),

]