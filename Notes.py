# print("Hello World")
# #Comment
# print(3+5)
# print(3**3)
# print()
# # cat_name = "Kitty"
# # cat_type = "White"
# # cat_cylinders = 1
# # cat_mpg = 12
# #
# # print("My cat is named %s. It is a %s cat" % (cat_name, cat_type))
# # name = input ("what is your name?")
# # print("Hello %s." % name)
# # print(name)
#
# # age = input ("How old are you?")
# # print("%s? Is that old enough to be watching that movie?" % age)
#
# def print_hw():
#     print("Hello World")
#
#
# print_hw()
#
#
# def say_hi(name):
#     print("Hello %s." % name)
#     print("I hope you have a fantastic day.")
#
#
# say_hi("Box Box")
#
#
# def birthday(age):
#     age+=1  # age=age+1
#     print(age)
#
# say_hi("Box Box")
# print("John is 15. Next year:")
# birthday(15)


def f(x):
    return x**5 + 4 * x **4 - 17*x**2 + 4


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


# for num in range(5):
#     print(num+1)


# for Cat in "Hello World":
#     print(Cat)


# response = ""
# while response != "Hello":
#     response = input("Say \"Hello\"")


# print ("Hello \nWorld")
#
#
# import random
# print(random.randint(0, 6))
#
#
# def reverse_order():
#     first_name = input('what is your first name')
#     last_name = input('what is your last name')
#     print(reverse_order)


def happy_bday(name):
    print("Happy birthday to you,")
    print("Happy birthday to you,")
    print("Happy birthday dear %s") % name
    print("Happy birthday to you!")

