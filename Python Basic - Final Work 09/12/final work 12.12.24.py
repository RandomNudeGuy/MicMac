# Ex 1:
# Write a for loop that prints the numbers from 12 to 24.
#
# if __name__ == '__main__':
#     for i in range(12, 25):
#         print(i)
#---------------------------------------------------------------------------------------------
# Ex 2:
# Write a for loop that prints the ODD numbers from 7 to 31
#
# if __name__ == '__main__':
#     for i in range(7, 32):
#         if i % 2 == 1:
#             print(i)
# ------------------------------------------------------------------------------------------------------------------
# Ex 3:
# Write a for loop that prints the EVEN numbers from 10 to -20.
#
# if __name__ == '__main__':
#     for i in range(10, -20, -1):
#         if i % 2 == 0:
#             print(i)
# ---------------------------------------------------------------------------------------
# Ex 4:
# Write a for loop that iterates through all numbers from 1 to 45. Print the
# following:
# ● For each number that multiples of 3 print “Fizz”
# ● For each number that multiples of 5 print “Buzz”
# ● For each number that multiples of 3 and 5 print “FizzBuzz”
#
#
# if __name__ == '__main__':
#     for i in range(1, 46):
#         if i % 3 == 0 and i % 5 == 0:
#             print(str(i) + " " + "FizzBuzz")
#         elif i % 3 == 0:
#             print(str(i) + " " + "Fizz")
#         elif i % 5 == 0:
#             print(str(i) + " " + "Buzz")
# ----------------------------------------------------------------------------------------------------------------------
# Ex 5:
# Write a function that receives an array as a parameter and calculates the sum
# of all the numbers in the given array (don’t use sum() function).
#
# array = [1, 1, "Hello", 2, "Hell"]
#
# def sum_all_num(array):
#     sum = 0
#     for i in array:
#         if type(i) == int:
#             sum = i + sum
#         else:
#             continue
#
#     print(sum)
#
# if __name__ == '__main__':
#     sum_all_num(array)
#
# ------------------------------------------------------------------------------------------------------------
# Ex 6:
# Write a function that receives an array of objects.
# Each object should represent a student with the properties:
# ● id
# ● first name
# ● last name
# ● age
# ● country
# ● city
# In addition, the function should receive a property to change.
# 1 - The function should check for each property in each object in the array if
# the given property exists and if it does, the function should delete it from the
# object.
# 2 - Write a function that prints each property of each object in the given array.
# 3 - Write a function that sorts the array by the students age from the oldest to
# the youngest and return the sorted array.
#
# students_list = [{"id":1,
#           "first name":"Jonathan",
#           "last name":"Tzur",
#           "age":22,
#           "country":"Israel",
#           "city":"Massad"},
#
#          {"id": 2,
#           "first name": "Michael",
#           "last name": "Shufani",
#           "age": 24,
#           "country": "Israel",
#           "city": "Eilabun"}
#
#          ]
#
# 1 - The function should check for each property in each object in the array if
# the given property exists and if it does, the function should delete it from the
# object.
#
# def delete_property(students_list, property):
#     for student in students_list:
#         if property in student:
#             student.pop(property)
#         else:
#             continue
#
# 2 - Write a function that prints each property of each object in the given array.
#
# def print_property(students_list, property):
#     student_counter = 1
#     for student in students_list:
#         print(f"Student {student_counter} Property: {student[property]}")
#         student_counter += 1
#
#
# 3 - Write a function that sorts the array by the students age from the oldest to
# the youngest and return the sorted array.
#
# def students_age_sort(students_list):
#     sorted_students_age = []
#     sorted_students = []
#     for student in students_list:
#         sorted_students_age.append(student["age"])
#     sorted_students_age.sort(reverse=True)
#     for age in sorted_students_age:
#         for student in students_list:
#             if student["age"] == age:
#                 sorted_students.append(student)
#     return sorted_students
#
#
#
# if __name__ == '__main__':
#     delete_property(students_list, "id")
#     print_property(students_list, "first name")
#     print(students_age_sort(students_list))
# ------------------------------------------------------------------------------------------------------------
# Ex 7:
# 1 - Write a function that receives the array shown above and prints only
# animalType: cat.
# 2 - Write a function that receives the array shown above and the animal type.
# The function should print all names of that animal type if this type exists in the
# object.
# 3 - Write a function that that receives the array shown above and animal name
# The function should add the specified animal name to each ‘names’ array in
# each animal_type if that name does not exist in the ‘names’ array.
#
# our_pets = [
#         {"animal_type": "cat",
#         "names": ["Meowzer", "Fluffy", "Kit-Cat"]
#         },
#
#         {"animal_type": "dog",
#         "names": ["Spot", "Bowser", "Frankie"]
#         }
# ]
#
# 1 - Write a function that receives the array shown above and prints only
# animalType: cat.
#
# def pet_type(pets_list):
#     for pet in pets_list:
#         if pet["animal_type"] == "cat":
#             print("animalType: cat")
#
# 2 - Write a function that receives the array shown above and the animal type.
# The function should print all names of that animal type if this type exists in the
# object.
#
# def pet_names(pets, type):
#     for pet in pets:
#         if pet["animal_type"] == type:
#             pet_names = pet["names"]
#             print(f"Names of the {pet["animal_type"]}: {pet_names}")
#             return
#         else:
#             continue
#     print("This type of animal is not on our list!")
#
# 3 - Write a function that that receives the array shown above and animal name
# The function should add the specified animal name to each ‘names’ array in
# each animal_type if that name does not exist in the ‘names’ array.
#
# def add_names(pets, name):
#     for pet in pets:
#         if name not in pet["names"]:
#             pet["names"].append(name)
#             print(pet["names"]) # for checking the list
#         else:
#             continue
#
#
#
#
#
#
# if __name__ == '__main__':
#     pet_type(our_pets)
#     pet_names(our_pets, "snail")
#     add_names(our_pets,"Garry")
# --------------------------------------------------------------------------------------------------------
# Ex 8:
# 1 - Write a function that prints all the student data (each student property
# should be printed in a new line).
# 2 - Write a function that receives the student object and a hobby, the function
# should add the hobby to the student's hobbies array if it’s not exist already.
# 3 - Use the function that you wrote in ex 1 to print the data of the student and
# check that the new hobby has been added.
# 4 - Write a function that receives an object of a student and hobby, the
# function should delete the hobby from the student's hobbies.
# 5 - Use the function that you wrote in ex 1 to print the data student and check
# that the hobby has been deleted from the object student.
# 6 - Add to the object student new property: family_name and add a value.
#
# student = {
# 'name': 'John',
# 'age': 20,
# 'hobbies': ['reading', 'games', 'coding'],
# }
#
# #
# # 1 - Write a function that prints all the student data (each student property
# # should be printed in a new line).
# #
# def student_data(student):
#     for key in student:
#         print(key + ": " + str(student[key]))
# #
# # 2 - Write a function that receives the student object and a hobby, the function
# # should add the hobby to the student's hobbies array if it’s not exist already.
# #
# def add_hobby(student, hobby):
#     if hobby not in student['hobbies']:
#         student['hobbies'].append(hobby)
#         print(f"Hobby {hobby} has been added!")
#         student_data(student) ## 3 - Use the function that you wrote in ex 1 to print the data of the student and check that the new hobby has been added.
#     else:
#         print(f"Hobby {hobby} already in!")
#         student_data(student)
#
# #
# # 4 - Write a function that receives an object of a student and hobby, the
# # function should delete the hobby from the student's hobbies.
# #
# def del_hobby(student, hobby):
#     if hobby in student['hobbies']:
#         student['hobbies'].remove(hobby)
#         print(f"Hobby {hobby} has been deleted!")
#         student_data(student) # 5 - Use the function that you wrote in ex 1 to print the data student and check that the hobby has been deleted from the object student.
#     else:
#         print(f"Hobby {hobby} is not in!")
#         student_data(student)
#
# if __name__ == '__main__':
#     add_hobby(student, "singing")
#     del_hobby(student, "singing")
#     student["last_name"] = "Brown" # 6 - Add to the object student new property: family_name and add a value
#     student_data(student)
#
# -------------------------------------------------------------------------------------------------------------------------------
# Ex 9:
# Write a function that prints all the elements of a 2D array using nested for
# loops.
# print_matrix(matrix) → Should print: 1 2 3 4 5 6
#
# matrix = [
# [1, 2],
# [3, 4],
# [5, 6]
# ]
#
# def print_matrix(matrix):
#     temp_list = []
#     for i in matrix:
#         for x in i:
#             temp_list.append(x)
#     print(*temp_list)
#
# if __name__ == '__main__':
#     print_matrix(matrix)
#
# ------------------------------------------------------------------------------------------------------------
# Ex 10:
# Write a function to count how many numbers of zeros appear in a 2D matrix
# using nested for loops and increment operation.
# print(zero_count(matrix)) → Should print: 5
# matrix =[
# [0,1,1],
# [0,1,0],
# [1,0,0]
# ]
#
# def zero_count(matrix):
#     counter = 0
#     for i in matrix:
#         for x in i:
#             if x == 0:
#                 counter += 1
#             else:
#                 continue
#     return counter
#
#
#
# if __name__ == '__main__':
#     print(zero_count(matrix))
# ----------------------------------------------------------------------------------------
# Ex 11:
# Write a function to return an array of all the elements that are repeated more
# than once in a given array.
# print(find_dup(arr)) Should print: [4, 1]
# arr = [4,2,34,4,1,12,1,4]
#
#
# def find_dup(array):
#     dupes_list = []
#     for number in array:
#         dupe = array.count(number)
#         if dupe > 1 and number not in dupes_list:
#             dupes_list.append(number)
#     return dupes_list
#
# if __name__ == '__main__':
#     print(find_dup(arr))
# ---------------------------------------------------------------------------------------
# Ex 12:
# Write a function using a for loop that gets an array and returns a new array
# with the elements from the given array appearing in reverse order. (Don’t use
# array reverse() method)
# For example:
# arr = [43, "what", 9, true, "cannot", false, "be", 3, true];
# Function output should be:
# [ture, 3, “be”, false, “cannot”, true, 9, “what”, 43]
#
#
# arr = [43, "what", 9, True, "cannot", False, "be", 3, True]
#
# def reverse_array(array):
#     revered_list = []
#     for i in range(len(array), 0, -1):
#         i = i -1
#         revered_list.append(array[i])
#     return revered_list
#
#
# if __name__ == '__main__':
#     print(reverse_array(arr))
# -------------------------------------------------------------------------
# Ex 13:
# Given two arrays of integers. Add up each element in the same position and
# create a new array containing the sum of each pair.
# Assume both arrays are of the same length.
# For example:
# first_array = [4, 6, 7];
# second_array = [8, 1, 9];
# Function output should be:
# [12, 7, 16]

