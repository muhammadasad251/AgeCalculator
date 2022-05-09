from django.shortcuts import render
from datetime import date, datetime
import numpy as np

# Create your views here.


def index(request):
    context = {}
    if request.method == "POST":
        date_of_birth_user_input = request.POST['date']

        def ageCalculator(date_of_birth):
            # getting the birth date from user input
            birth_date_with_time = date_of_birth
            birth_date = datetime.strptime(birth_date_with_time, '%Y-%m-%d')
            birth_month = birth_date.month
            birth_day = birth_date.day

            # getting the current date
            today = date.today()
            current_month = today.month
            current_day = today.day

            # calculating the month difference
            if birth_month > current_month:
                month_diff = birth_month - current_month
            else:
                month_diff = current_month - birth_month

            # calculating the day difference
            if birth_day > current_day:
                day_diff = birth_day - current_day
            else:
                day_diff = current_day - birth_day

            # calculating year difference
            year_diff = today.year - birth_date.year

            # printing the results on console for testing
            print("Year: " + str(year_diff))
            print(type(year_diff))
            print("Month: " + str(month_diff))
            print(type(month_diff))
            print("Day: " + str(day_diff))
            print(type(day_diff))

            # printing the message and remark based on the age
            age_string = ""
            if year_diff == 0 and month_diff == 0 and day_diff >= 1:
                print("C1")
                age_string = "You are only " + str(day_diff) + " days old!"
            elif year_diff == 0 and month_diff >= 1 and day_diff == 0:
                print("Ca")
                age_string = "You are exactly " + \
                    str(month_diff) + " month(s) old!"
            elif year_diff == 0 and month_diff >= 1:
                print("C3")
                age_string = "You are only " + \
                    str(month_diff) + " months and " + \
                    str(day_diff) + " days old!"
            elif year_diff >= 1 and month_diff == 0 and day_diff == 0:
                print("C4")
                age_string = "You are exactly " + \
                    str(year_diff) + " year(s) old!"
            elif year_diff >= 1 and month_diff >= 1 and day_diff == 0:
                print("C4")
                age_string = "You are exactly " + \
                    str(year_diff) + " year(s) old and " + \
                    str(month_diff) + " month(s) old!"
            elif year_diff >= 1 and month_diff >= 1 and day_diff == 0:
                print("C5")
                age_string = "You are exactly " + \
                    str(year_diff) + " years and " + \
                    str(month_diff) + " months old!"
            else:
                print("C6")
                age_string = "You are " + \
                    str(year_diff) + " years and " + \
                    str(month_diff) + " months and " + \
                    str(day_diff) + " days old!"

            remark = ""
            if year_diff == 0 and month_diff == 0 and day_diff < 30:
                remark = "You are just a new-born baby!"
            elif (year_diff < 0 and month_diff >= 1):
                remark = "You are a toddler!"
            elif (year_diff >= 0 and month_diff >= 1) and (year_diff <= 5):
                remark = "You are a toddler!"
            elif year_diff > 0 and year_diff <= 12:
                remark = "You are a kid!"
            elif year_diff >= 13 and year_diff <= 19:
                remark = "You are a teenager!"
            elif year_diff >= 20 and year_diff <= 35:
                remark = "You are a young adult!"
            elif year_diff >= 36 and year_diff <= 65:
                remark = "You are an adult!"
            elif year_diff >= 66:
                remark = "You are an elder!"

            # returning the age difference message to the frontend
            return remark + " " + age_string

        age_message = (ageCalculator(date_of_birth_user_input))
        context = {
            "age": age_message
        }
    return render(request, 'index.html', context)


def rangeCalculator(request):
    context = {}
    if request.method == "POST":
        date_of_birth = request.POST['sdate']
        edate = request.POST['edate']

        def Calc(date_of_birth, edate):
            born_date = date_of_birth
            born = datetime.strptime(born_date, '%Y-%m-%d')
            today = edate
            today = datetime.strptime(today, '%Y-%m-%d')
            curr_month = today.month
            born_month = born.month
            curr_day = today.day
            born_day = born.day
            if born_month > curr_month:
                month_diff = born_month - curr_month
            else:
                month_diff = curr_month - born_month
            if born_day > curr_day:
                day_diff = born_day - curr_day
            else:
                day_diff = curr_day - born_day
            age = today.year - born.year
            print(str(age))
            print(month_diff)
            print(str(day_diff))
            return " Your Age  : " + str(age) + "  Years   " + str(month_diff) + "  Months  and " + str(day_diff) + "  Days"
        age = (Calc(date_of_birth, edate))
        context = {
            "age": age
        }
        working_days = np.busday_count('2022-03-01', '2022-03-18')
        print(working_days)
    return render(request, 'rangeCalculator.html', context)


def weekDays(request):
    context = {}
    if request.method == "POST":
        date_of_birth = request.POST['sdate']
        edate = request.POST['edate']

        def Calc(date_of_birth, edate):
            born_date = date_of_birth
            born = datetime.strptime(born_date, '%Y-%m-%d')
            today = edate
            today = datetime.strptime(today, '%Y-%m-%d')
            days = working_days = np.busday_count(date_of_birth, edate)
            return "Week days are  : " + str(days) + "  Days"
        age = (Calc(date_of_birth, edate))
        context = {
            "age": age
        }
    return render(request, 'weekDays.html', context)


def workDays(request):
    context = {}
    if request.method == "POST":
        sdate = request.POST['sdate']
        edate = request.POST['edate']
        date_start_val = sdate
        date_end_val = edate  # end date (inclusive)

        date_start = datetime.strptime(date_start_val, '%Y-%m-%d').date()
        date_end = datetime.strptime(date_end_val, '%Y-%m-%d').date()

        days = {'mon': 0, 'tue': 1, 'wed': 2,
                'thu': 3, 'fri': 4, 'sat': 5, 'sun': 6}

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
            weekday_count = weekday_count/7 + (weekday_count % 7 and 1 or 0)
        else:
            weekday_count = 0

        day_count = total_days - weekday_count
        print(day_count)
        age = int(day_count)
        context = {
            "age": age
        }
    return render(request, 'workDays.html', context)


def calculateWages(request):
    context = {}
    if request.method == "POST":
        date_of_birth = request.POST['sdate']
        edate = request.POST['edate']
        rate = float(request.POST['rate'])
        hoursPerDay = float(request.POST['hoursPerDay'])

        def Calc(date_of_birth, edate):
            born_date = date_of_birth
            born = datetime.strptime(born_date, '%Y-%m-%d')
            today = edate
            today = datetime.strptime(today, '%Y-%m-%d')
            curr_month = today.month
            born_month = born.month
            curr_day = today.day
            born_day = born.day
            if born_month > curr_month:
                month_diff = born_month - curr_month
            else:
                month_diff = curr_month - born_month
            if born_day > curr_day:
                day_diff = born_day - curr_day
            else:
                day_diff = curr_day - born_day
            age = today.year - born.year
            print(str(age))
            print(month_diff)
            print(str(day_diff))
            # return " Your Age  : " + str(age) +"  Years   " + str(month_diff) +  "  Months  and " + str(day_diff) + "  Days"

            years = float(str(age))
            int(years)
            months = float(str(month_diff))
            int(months)
            days = float(str(day_diff))
            int(days)
            if(years > 0):
                ydays = 365*years
            else:
                ydays = 0
            if(months > 0):
                mdays = 30*months
            else:
                mdays = 0
            age = ydays+mdays+days
            hours = rate*(hoursPerDay*age)
            return hours
        age = (Calc(date_of_birth, edate))
        context = {
            "age": age
        }
        working_days = np.busday_count('2022-03-01', '2022-03-18')
        print(working_days)
    return render(request, 'calculateWages.html', context)
