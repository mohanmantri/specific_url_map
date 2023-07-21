from django.urls import path
app_name='haha'
from app1.views import *
urlpatterns=[
    path('mohan/',mohan,name='mohan'),
]