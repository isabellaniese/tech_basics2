from datetime import date
import os

os.system("clear")

#user_day = int(input ("Which day were you born?"))
#user_month = int(input ("Which month?"))
#user_year = int(input ("In which year?"))

dob = input("What is your date of birth? Please write in this format: YYYY/MM/DD")

print(type(user_day))
print(type(user_month))
print(type(user_year))

#split into day, month and year
year, month, day = dob.split("-")
user_year = (int(year))
user_month = (int(month))
user_day = (int(day))

def calculate_age(year, month, date):

    #which day is today
    today = date.today()
    #what age is the user
    dob = date(user_year, user_month, user_day)

    age = int((today - dob).days / 365.25)

    #age = today.year - birthDate.year
    #((today.month, today.day) <
    #(user_month, user_day))

    return calculate_age

# Driver code
print(calculate_age(date(2001, 11, 28)), "years")

def calculate_horoscope (user_sign, user_month, user_day):

    user_sign = calculate_horoscope(user_month, user_day)

    if (user_month == 1 and user_day < 22) or (user_month == 12 and user_day >= 22):
        user_sign = "capricorn"
    elif (user_month == 2 and user_day < 18) or (user_month == 1 and user_day >= 20):
        user_sign = "aquarius"
    elif (user_month == 3 and user_day < 20) or (user_month == 2 and user_day >= 19):
        user_sign = "pisces"
    elif (user_month == 4 and user_day < 19) or (user_month == 3 and user_day >= 21):
        user_sign = "aries"
    elif (user_month == 5 and user_day < 20) or (user_month == 4 and user_day >= 20):
        user_sign = "taurus"
    elif (user_month == 6 and user_day < 20) or (user_month == 5 and user_day >= 21):
        user_sign = "gemini"
    elif (user_month == 7 and user_day < 22) or (user_month == 6 and user_day >= 21):
        user_sign = "cancer"
    elif (user_month == 8 and user_day < 22) or (user_month == 7 and user_day >= 23):
        user_sign = "leo"
    elif(user_month == 9 and user_day < 22) or (user_month == 8 and user_day >= 23):
        user_sign = "virgo"
    elif (user_month == 10 and user_day < 22) or (user_month == 9 and user_day >= 23):
        user_sign = "libra"
    elif (user_month == 11 and user_day < 21) or (user_month == 10 and user_day >= 23):
        user_sign = "scorpio"
    else (user_month == 12 and user_day < 21) or (user_month == 11 and user_day >= 22):
        user_sign = "sagittarius"

return calculate_horoscope