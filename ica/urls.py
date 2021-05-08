from django.urls import path
from . import views


urlpatterns = [
    path('', views.ica, name='ica'),
    path('results/', views.results, name='results'),
]