from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('analysis1/', views.analysis1, name='analysis1'),
    path('output1/', views.output1, name='output1'),
    path('analysis2/', views.analysis2, name='analysis2'),
    path('output2/', views.output2, name='output2'),

]