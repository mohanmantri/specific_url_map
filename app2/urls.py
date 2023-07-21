from django.urls import path
from app2.views import *
app_name='mohan'
urlpatterns=[
    path('mohan/',mohan,name='mohan'),
]