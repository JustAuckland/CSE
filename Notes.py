"""
# # print("Hello World!")
# #
# # # Mr. Wiebe (Use ctrl+/ to toggle comments)
# #
# # print(3 + 5)
# # print(5 - 3)
# # print(5 * 3)
# # print(6 / 2)
# # print(3 ** 2)
# #
# # print()  # Creates a blank line
# # print("See if you can figure this out")
# # print(15 % 5)
# #
# # # Variables
# # car_name = "Wiebe Mobile"
# # car_type = "Lamborghini Sesto Elemento"
# # car_cylinders = 8
# # car_mpg = 9000.1
# #
# # # Inline Printing
# # print("My car is the %s." % car_name)
# # print("My car is the %s. It is a %s" % (car_name, car_type))
# #
# # # Taking input
# # name = input("What is your name? ")
# # print("Hello %s." % name)
# # # print(name)
# #
# # age = input("How old are you? ")
# # print("%s?! That old? You belong in a museum." % age)
# # print("That or a retirement home.")
#
# # Change to the file
#
#
# def print_hw():
#     print("Hello World")
#
#
# print_hw()
#
#
# def say_hi(name):  # name is a "parameter"
#     print("Hello %s." % name)
#     print("I hope you have a fantastic day.")
#
#
# say_hi("John")
#
#
# def birthday(age):
#     age += 1  # age = age + 1
#     print(age)
#
#
# say_hi("John")
# print("John is 15. Next year:")
# birthday(15)
#
# Press Ctrl-A and Ctrl-/
# to comment old code
def f(x):
    return x**5 + 4 * x ** 4 - 17*x**2 + 4
# print(f(3))
# print(f(3) + f(5))
# If statements
def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:  # Else if
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"
# Loops
# for num in range(5):
#     print(num + 1)
# for mystery in "Hello World":
#     print(mystery)
a = 1
while a < 10:
    print(a)
    a += 1
response = ""
# while response != "Hello":
#     response = input("Say \"Hello\"")
print("Hello \nWorld")  # \n means newline
import random  #imports should be at the top
print(random.randint(0, 6))
"""


# Lists

the_count = [1, 2, 3, 4, 5]
characters = ["graves", "Dory", "Boots", "Dora", "Shrek", "Obi-wan", "Carl"]
print(characters[0])
print(characters[4])

print(len(characters))  # Gives you the length of the list

# Going through lists
for char in characters:
    print(char)

for num in the_count:
    print(num ** 2)

len(characters)
range(3)   # Makes a list of the numbers from 0 to 2
range(len(characters))  # Makes a list of ALL INDICES

for num in range(len(characters)):
    char = characters[num]
    print("The character at index %d is %s" % (num, char))

str1 = "Hello World!"
listOne = list(str1)
print(listOne)
listOne[11] = '.'
print(listOne)
newStr = "".join(listOne)
print(newStr)

# adding stuff to a list
characters.append("Ironman/Batman/whomever you want")
print(characters)

# removing things from a list
characters.remove("Carl")
print(characters)

characters.pop(6)
print(characters)

# the string class
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.digits)
print(string.punctuation)

strTwo = 'ThIs sEntENcE iS uNuSuAL'
lowercase = strTwo.lower()
print(lowercase)