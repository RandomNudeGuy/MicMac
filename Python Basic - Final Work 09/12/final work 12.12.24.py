# Ex 1:
# Write a for loop that prints the numbers from 12 to 24.
#
# if __name__ == '__main__':
#     for i in range(12, 25):
#         print(i)
#---------------------------------------
# Ex 2:
# Write a for loop that prints the ODD numbers from 7 to 31
#
# if __name__ == '__main__':
#     for i in range(7, 32):
#         if i % 2 == 1:
#             print(i)
# ---------------------------------
# Ex 3:
# Write a for loop that prints the EVEN numbers from 10 to -20.
#
# if __name__ == '__main__':
#     for i in range(10, -20, -1):
#         if i % 2 == 0:
#             print(i)
# ---------------------------------
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
# -------------------------------------
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
# ----------------------------------
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
# def delete_property(students_list, property):
#     for student in students_list:
#         if property in student:
#             student.pop(property)
#         else:
#             continue
#
# def print_property(students_list, property):
#     student_counter = 1
#     for student in students_list:
#         print(f"Student {student_counter} Property: {student[property]}")
#         student_counter += 1
#
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
# ---------------------------
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
# def pet_type(pets_list):
#     for pet in pets_list:
#         if pet["animal_type"] == "cat":
#             print("animalType: cat")
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
# -----------------------
