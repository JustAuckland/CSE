class Vehicle(object):
    def __init__(self, engine_type, steering_mechanism, seat):
        self. engine_type = engine_type
        self.steering_mechanism = steering_mechanism
        self.seat = seat

    def move(self):
        print("You move forward")

    def change_direction(self):
        print("You change direction")


class Car(Vehicle):
    def __init__(self, seat, hp):
        super(Car, self).__init__("engine", "steering", seat)
        self.horsepower = hp

    def turn_on(self):
        print("You turn the key and the car turns on")


test_car = Car(4, 9001)
test_car.change_direction()


class KeylessCar(Car):
    def __init__(self, seat, hp):
        super(KeylessCar, self).__init__(seat, hp)

    def turn_on(self):
        print("You push a bbutton and the car turns on")


cool_car = KeylessCar(4, 9001)
test_car.turn_on()
cool_car.turn_on()


class Tesla(KeylessCar):
    def __init__(self, seat, hp):
        super(Tesla, self).__init__(seat, hp)

    def fly(self):
        print("You launch the car into low earth orbit")

    def turn_on(self):
        Car.turn_on(self)


musk_car = Tesla(2, 400)
musk_car.turn_on()
