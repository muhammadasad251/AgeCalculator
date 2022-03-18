from django.urls import path
from ageCalculator.views import *

urlpatterns =[
    path('', index, name='index'),
    path('index', index, name='index'),
    path('rangeCalculator',rangeCalculator, name='rangeCalculator'),
    path('weekDays',weekDays, name='weekDays')
]
