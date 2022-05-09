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
                age_string = "You are only " + str(day_diff) + " days old!"
            elif year_diff == 0 and month_diff >= 1 and day_diff == 0:
                age_string = "You are exactly " + \
                    str(month_diff) + " month(s) old!"
            elif year_diff == 0 and month_diff >= 1:
                age_string = "You are only " + \
                    str(month_diff) + " months and " + \
                    str(day_diff) + " days old!"
            elif year_diff >= 1 and month_diff == 0 and day_diff == 0:
                age_string = "You are exactly " + \
                    str(year_diff) + " year(s) old!"
            elif year_diff >= 1 and month_diff >= 1 and day_diff == 0:
                age_string = "You are exactly " + \
                    str(year_diff) + " year(s) old and " + \
                    str(month_diff) + " month(s) old!"
            elif year_diff >= 1 and month_diff >= 1 and day_diff == 0:
                age_string = "You are exactly " + \
                    str(year_diff) + " years and " + \
                    str(month_diff) + " months old!"
            else:
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
        start_date_from_user = request.POST['sdate']
        end_date_from_user = request.POST['edate']

        def CalculateDateRange(start_date, end_date):
            # breaking down the start date
            start_date_without_time = datetime.strptime(start_date, '%Y-%m-%d')
            start_month = start_date_without_time.month
            start_day = start_date_without_time.day

            # breakind down the end date
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            current_month = end_date.month
            current_day = end_date.day

            if start_month > current_month:
                month_diff = start_month - current_month
            else:
                month_diff = current_month - start_month
            if start_day > current_day:
                day_diff = start_day - current_day
            else:
                day_diff = current_day - start_day

            year_diff = end_date.year - start_date_without_time.year

            # printing the results on console for testing
            print("Year: " + str(year_diff))
            print(type(year_diff))
            print("Month: " + str(month_diff))
            print(type(month_diff))
            print("Day: " + str(day_diff))
            print(type(day_diff))

            # printing the message and remark based on the age
            range_string = ""
            if year_diff == 0 and month_diff == 0 and day_diff >= 1:
                range_string = "The date range is only " + \
                    str(day_diff) + " days."
            elif year_diff == 0 and month_diff >= 1 and day_diff == 0:
                range_string = "The date range is exactly " + \
                    str(month_diff) + " month(s)."
            elif year_diff == 0 and month_diff >= 1:
                range_string = "The date range is only " + \
                    str(month_diff) + " months and " + \
                    str(day_diff) + " days."
            elif year_diff >= 1 and month_diff == 0 and day_diff == 0:
                range_string = "The date range is exactly " + \
                    str(year_diff) + " year(s)."
            elif year_diff >= 1 and month_diff >= 1 and day_diff == 0:
                range_string = "The date range is exactly " + \
                    str(year_diff) + " year(s) old and " + \
                    str(month_diff) + " month(s)."
            elif year_diff >= 1 and month_diff >= 1 and day_diff == 0:
                range_string = "The date range is exactly " + \
                    str(year_diff) + " years and " + \
                    str(month_diff) + " months."
            else:
                range_string = "The date range is " + \
                    str(year_diff) + " year(s) and " + \
                    str(month_diff) + " month(s) and " + \
                    str(day_diff) + " day(s)."

            return range_string

        range_message = (CalculateDateRange(
            start_date_from_user, end_date_from_user))

        context = {
            "age": range_message
        }

        # working_days = np.busday_count('2022-03-01', '2022-03-18')
        working_days = np.busday_count(
            start_date_from_user, end_date_from_user)
        print("Working days: ", working_days)
    return render(request, 'rangeCalculator.html', context)


def weekDays(request):
    context = {}
    if request.method == "POST":
        start_date = request.POST['sdate']
        end_date = request.POST['edate']

        def CalculateWeekdays(start_date, end_date):
            days = np.busday_count(start_date, end_date)
            return "Total weekdays are " + str(days) + " days"

        total_weekdays = (CalculateWeekdays(start_date, end_date))

        context = {
            "age": total_weekdays
        }
    return render(request, 'weekDays.html', context)


def workDays(request):
    context = {}
    if request.method == "POST":
        date_start_val = request.POST['sdate']
        date_end_val = request.POST['edate']  # end date (inclusive)

        date_start_stripped = datetime.strptime(
            date_start_val, '%Y-%m-%d').date()
        date_end_stripped = datetime.strptime(date_end_val, '%Y-%m-%d').date()

        days = {'mon': 0, 'tue': 1, 'wed': 2,
                'thu': 3, 'fri': 4, 'sat': 5, 'sun': 6}

        total_days = (date_end_stripped - date_start_stripped).days + 1

        first_weekday = date_start_stripped.weekday()
        last_weekday = date_end_stripped.weekday()

        if last_weekday == first_weekday:
            days_before = 0
        elif last_weekday < first_weekday:
            days_before = 7 - first_weekday + last_weekday
        else:
            days_before = last_weekday - first_weekday

        weekday_count = total_days - days_before

        if weekday_count > 0:
            weekday_count = weekday_count/7 + (weekday_count % 7 and 1 or 0)
        else:
            weekday_count = 0

        day_count = total_days - weekday_count
        print(day_count)
        result_string = int(day_count)
        context = {
            "age": result_string
        }
    return render(request, 'workDays.html', context)


def calculateWages(request):
    context = {}
    if request.method == "POST":
        start_date = request.POST['sdate']
        end_date = request.POST['edate']
        rate = float(request.POST['rate'])
        hoursPerDay = float(request.POST['hoursPerDay'])

        def CalculateWages(start_month, end_date):
            start_date = datetime.strptime(start_month, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')

            current_month = end_date.month
            current_day = end_date.day

            start_month = start_date.month
            start_day = start_date.day

            if start_month > current_month:
                month_diff = start_month - current_month
            else:
                month_diff = current_month - start_month
            if start_day > current_day:
                day_diff = start_day - current_day
            else:
                day_diff = current_day - start_day

            year_diff = end_date.year - start_date.year

            # printing the results on console for testing
            print("Year: " + str(year_diff))
            print(type(year_diff))
            print("Month: " + str(month_diff))
            print(type(month_diff))
            print("Day: " + str(day_diff))
            print(type(day_diff))
            # return " Your Age  : " + str(age) +"  Years   " + str(month_diff) +  "  Months  and " + str(day_diff) + "  Days"

            years = float(str(year_diff))
            int(years)
            months = float(str(month_diff))
            int(months)
            days = float(str(day_diff))
            int(days)

            if(years > 0):
                years_to_days = 365*years
            else:
                years_to_days = 0
            if(months > 0):
                months_to_days = 30*months
            else:
                months_to_days = 0

            year_diff = years_to_days+months_to_days+days

            total_wage_string = "You have worked " + str(hoursPerDay) + " hours per day " + str(
                year_diff) + " days @" + str(rate) + "per/hour totalling and " + str(rate*(hoursPerDay*year_diff))
            return total_wage_string

        total_wage_result = (CalculateWages(start_date, end_date))

        context = {
            "age": total_wage_result
        }

        # working_days = np.busday_count('2022-03-01', '2022-03-18')
        # print(working_days)
    return render(request, 'calculateWages.html', context)
