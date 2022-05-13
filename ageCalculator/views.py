from django.shortcuts import render
from datetime import date, datetime
import numpy as np
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this

# Create your views here.
#Calculate age from birthday
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


#Calculating the Range
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
            #Getting umber of months and days from given number of range. Same like wage calcyion function
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
            return " Range is  : " + str(age) +"  Years   " + str(month_diff) +  "  Months  and " + str(day_diff) + "  Days"
        age=(Calc(date_of_birth,edate))
        context = {
            "age":age
        }
        working_days=np.busday_count('2022-03-01', '2022-03-18')
        print(working_days)
    return render(request, 'rangeCalculator.html',context)
#Calculating Weekdays
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
            #Numpy function is used to get week days from given number of ragge
            days=working_days=np.busday_count(date_of_birth, edate)
            return "Week days are  : " +str(days) + "  Days"
        age=(Calc(date_of_birth,edate))
        context = {
            "age":age
        }
    return render(request, 'weekDays.html',context)

#Calculating workdays by skipping specific days like here we are skipping tuesday.
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
        #Tuesday is off
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
#Calculating wages by given numbers of hours and pa rate.
def calculateWages(request):
    context={}
    if request.method =="POST":
        date_of_birth = request.POST['sdate']
        edate = request.POST['edate']
        rate = float(request.POST['rate'])
        hoursPerDay = float(request.POST['hoursPerDay'])
        def Calc(date_of_birth,edate):
            born_date = date_of_birth
            born = datetime.strptime(born_date, '%Y-%m-%d')
            today = edate
            today=datetime.strptime(today, '%Y-%m-%d')
            curr_month = today.month
            born_month = born.month
            curr_day   = today.day
            born_day   = born.day
            #Calculating Months and Days from Given range
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
            #return " Your Age  : " + str(age) +"  Years   " + str(month_diff) +  "  Months  and " + str(day_diff) + "  Days"
            
            #Getting number of years, Months and days
            years=float(str(age))
            int(years)
            months=float(str(month_diff))
            int(months)
            days=float(str(day_diff))
            int(days)
            if(years>0):
                ydays=365*years
            else:
                ydays=0
            if(months>0):
                mdays=30*months
            else:
                mdays=0
            age=ydays+mdays+days
            hours=rate*(hoursPerDay*age)
            return hours
        age=(Calc(date_of_birth,edate))
        context = {
            "age":'Your wage is : '+str(age)
        }
        working_days=np.busday_count('2022-03-01', '2022-03-18')
        print(working_days)
    return render(request, 'calculateWages.html',context)

