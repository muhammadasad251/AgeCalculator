from django.shortcuts import render
from datetime import date, datetime

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