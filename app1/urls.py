from django.urls import path
from app1.views import *
app_name='impossible'
urlpatterns=[
    path('impossible/',impossible,name='impossible'),
]