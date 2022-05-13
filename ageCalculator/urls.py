from django.urls import path
from ageCalculator.views import *

urlpatterns =[
    path('', index, name='index'),
    path('index', index, name='index'),
    path('rangeCalculator',rangeCalculator, name='rangeCalculator'),
    path('weekDays',weekDays, name='weekDays'),
    path('workDays',workDays, name='workDays'),
    path('calculateWages',calculateWages, name='calculateWages'),
    path('appointment',appointment, name='appointment'),
]
