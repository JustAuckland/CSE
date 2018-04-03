class Person(object):
    def __init__(self, name, education):
        self.name = name
        self.education = education

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, education, uniform):
        super(Employee, self).__init__(name, education)
        self.uniform = uniform

    def greetings(self):
        print("Welcome to this establishment")


class Programmer(Employee):
    def __init__(self, name, education, uniform, computer):
        super(Programmer, self).__init__(name, education, uniform)
        self.computer = computer

    def type(self):
        print("Your typing powers increase")


persona = Programmer("Auckland", "MIT", "Casual", "HP Spectre")
persona.type()