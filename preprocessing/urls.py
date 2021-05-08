from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('preprocessing/', views.preprocessing, name='preprocessing'),
    path('results/', views.results, name='results'),
]