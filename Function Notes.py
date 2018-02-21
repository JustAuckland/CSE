# Defining Functions
def hello_world():
    print("Hello World!")


hello_world()


def square_it(number):
    return number * 2


print(square_it(3))


def tip_calc(subtotal):
    tip_amt = subtotal * 0.18  # tip_amt is a local variable
    print("The tip ammount is $%s" % tip_amt)
    return tip_amt


def total_bill(subtotal):
    total = subtotal + tip_calc(subtotal)
    return total


print("$%s" % (total_bill(100)))


def distance(x1, y1, x2, y2):
    inside = (x2 - x1) ** 2 + (y2 - y1) ** 2
    answer = inside **  0.5
    return answer


print(distance(0, 0, 3, 4))

