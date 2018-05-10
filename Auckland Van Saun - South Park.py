"""

- import statements
-class definitions
    -items
    -characters
    -rooms
-institution of classes
-controller

"""
import random

randomnumber = random.randint(1, 10)
mod = randomnumber % 2


def clear_screen():
    print("_________________________________________________________________________")
    print("")


class NumberError(Exception):
    def __init__(self):
        super(NumberError, self).__init__()


def game_over():
    print("   _____          __  __ ______    ______      ________ _____  _\n"
          "  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \| |\n"
          " | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) | |\n"
          " | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /| |\n"
          " | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \|_|\n"
          "  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_(_)\n")
    quit(0)


def inventory():
    print("this worked out well")
    clear_screen()


def fight(enemy):
    endloop = 0
    clear_screen()
    print("You have %d health left" % you.health)
    print("%s has %d health left" % (enemy.name, enemy.health))
    while you.health > 0 and enemy.health > 0 and endloop == 0:
        print("What do you want to do?")
        attack_commands = ['Attack', "Do nothing", "Use item", "Run"]
        for num, action in enumerate(attack_commands):
            print(str(num + 1) + ": " + action)
        print("\n" * 1)
        print("_________________________________________________________________________")
        print("")
        try:
            cmd = int(input(">_"))
            clear_screen()
            if cmd == 1:
                you.attack(enemy)
            elif cmd == 2:
                print("You do nothing")
            elif cmd == 3:
                print("\"Open\'s bag\"")
            elif cmd == 4:
                print(mod)
                if mod == 0:
                    print("You got away safely")
                    endloop += 1
                else:
                    print("You were unable to escape")

            elif cmd > len(attack_commands) or cmd < 0:
                raise NumberError
        except ValueError:
            print("That is not a number")
            continue
        except NumberError:
            print("Invalid number")
            continue
        if enemy.health > 0:
            enemy.attack(you)
            if you.health <= 0:
                print("You have died at the hands of %s\n" % enemy.name)
                game_over()
        if enemy.health <= 0:
            print("%s has been defeated\n" % enemy.name)


# Items


class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Combat(Item):
    def __init__(self, name, description, stats):
        super(Combat, self).__init__(name, description)
        self.stats = stats


class Defend(Combat):
    def __init__(self, name, description, stats, armor):
        super(Defend, self).__init__(name, description, stats)
        self.armor = armor


class Attack(Combat):
    def __init__(self, name, description, stats, damage):
        super(Attack, self).__init__(name, description, stats)
        self.damage = damage


class Pistol(Attack):
    def __init__(self, name, description, stats, damage):
        super(Pistol, self).__init__(name, description, stats, damage)

    def shoot(self):
        print("You shoot your %s" % self.name)

    def reload(self):
        print("You reload your %s" % self.name)


class Bow(Attack):
    def __init__(self, name, description, stats, damage):
        super(Bow, self).__init__(name, description, stats, damage)

    def shoot(self):
        print("You shoot your %s" % self.name)

    def reload(self):
        print("You reload your %s.. slowly" % self.name)


class Sword(Attack):
    def __init__(self, name, description, stats, damage):
        super(Sword, self).__init__(name, description, stats, damage)

    def stab(self):
        print("You stab %s" % currentnode.character.name)


class Shield(Defend):
    def __init__(self, name, description, stats, armor):
        super(Shield, self).__init__(name, description, stats, armor)


class Helmet(Defend):
    def __init__(self, name, description, stats, armor):
        super(Helmet, self).__init__(name, description, stats, armor)


class Misc(Item):
    def __init__(self, name, description):
        super(Misc, self).__init__(name, description)


class Cosmetic(Misc):
    def __init__(self, name, description):
        super(Cosmetic, self).__init__(name, description)


class Hidden(Misc):
    def __init__(self, name, description):
        super(Hidden, self).__init__(name, description)


class Consumable(Item):
    def __init__(self, name, description):
        super(Consumable, self).__init__(name, description)


class Heals(Consumable):
    def __init__(self, name, description, health=0):
        super(Heals, self).__init__(name, description)
        self.health = health

    def heal(self):
        print("You have healed yourself for %d health" % self.health)


class Drinks(Consumable):
    def __init__(self, name, description, shield=0):
        super(Consumable, self).__init__(name, description)
        self.shield = shield

    def drink(self):
        print("You have shielded yourself for %d ammount of damage" % self.shield)


antoniodoll = Item("Antonio Banderas doll", "A nearly-lifesize blow-up doll of Antonio Banderas")


# Characters


class Character(object):
    def __init__(self, name, description, health, stats, armor=0, item=None):
        self.name = name
        self.description = description
        self.health = health
        self.stats = stats
        self.armor = armor
        self.item = item

    def takedamage(self, amount):
        dmg = amount - self.armor
        if dmg < 0:
            dmg = 0
            print("The attack was not very effective...")
        self.health -= dmg
        if self.health < 0:
            self.health = 0
        if self.name == "You":
            print("You have %d hp left" % self.health)
        else:
            print("%s has %d hp left" % (self.name, self.health))

    def attack(self, target):
        if self.name == "You":
            print("You attack %s" % target.name)
        else:
            print("%s attacks %s" % (self.name, target.name))
        target.takedamage(self.stats)
        print()


class Enemy(Character):
    def __init__(self, name, description, health, stats, armor=0, item=None):
        super(Enemy, self).__init__(name, description, health, stats, armor, item)


class Friendly(Character):
    def __init__(self, name, description, health, stats, armor=0, item=None):
        super(Friendly, self).__init__(name, description, health, stats, armor, item)


you = Character("You", "You are wearing a white sleeveless coat and wearing a backwards baseball cap",
                175, 20)
cartman = Enemy("Eric Cartman", "a fat kid your age, wearing a red coat and a blue poofball hood",
                125, 20, 0, antoniodoll)
stan = Friendly("Stan Marsh", "a kid your age, wearing a brown coat with a blue hat", None, 100, 25)
kyle = Friendly("Kyle Broflovski", "a kid your age wearing a green coat with an orange hat", None, 100, 30)
kenny = Enemy("Kenny McCormick", "a kid your age wearing an orange coat with the hood covering most of his face",
              85, 40)
butters = Friendly("Butters Stotch", "a kid your age wearing a light-blue coat", 90, 25)
jimmy = Enemy("Jimmy Valmer", "a kid your age with crutches wearing a yellow shirt", 140, 40)
craig = Friendly("Craig Tucker", "a kid your age weaing a blue coat, with a matching blue hood", 100, 30)
clyde = Enemy("Clyde Donovan", "a kid your age wearing a red and blue coat", 100, 25)
bebe = Enemy("Bebe Stevens", "a girl your age with blonde curly hair, wearing a bright red coat", 120, 20)
al = Friendly("Big Al", "a man in his late thirties wearing a pink hawaiian T-shirt and constantly smoking a cigar",
              150, 30)
token = Friendly("Token Black", "a kid your age with an afro, wearing a purple shirt", 100, 25)


# World Map


class Place(object):
    def __init__(self, name, description, north, south, east, west, enter, up, down, character=None, item=None,
                 leave=None):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.enter = enter
        self.up = up
        self.down = down
        self.character = character
        self.item = item
        self.exit = leave

    def move(self, direction):
        global currentnode
        currentnode = globals()[getattr(self, direction)]


yourhouse = Place("Your House", "You see a bright red house", None, None, "randomtree", "southparksign",
                  "inside_yourhouse", None, None, None, antoniodoll)
randomtree = Place("Random Tree", "You see a random tree", None, None, "buttershouse", "yourhouse",
                   "inside_buttershouse", None, None)
buttershouse = Place("Butters\'house", "You see a red brownish house", None, None, "cartmanshouse", "randomtree",
                     "inside_buttershouse", None, None, butters)
cartmanshouse = Place("Cartman\'s house", "You see a bright green house", None, None, "stanshouse", "buttershouse",
                      "inside_cartmanshouse", None, None, cartman)
stanshouse = Place("Stan\'s house", "You see a dark green house", None, None, "kyleshouse", "cartmanshouse",
                   "insidestanshouse", None, None, stan)
kyleshouse = Place("Kyle\'s house", "You see a moss green house", None, None, "stonepath", "stanshouse",
                   "insidekyleshouse", None, None, kyle)
stonepath = Place("Stone Path", "You see a paved path to your left leading to what looks like a park", "playground",
                  None, "traintracks", "kyleshouse", None, None, None)
traintracks = Place("Train Tracks", "You see train tracks almost hidden under a trick layer of snow", None, None,
                    "sodosopa", "stonepath", None, None, None)
sodosopa = Place("Sodosopa", "You see a broken down, olive green house, surrounded almost completely by what seems "
                             "to be a modernized restaurant",
                 None, None, None, "traintracks", "insidekennyshouse", "insidesodosopa", None, kenny)
southparksign = Place("SouthPark Sign", "You see a sign that says \"South Park\" \nOn your left lies a road\n"
                                        "Beyond the road you see a bus stop",
                      None, None, "yourhouse", "road", None, None, None)
road = Place("Road", "A road blocks your path", None, None, "southparksign", "busstop", None, None, None)
busstop = Place("Bus Stop", "You see the local elementary school's bus stop", None, None, "road", "jimmyshouse",
                None, None, None)
jimmyshouse = Place("Jimmy\'s house", "You see a red house", None, None, "busstop", "craigshouse", "inside_jimmyshouse",
                    None, None, jimmy)
craigshouse = Place("Craig\'s house", "You see a light brown house", None, None, "jimmyshouse", "clydeshouse",
                    "inside_craigshouse", None, None, craig)
clydeshouse = Place("Clyde\'s house", "You see a dark brown house", None, None, "craigshouse", "bebeshouse",
                    "inside_clydeshouse", None, None, clyde)
bebeshouse = Place("Bebe\'s house)", "You see a red house", None, None, "clydeshouse", "communitycenter",
                   "insidebebeshouse", None, None, bebe)
communitycenter = Place("Community Center", "You see a large, orange multi-purpose building", "policestation", None,
                        "bebeshouse", "elementaryschool", "insidecommunitycenter", None, None)
elementaryschool = Place("South Park Elementary School", "You see a yellow double-storie elementary school building",
                         "church", None, "communitycenter", None, "insideelementaryschool", None, None)
church = Place("Church", "You see a wooden steeple", None, "elementaryschool", "policestation", None, "insidechurch",
               None, None)
policestation = Place("Police Station", "You see a large black police station", None, None, "cityhall", "church",
                      "insidepolicestation", None, None)
cityhall = Place("City Hall", "You see an authentic stone building that looks important", None, None, "townsquare",
                 "policestation", "insidecityhall", None, None)
townsquare = Place("Town Square", "You see a small rectangular park with a few trees and benches", None, None,
                   "postoffice", "cityhall", "insidetownsquare", None, None)
postoffice = Place("Post Office", "You see a small blue and white post office", None, None, "bank", "townsquare",
                   "insidepostoffice", None, None)
bank = Place("South Park Bank", "You see a short, dark green building", None, None, "tacoshop", "postoffice",
             "insidebank", None, None)
tacoshop = Place("Taco Stand", "You see a white and red taco food truck", None, None, "playground", "bank",
                 "insidetacoshop", None, None)
playground = Place("playground", "you see a basketball court and a small playground to the right", None, "stonepath",
                   "alshouse", "tacoshop", "insideplayground", None, None)
alshouse = Place("Al\'s House", "You see a bright red house", "coffeeshop", None, None, "playground", "insidealshouse",
                 None, None, al)
coffeeshop = Place("Tweal Bro\'s Coffee", "You see a small tan building with a coffee sign", None, "alshouse", None,
                   "theatre", "insidecoffeeshop", None, None)
theatre = Place("Movie Theatre", "You see a large orange and red theatre", None, None, "coffeeshop", "tokenshouse",
                "insidetheatre", None, None)
tokenshouse = Place("Token\'s House", "You see a very large fenced-off light brown manor", None, None, "theatre",
                    "mall", "insidetokenshouse", None, None, token)
mall = Place("South Park Mall", "You see a very large light-blue mall under construction", None, None, "tokenshouse",
             "kfc", None, None, None)
kfc = Place("South Park Fried Chicken", "You see a fried chicken fast-food restaurant", None, None, "mall",
            "chineesefood", "insidekfc", None, None)
chinesefood = Place("City Wok Cineese Food", "You see a light-blue and red chineese styled building", None, None,
                    "kfc", "gunstore", "insidechineesefood", None, None)
gunstore = Place("Jimbo\'s Guns", "You see a crimson red building with many unique weapons in the window", None, None,
                 "chinesefood", "bar", "insidegunstore", None, None)
bar = Place("Skeeter\'s Wine Bar", "You see a swamp-green building with dark-tinted buildings", None, "church",
            "gunstore", None, "insidebar", None, None)
inside_yourhouse = Place("Inside Your House""You see a good-sized family room with a couch  and a TV", None, None, None,
                         None, None, None, None, None, None, "yourhouse")


# Controller


directions = ["north", "south", "east", "west", "enter", "exit", "up", "down"]
shortened = ["n", "s", "e", "w", "in", "out", "u", "d"]
currentnode = yourhouse

while you.health > 0:
    # print()
    print(currentnode.name)
    print(currentnode.description)

    if currentnode.character is not None:
        print("You see %s" % currentnode.character.name)

    command = input(">_").lower().strip()
    clear_screen()
    if command == "quit":
        quit(0)
    elif command in shortened:
        location = shortened.index(command)
        command = directions[location]
    if command in directions:
        try:
            currentnode.move(command)
        except KeyError:
            print("You can\'t go that way")
    elif "fight" in command:
        print("You challenge %s" % currentnode.character.name)
        if currentnode.character is not None and isinstance(currentnode.character, Enemy):
            fight(currentnode.character)
        else:
            if currentnode.character is not None and isinstance(currentnode.character, Friendly):
                print("There is nobody here willing to fight. \nDon\'t be mean like that")
            else:
                print("There is nobody here. \nIf someone was here, they'd laugh at you")
    elif "inventory" in command:
        print("You open your bag")
        inventory()

    elif "description" in command:
        if currentnode.character:
            print("You see a %s named %s" % (currentnode.character.description, currentnode.character.name))
    elif command == "look":
        if currentnode.item is not None:
            if currentnode.item.name[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                print("You see an %s in the room" % currentnode.item.name)
            else:
                print("You see a %s in the room" % currentnode.item.name)
    elif command == "give":
        print("")

    else:
        print("Command not recognized")
