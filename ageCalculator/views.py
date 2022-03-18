from django.shortcuts import render
from datetime import date, datetime
import numpy as np

# Create your views here.
def index(request):
    context={}
    if request.method =="POST":
        date_of_birth = request.POST['date']
        def Calc(date_of_birth):
            born_date = date_of_birth
            born = datetime.strptime(born_date, '%Y-%m-%d')
            today = date.today()
            curr_month = today.month
            born_month = born.month
            curr_day   = today.day
            born_day   = born.day
            if born_month > curr_month:
                month_diff = born_month - curr_month
            else :
                month_diff = curr_month - born_month
            if born_day > curr_day:
                day_diff = born_day - curr_day
            else :
                day_diff = curr_day - born_day 
            age = today.year - born.year
            print(str(age))
            print(month_diff)
            print(str(day_diff))
            return " Your Age  : " + str(age) +"  Years   " + str(month_diff) +  "  Months  and " + str(day_diff) + "  Days"
        age=(Calc(date_of_birth))
        context = {
            "age":age
        }
    return render(request, 'index.html',context)



def rangeCalculator(request):
    context={}
    if request.method =="POST":
        date_of_birth = request.POST['sdate']
        edate = request.POST['edate']
        def Calc(date_of_birth,edate):
            born_date = date_of_birth
            born = datetime.strptime(born_date, '%Y-%m-%d')
            today = edate
            today=datetime.strptime(today, '%Y-%m-%d')
            curr_month = today.month
            born_month = born.month
            curr_day   = today.day
            born_day   = born.day
            if born_month > curr_month:
                month_diff = born_month - curr_month
            else :
                month_diff = curr_month - born_month
            if born_day > curr_day:
                day_diff = born_day - curr_day
            else :
                day_diff = curr_day - born_day 
            age = today.year - born.year
            print(str(age))
            print(month_diff)
            print(str(day_diff))
            return " Your Age  : " + str(age) +"  Years   " + str(month_diff) +  "  Months  and " + str(day_diff) + "  Days"
        age=(Calc(date_of_birth,edate))
        context = {
            "age":age
        }
        working_days=np.busday_count('2022-03-01', '2022-03-18')
        print(working_days)
    return render(request, 'rangeCalculator.html',context)

def weekDays(request):
    context={}
    if request.method =="POST":
        date_of_birth = request.POST['sdate']
        edate = request.POST['edate']
        def Calc(date_of_birth,edate):
            born_date = date_of_birth
            born = datetime.strptime(born_date, '%Y-%m-%d')
            today = edate
            today=datetime.strptime(today, '%Y-%m-%d')
            days=working_days=np.busday_count(date_of_birth, edate)
            return " Your Working days are  : " +str(days) + "  Days"
        age=(Calc(date_of_birth,edate))
        context = {
            "age":age
        }
    return render(request, 'weekDays.html',context)