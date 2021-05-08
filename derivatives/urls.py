from django.urls import path
from . import views


urlpatterns = [
    path('', views.derivatives, name='derivatives'),
    path('results/', views.results, name='results'),
]