# class exercise
#
# 2222
# if __name__ == '__main__':
#     global total_payment
#     total_payment = 0
#     students = {"name": "ben",
#                 "last_name": "cohen",
#                 "age": 22,
#                 "course": "AI",
#                 "grade": 100,
#                 }
#
# students["is_pay_received"] = True
# students["payment_amount"] = 1000
#
#
# def print_student(students):
#     print(students)
#
#
#
# def payment_calculation(students):
#     global total_payment
#     if students["is_pay_received"]:
#         total_payment = total_payment + students["payment_amount"]
#     else:
#         print("Student " + students["name"] + " did not pay")
#
#
#
# payment_calculation(students)
# print(total_payment)
# -------------------------------
# Exercise 1:
# Write a function called display_name() that takes a dictionary as an argument and
# prints the person's first and last name.
#
# def display_name(person):
#     print("Name: " + person["first_name"])
#     print("Last Name: " + person["last_name"])
#
# if __name__ == '__main__':
#     person_info = {"first_name": "Jonathan",
#                    "last_name": "Tzur"}
#     display_name(person_info)
# ----------------------------
# Exercise 2:
# Write yourself a virtual cat.
# ● Create a dictionary that represents a cat. It should have properties for
# tiredness, hunger, loneliness and happiness with values of scale
# from 0 - 10, For example: loneliness: 5, happiness: 8 etc…
# ● Next, write functions that increase and decrease those properties. Call them
# something that actually represents what would increase or decrease these
# things, like "feed", "sleep", or "pet".
#
# def food_eat(kitty):
#     if kitty["hunger"] > 0:
#         kitty["hunger"] -= 1
#     else:
#         print("kitty is full")
#
# def food_need(kitty):
#     if kitty["hunger"] < 10:
#         kitty["hunger"] += 1
#     else:
#         print("kitty cant be more hungry (lie)")
#
#
# def sleep_need(kitty):
#     if kitty["tiredness"] < 10:
#         kitty["tiredness"] += 1
#     else:
#         print("kitty cant be more tired")
#
# def sleep_get(kitty):
#     if kitty["tiredness"] > 0:
#         kitty["tiredness"] -= 1
#     else:
#         print("kitty is cant be less sleepy")
#
# def pet_get(kitty):
#     if kitty["loneliness"] > 0:
#         kitty["loneliness"] -= 1
#     else:
#         print("kitty is cant be less lonley")
# def pet_need(kitty):
#     if kitty["loneliness"] < 10:
#         kitty["loneliness"] += 1
#     else:
#         print("kitty cant be more lonely")
#
# def play_get(kitty):
#     if kitty["happiness"] > 0:
#         kitty["happiness"] -= 1
#     else:
#         print("kitty is cant be less happy")
# def play_need(kitty):
#     if kitty["happiness"] < 10:
#         kitty["happiness"] += 1
#     else:
#         print("kitty cant be more happy")
#
#
# if __name__ == '__main__':
#     cat = {"tiredness": 0,
#            "hunger": 10,
#            "loneliness": 10,
#            "happiness": 0}
#
#     sleep_get(cat)
#     food_need(cat)
#     pet_need(cat)
#     play_get(cat)
#
# ----------------------
# Exercise 3:
# Create a recipe dictionary that has information on your favorite recipe. It should have
# the following properties:
# ● title (a string),
# ● number_of_orders (how many times this recipe was ordered),
# ● is_vegan(Boolean), and ingredients (an array of strings).
# Write functions that update servings and delete or update ingredients.
# Write a function that prints a receipt with all the information.
# Write a function that receives a receipt and returns if the receipt is vegan or not
# (Boolean value).
#
#
# def get_serving(recipe):
#     recipe["number_of_orders"] += 1
#
# def ingredients_update(recipe, indgredient, add_or_del):
#     if add_or_del == "add":
#         recipe["ingredients"].append(indgredient)
#     elif add_or_del == "del":
#         recipe["ingredients"].remove(indgredient)
#     else:
#         print("Action invalid")
#
# def print_receipt(recipe):
#     print("Dish: " + recipe["name"])
#     print("Amount: " + str(recipe["number_of_orders"]))
#     print("Vegan: " + str(recipe["is_vegan"]))
#     print("Ingredients: " + str(recipe["ingredients"]))
#
#
# def is_vegan(recipe):
#     if recipe["is_vegan"]:
#         return True
#     else:
#         return False
#
# if __name__ == '__main__':
#     recipe = {"name": "omelette",
#               "number_of_orders": 10,
#               "is_vegan": True,
#               "ingredients": ["eggs","salt"]
#               }
#     print_receipt(recipe)
#     print(is_vegan(recipe))
# -------------------------------
# Exercise 4:
# Create an array of dictionaries, where each dictionary describes a book and has the
# following properties:
# ● title (a string),
# ● author (a string),
# ● already_read (a boolean indicating if you read it yet).
# write a function that get the array of books and book number as parameters
# If the book array has a book_number as an index, your function should check if the
# book was read or not and print the result.
# If inside the array there is no book with that index your function should print:
# “The array doesn’t contain book number {book_number}”
#
# def book_number(books, book_number):
#     books_index = len(books) - 1
#     if book_number <= books_index:
#         print(books[book_number]["already_read"])
#     else:
#         print("The array doesn’t contain book number " + str(book_number))
#
#
# if __name__ == '__main__':
#     books = [
#         {"book_title": "Harry Potter",
#         "author": "J. K. Rowling",
#         "already_read": False},
#
#         {"book_title": "To Kill a Mocking Bird",
#         "author": "Harper Lee",
#         "already_read": False},
#
#         {"book_title": "The Hobbit",
#         "author": "J. R. R. Tolkien",
#         "already_read": True},
#
#         {"book_title": "Moby Dick",
#         "author": "Herman Melville",
#         "already_read": False}
#
#          ]
#
#     book_number(books, 1)