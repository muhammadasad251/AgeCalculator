from django.urls import path
from ageCalculator.views import *

urlpatterns =[
    path('', index, name='index'),
]
