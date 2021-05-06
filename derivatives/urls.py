from django.urls import path
from . import views


urlpatterns = [
    path('analysis2/', views.analysis2, name='analysis2'),
    path('output2/', views.output2, name='output2'),
]