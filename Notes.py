# """
# # print("Hello world")
# # # This is a new line of code
# #
# # # Mr. Wiebe
# #
# # a = 4
# # b = 3
# #
# # print(3 + 5)
# # print(5 - 3)
# # print(3 * 5)
# # print(6 / 2)
# # print(3 ** 2)
# #
# # print()
# # print("Try to figure out how this works")
# # print(13 % 5)
# #
# # # the "%" sign is a modulus. It finds the remainder.
# #
# # car_name = "The Wiebe Mobile"
# # car_type = "BMW"
# # car_cylinders = 8
# # car_mpg = 5000.9
# #
# # print("I have a car called %s. It's pretty nice." % car_name)
# # print("I have a car called %s. It's a %s." % (car_name, car_type)) # watch the order
# #
# # # Here is where we get a little fancy
# # print("What is your name?")
# # name = input(">_ ")
# # print("Hello %s." % name)
# #
# # age = input("How old are you?")
# # print("%s?! That's really old. You belong in a retirement home." % age)
# # Functions
# def print_hw():
#     print("Hello World")
# print_hw()
# print_hw()
# print_hw()
# def say_hi(name):  # name is a parameter
#     print("Hello %s." % name)
#     print("Enjoy your day.")
# say_hi("John")
# def print_age(name, age):
#     print("%s is %d years old." % (name, age))
#     age += 1  # age = age + 1
#     print("Next year, they will be %d" % age)
# print_age("John", 15)
# def f(x):
#     return x**3 + 4 * x**2 + 7 * x - 4
# print(f(3))
# print(f(4))
# print(f(5))
# # If statements
# def grade_calc(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 80:
#         return "B"
#     elif percentage >= 70:
#         return "C"
#     elif percentage >= 60:
#         return "D"
#     else:
#         return "F"
# '''Write a function called "happy_bday"
# that "sings" (prints) Happy birthday
# It must take one parameter called "name"
# '''
# def happy_bday(name):
#     print("Happy birthday to you" + ",")
#     print("Happy birthday to you" + ",")
#     print("Happy birthday to " + name + ",")
#     print("Happy birthday to you" + ".")
# happy_bday("John")
# # Loops
# for num in range(10):
#     print(num + 1)
# a = 1
# while a <= 10:
#     print(a)
#     a += 1
# # Random Numbers
# import random  # This should be on line 1
# print(random.randint(0, 100))
# """
#
#
# # Lists
# the_count = [1, 2, 3, 4, 5]
# shopping_list = ["Noodles", "Eggrolls", "Milk", "rice", "soda", "chips"]
#
# print(shopping_list[0])
#
# print(len(shopping_list))
#
# # Going through a list
# for item in shopping_list:
#     print(item)
#
# for num in the_count:
#     print(num * 2)
#
# len(shopping_list)  # Gives me the length of the list
# range(3)  # Gives a list of the numbers 0 through 2
# range(len(shopping_list))  # A list of EVERY index in a list
#
# for num in range(len(shopping_list)):
#     item = shopping_list[num]
#     print("The item at index %d is %s" % (num, item))
#
# # Turn things into a list
# str1 = "Hello Class!"
# listOne = list(str1)
# print(listOne)
# listOne[11] = '.'
# print(listOne)
# print("".join(listOne))
#
# # Add things to a list
# shopping_list.append("cereal")
# print(shopping_list)
#
# # Removing things from a list
# shopping_list.remove("soda")
# print(shopping_list)
# shopping_list.pop(0)
# print(shopping_list)
#
# # the string class
# import string
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.punctuation)
# print(string.digits)
#
# # Dealing with strings
# strTwo = "ThIs iS a VeRY oDd sEnTenCE"
# lowercase = strTwo.lower()
# print(lowercase)
# Dictionaries - Make up a key: value pair
dictionary = {'name': 'Lance', 'age': 18, 'height': 6 * 12}

# Accessing from a dictionary
print(dictionary['name'])
print(dictionary['age'])
print(dictionary['height'])
