from django.urls import path
from app2.views import *
app_name='possible'
urlpatterns=[
    path('possible/',possible,name='possible'),
]