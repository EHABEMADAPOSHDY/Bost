from django.urls import path
from . import views

urlpatterns = [
    path('',views.post, name='post'),
    path('index',views.index, name='index'),
    
]
