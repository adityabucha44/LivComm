from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('create',views.create,name='comm'),
    path('stop',views.stop,name='stop')
]