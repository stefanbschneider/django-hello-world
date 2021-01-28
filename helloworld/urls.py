from django.urls import path

from . import views


app_name = 'helloworld'

urlpatterns = [
    path('', views.index, name='index'),
]
