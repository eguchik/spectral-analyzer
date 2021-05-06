from django.urls import path
from . import views


urlpatterns = [

    path('analysis3/', views.analysis3, name='analysis3'),
    path('output3/', views.output3, name='output3'),

]