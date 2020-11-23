from django.urls import path
from . import views

app_name = 'apiReader'

urlpatterns = [
    path('', views.index, name='index'),
]