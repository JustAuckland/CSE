print("Hello World")
#Comment
print(3+5)
print(3**3)
print()
# cat_name = "Kitty"
# cat_type = "White"
# cat_cylinders = 1
# cat_mpg = 12
#
# print("My cat is named %s. It is a %s cat" % (cat_name, cat_type))
# name = input ("what is your name?")
# print("Hello %s." % name)
# print(name)

# age = input ("How old are you?")
# print("%s? Is that old enough to be watching that movie?" % age)

def print_hw():
    print("Hello World")


print_hw()


def say_hi(name):
    print("Hello %s." % name)
    print("I hope you have a fantastic day.")


say_hi("Box Box")


def birthday(age):
    age+=1  # age=age+1
    print(age)

say_hi("Box Box")
print("John is 15. Next year:")
birthday(15)
