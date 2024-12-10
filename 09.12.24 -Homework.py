# Exercise 1:
# 1. Write a function that returns the current date in local time.
# 2. Write a function that gets local date time as a parameter and return it in UTC
# timezone.
# from datetime import datetime
# import pytz
#
# def current_date():
#     date = datetime.now()
#     date_convert = date.date()
#     return date_convert
#
# def utc_time(timezone, datetime):
#     local_timezone = pytz.timezone(timezone)
#
#     local_datetime = local_timezone.localize(datetime)
#
#     utc_datetime = local_datetime.astimezone(pytz.utc)
#
#     utc_formatted = utc_datetime.strftime('%Y-%m-%d %H:%M:%S')
#
#     return  utc_formatted
#
# if __name__ == '__main__':
#     print(current_date())
#     # print(utc_time(datetime.datetime.now()))
#     local_dt = datetime.now()
#
#     local_tz = 'Asia/Jerusalem'
#     utc_dt = utc_time(local_tz, local_dt)
#     print("UTC datetime:", utc_dt)
# --------------------------------------
#Exercise 2:
# Write a program that gets the current date and returns an array with the next 5 days
# starting from today.
# from datetime import datetime, timedelta  # couldve used the .replace method for replacing the day at the i but than it wont care about how many days in month
# def five_days(date):
#     next_5_days = []
#     for i in range(5):
#         next_day = (date + timedelta(days=i)).strftime('%Y-%m-%d')
#         next_5_days.append(next_day)
#     return next_5_days
#
#
# if __name__ == '__main__':
#     date = (datetime.now() + timedelta(days=1)) #added 1 more day to not count today
#     print(five_days(date))
#
#---------------------------------------
# Exercise 3:
# Write a function that get a date object and display this date in ‘mm/dd/yyyy’ format:
# import datetime
#
# def date_format(date):
#     return date.strftime('%m/%d/%Y')
#
#
# if __name__ == '__main__':
#     date = datetime.datetime.now()
#     print(date_format(date))
# -------------------------------------
# Exercise 4:
# Write a function that gets an array of strings as parameter, your function should
# generate a random number between the range of the array index and return the
# element which positions in the number that was randomly generated.
# import random
#
# array = ["zero", "one", "two", "three"]
#
# def element_from_random(array):
#     length = len(array) - 1
#     random_num = random.randint(0, length)
#     return array[random_num]
#
# if __name__ == '__main__':
#     print(element_from_random(array))
#
# ---------------------------------------
# Exercise 5:
# Write a function that gets a string as a parameter and print it in reverse (don’t use
# reverse Python functions but implement your own).
#
# def reverse(string):
#     reversed = string[::-1]
#     return  reversed
#
# if __name__ == '__main__':
#     string = "hello"
#     print(reverse(string))
#
# ---------------------------------------
# Exercise 6:
# Write a function that gets two different strings as parameters and returns True if one
# of them is a substring of the other and otherwise the function will return False.
# For example: for strings “Hello” , “Hel” → should return True
# for strings “Hello”, “Ola” → should return False
#
#
# def str_in_str(str1, str2):
#     if str2 in str1:
#         return True
#     else:
#         return False
#
# if __name__ == '__main__':
#     first_str = "Hello"
#     second_str = "Hell"
#     print(str_in_str(first_str, second_str))
# ------------------------------------
# Exercise 7:
# Write a function to convert a given string to all uppercase if it contains at least 2
# uppercase characters in the first 4 characters.
#
#
# def convertion_upper(str):
#     new_str = str[:4]
#     for i in new_str:
#         for x in new_str:
#             if (x != i) and (x.isupper() == True and i.isupper() == True):
#                 return True
#             else:
#                 continue
#         return False
#
# if __name__ == '__main__':
#     str = "Hello"
#     print(convertion_upper(str))
# -------------------------------
# Exercise 8:
# Write a function that gets an email string as a parameter and validates that the string
# that was provided is indeed an email. A valid email is an email that contains ‘@’ in it
# and is above 5 chars.
#
# def email_check(str):
#     if "@" in str and len(str) > 5:
#         return "Email is valid"
#     else:
#         return "Email not Valid"
#
#
# if __name__ == '__main__':
#     email = "hello@gmail.com"
#     print(email_check(email))
#

