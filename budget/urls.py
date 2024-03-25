from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', project_list,name='list'),
    path('<slug:project_slug>',project_detail,name='detail'),

]
