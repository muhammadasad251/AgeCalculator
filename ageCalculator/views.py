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
            return "Week days are  : " +str(days) + "  Days"
        age=(Calc(date_of_birth,edate))
        context = {
            "age":age
        }
    return render(request, 'weekDays.html',context)


def workDays(request):
    context={}
    if request.method =="POST":
        sdate=request.POST['sdate']
        edate=request.POST['edate']
        date_start_val = sdate
        date_end_val = edate  # end date (inclusive)

        date_start = datetime.strptime(date_start_val,'%Y-%m-%d').date()
        date_end = datetime.strptime(date_end_val,'%Y-%m-%d').date()

        days = {'mon':0,'tue':1,'wed':2,'thu':3,'fri':4,'sat':5,'sun':6}

        total_days = (date_end - date_start).days + 1 

        first_weekday = date_start.weekday()
        target_weekday = days['tue']   

        if target_weekday == first_weekday:
            days_before = 0
        elif target_weekday < first_weekday:
            days_before = 7 - first_weekday + target_weekday
        else:
            days_before = target_weekday - first_weekday
        
        weekday_count = total_days - days_before
        if weekday_count > 0:
            weekday_count = weekday_count/7 + (weekday_count%7 and 1 or 0)
        else:
            weekday_count = 0

        day_count = total_days - weekday_count
        print(day_count)
        age=int(day_count)
        context = {
            "age":age
        }
    return render(request, 'workDays.html',context)