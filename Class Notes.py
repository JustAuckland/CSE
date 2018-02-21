#Define a class
class Cat(object):
    #TWO underscores before and after
    def __init__(self, colour, pattern):
        # Things that a Cat has
        self.colour = colour
        self.pattern = pattern
        self.state = "happy"
        self.hungry = False

        #Things that a Cat can do
    def jump(self):
        self.state = "Scared"
        print("The cat jumps in the air")

    def play(self):
        self.state = "happy"
        print("You play with the cat")


# Instantiating (creating) two cats
cute_cat = Cat("brown", "Spots")
cute_cat2 = Cat("grey", "no spots")

# Getting information about the cats
print(cute_cat.colour)
print(cute_cat2.state)
print(cute_cat2.colour)

cute_cat.jump()
print(cute_cat.state)
print(cute_cat2.state)

cute_cat.play()
print(cute_cat.state)


class Car(object):
    def __init__(self, colour, brand, horsepower, cylinders):
        self.colour = colour
        self.brand = brand
        self.horsepower = horsepower
        self.cylinders = cylinders

def turn_on(self):
    if self.engineOn:
        print("Nothing Happens")
    else:
        print("The engine turns on")
        self. engineOn = True

    def mmove_forars(self):
        if self.engineOn:
            print("You move forward")
        else:
            print("Nothing Happens")









my_car = Car(4, "Subaru", "Blue")

my_car.turn_on()
my_car.move_forward()
my_car.turn_off()