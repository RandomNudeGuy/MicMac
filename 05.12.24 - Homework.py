# Ex1:
# Write a function `print_numbers()` that prints all numbers between 1 to 10 using a for
# loop.
#
#
# def print_numbers():
#     for i in range(1, 11):
#         print(i)
#
# if __name__ == '__main__':
#     print_numbers()
#-------------------------
# Ex2:
# Write a function `delete_element()` that deletes all the occurrences of the given
# element from the given array.
# for example: arr = [23,56,4,78,5,63,45,210,56] and number 4
# if the given number appears in the array your function should delete it
#
# arr = [23,56,4,78,5,63,45,210,56]
#
# def delete_element(array, number):
#     for i in array:
#         if number == i:
#             array.remove(i)
#         else:
#             continue
#
#
# if __name__ == '__main__':
#     delete_element(arr, 23)
#     print(arr)
# -----------------------------
# Ex3:
# Write a function that receives an array of integers and returns how many numbers
# are odd and how many are even.
# Return a dictionary that contains this data as key-value.
#
# dict = {
#     "even": 0,
#     "odd": 0
# }
#
# array = [10, 22, 53, 72, 81, 2, 98]
#
# def odd_even(array):
#     for i in array:
#         if i % 2 == 0:
#             dict["even"] += 1
#             continue
#         elif i % 2 == 1:
#             dict["odd"] += 1
#             continue
#
# if __name__ == '__main__':
#     odd_even(array)
#     print("Number of even: " + str(dict["even"]) + "\n" + "Number of odds: " + str(dict["odd"]))
# ---------------------------------
# Ex4:
# Write a function called find_dup() that returns all the elements that are repeated
# more than once in a given array.
# Return the result as a dictionary (the key should be the repeated element, the value
# should be the amount of times this element repeated).
# If an element appears only once it should not be added to the result dictionary.
#
# array = [22, 22, 22, 53, 53, 72, 81, 2, 98]
#
# dupes = {}
#
# def find_dup(array):
#     temp_array = []
#     for i in array:
#         if i not in temp_array:
#             temp_array.append(i)
#         else:
#             dupe_array = []
#             for x in array:
#                 if x == i:
#                     dupe_array.append(x)
#                 else:
#                     continue
#             dupes[i] = len(dupe_array)
#
#
# if __name__ == '__main__':
#     find_dup(array)
#     print(dupes)
# -------------------------------------
# Ex5:
# Construct for loops that accomplish the following tasks:
# 1. Print the numbers 1 - 20, one number per line.
# 2. Print only the ODD values from 3 - 29, one number per line.
# 3. Print the EVEN numbers between 1 - 20 in a descending order, one number
# per line.
# 4. Print the numbers 50 down to 20 in descending order, but only if the numbers
# are multiples of 3.
#
# def num_1to20():
#     for i in range(1, 21):
#         print(i)
#
# def odd_3to29():
#     for i in range(3, 30):
#         if i % 2 == 1:
#             print(i)
#         else:
#             continue
#
# def even_1to20():
#     for i in range(21, 1, -1):
#         if i % 2 == 0:
#             print(i)
#
#
#
# def multiplier_of3():
#     for i in range(50, 19, -1):
#         if i % 3 == 0:
#             print(i)
#
#
#
#
# if __name__ == '__main__':
#     num_1to20()
#     print("-------------")
#     odd_3to29()
#     print("-------------")
#     even_1to20()
#     print("-------------")
#     multiplier_of3()
# -------------------------------------
# Ex7:
# Write a function that prints “Hello” 10 times using a while loop.
#
# def hello_10():
#     counter = 0
#     while counter < 10:
#         print("Hello")
#         counter += 1
#
# if __name__ == '__main__':
#     hello_10()
# --------------------------------
# Ex8:
# Write a function that receives an array of numbers and a number.
# Write Python code that calculates the sum of the array.
# As long as the sum of the array is lower than the number given, the loop will print
# “The number is still lower than array sum” and increment the given number by one.
# Once the while loop finish your code should print “The while loop has over”

array = [1, 1, 1]
sum = 0# Ex1:
# Write a function `print_numbers()` that prints all numbers between 1 to 10 using a for
# loop.
#
#
# def print_numbers():
#     for i in range(1, 11):
#         print(i)
#
# if __name__ == '__main__':
#     print_numbers()
#-------------------------
# Ex2:
# Write a function `delete_element()` that deletes all the occurrences of the given
# element from the given array.
# for example: arr = [23,56,4,78,5,63,45,210,56] and number 4
# if the given number appears in the array your function should delete it
#
# arr = [23,56,4,78,5,63,45,210,56]
#
# def delete_element(array, number):
#     for i in array:
#         if number == i:
#             array.remove(i)
#         else:
#             continue
#
#
# if __name__ == '__main__':
#     delete_element(arr, 23)
#     print(arr)
# -----------------------------
# Ex3:
# Write a function that receives an array of integers and returns how many numbers
# are odd and how many are even.
# Return a dictionary that contains this data as key-value.
#
# dict = {
#     "even": 0,
#     "odd": 0
# }
#
# array = [10, 22, 53, 72, 81, 2, 98]
#
# def odd_even(array):
#     for i in array:
#         if i % 2 == 0:
#             dict["even"] += 1
#             continue
#         elif i % 2 == 1:
#             dict["odd"] += 1
#             continue
#
# if __name__ == '__main__':
#     odd_even(array)
#     print("Number of even: " + str(dict["even"]) + "\n" + "Number of odds: " + str(dict["odd"]))
# ---------------------------------
# Ex4:
# Write a function called find_dup() that returns all the elements that are repeated
# more than once in a given array.
# Return the result as a dictionary (the key should be the repeated element, the value
# should be the amount of times this element repeated).
# If an element appears only once it should not be added to the result dictionary.
#
# array = [22, 22, 22, 53, 53, 72, 81, 2, 98]
#
# dupes = {}
#
# def find_dup(array):
#     temp_array = []
#     for i in array:
#         if i not in temp_array:
#             temp_array.append(i)
#         else:
#             dupe_array = []
#             for x in array:
#                 if x == i:
#                     dupe_array.append(x)
#                 else:
#                     continue
#             dupes[i] = len(dupe_array)
#
#
# if __name__ == '__main__':
#     find_dup(array)
#     print(dupes)
# -------------------------------------
# Ex5:
# Construct for loops that accomplish the following tasks:
# 1. Print the numbers 1 - 20, one number per line.
# 2. Print only the ODD values from 3 - 29, one number per line.
# 3. Print the EVEN numbers between 1 - 20 in a descending order, one number
# per line.
# 4. Print the numbers 50 down to 20 in descending order, but only if the numbers
# are multiples of 3.
#
# def num_1to20():
#     for i in range(1, 21):
#         print(i)
#
# def odd_3to29():
#     for i in range(3, 30):
#         if i % 2 == 1:
#             print(i)
#         else:
#             continue
#
# def even_1to20():
#     for i in range(21, 1, -1):
#         if i % 2 == 0:
#             print(i)
#
#
#
# def multiplier_of3():
#     for i in range(50, 19, -1):
#         if i % 3 == 0:
#             print(i)
#
#
#
#
# if __name__ == '__main__':
#     num_1to20()
#     print("-------------")
#     odd_3to29()
#     print("-------------")
#     even_1to20()
#     print("-------------")
#     multiplier_of3()
# -------------------------------------
# Ex7:
# Write a function that prints “Hello” 10 times using a while loop.
#
# def hello_10():
#     counter = 0
#     while counter < 10:
#         print("Hello")
#         counter += 1
#
# if __name__ == '__main__':
#     hello_10()
# --------------------------------
# Ex8:
# Write a function that receives an array of numbers and a number.
# Write Python code that calculates the sum of the array.
# As long as the sum of the array is lower than the number given, the loop will print
# “The number is still lower than array sum” and increment the given number by one.
# Once the while loop finish your code should print “The while loop has over”
#
# array = [1, 1, 1]
#
#
# def array_lowerthan_num(array, num):
#     sum = 0
#     for i in array:
#         sum = sum + i
#
#     while sum > num:
#         print("The number is still lower than array sum")
#         num = num + 1
#     print("The while loop is over")
#
# array_lowerthan_num(array, 1)
#-------------------------------
# Ex9:
# Write a function that receives an array of Boolean type.
# As long as the value is true, the loop should continue, if the value is false, then return
# the first index of the false value.

array = [True, True , False]

def array_true(array):
    while array[0]  == True:
        a

array_true(array)