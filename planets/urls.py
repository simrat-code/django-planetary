from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:planet_id>', views.planets_detail, name="planets_detail"),
]