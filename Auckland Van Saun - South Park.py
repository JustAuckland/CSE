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

inv = []

close = 0


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


def drop():
    if currentnode.character.item is not None:
        print("%s drops %s" % (currentnode.character.name, currentnode.character.item.name))
        currentnode.item = currentnode.character.item
        clear_screen()
    else:
        print()


def inventory():

    closebag = 0
    while closebag == 0:
        if len(inv) != 0:
            print("The items in your bag are : ")
            for itemname in inv:
                print(" - %s" % itemname.name)
                print()
            bag_commands = ["Give", "Close"]
            for num, action in enumerate(bag_commands):
                print(str(num + 1) + ": " + action)
            try:
                cmd = int(input(">_"))
                if cmd == 1:
                    endbagcom = 0
                    if endbagcom == 0:
                        clear_screen()
                        print("Would you like to give the %s to %s?" % (inv[0].name, currentnode.character.name))
                        print()
                        simplecommand = ["Yes", "No"]
                        for num, action in enumerate(simplecommand):
                            print(str(num + 1) + ": " + action)
                        try:
                            givecmd = int(input(">_"))
                            if givecmd == 1:
                                clear_screen()
                                print("You give %s to %s" % (inv[0].name, currentnode.character.name))
                                currentnode.character.item = inv[0]
                                inv.remove(inv[0])
                                endbagcom += 1
                                clear_screen()
                                specialprocesses()

                            elif givecmd == 2:
                                endbagcom += 1
                                clear_screen()

                            elif cmd > len(simplecommand) or cmd < 0:
                                raise NumberError

                        except ValueError:
                            print("That is not a number")
                            continue
                        except NumberError:
                            print("Invalid number")
                            continue

                elif cmd == 2:
                    print("You closed the bag")
                    closebag += 1
                    clear_screen()
                elif cmd > len(bag_commands) or cmd < 0:
                    raise NumberError

            except ValueError:
                print("That is not a number")
                continue
            except NumberError:
                print("Invalid number")
                continue
        else:
            print("You have nothing in your bag so you decide to close it")
            closebag += 1
            clear_screen()


def fight(enemy):
    endloop = 0
    clear_screen()
    print("You have %d health left" % you.health)
    print("%s has %d health left" % (enemy.name, enemy.health))
    while you.health > 0 and enemy.health > 0 and endloop == 0:
        randomnumber = random.randint(1, 10)
        mod = randomnumber % 2
        print("What do you want to do?")
        attack_commands = ["Attack", "Do nothing", "Use item", "Run"]
        for num, action in enumerate(attack_commands):
            print(str(num + 1) + ": " + action)
        print("\n" * 1)
        clear_screen()
        try:
            cmd = int(input(">_"))
            clear_screen()
            if cmd == 1:
                you.attack(enemy)
            elif cmd == 2:
                print("You do nothing")
            elif cmd == 3:
                print("\"Open\'s bag\"")
                inventory_bag = inv
                for num, action in enumerate(inventory_bag):
                    print(str(num + 1) + ": " + action)
            elif cmd == 4:
                print()
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
        if endloop == 0:
            if enemy.health > 0:
                enemy.attack(you)
                if you.health <= 0:
                    print("You have died at the hands of %s\n" % enemy.name)
                    game_over()
            if enemy.health <= 0:
                print("%s has been defeated\n" % enemy.name)
                if enemy.item is not None:
                    drop()
                else:
                    print("%s had no treasures to drop" % enemy.name)


def specialprocesses():
    if currentnode.character == cartman and currentnode.character.item == antoniodoll:
        print("Eric Carman says : \nThank you for getting my birthday present early! How can I repay you?")
        print("I know, here take this CD, no charge!")
        inv.append(faithcd)
        clear_screen()
        print("You have obtained Faith +1 CD")
        print("I'm pretty sure token needs one, not too sure what he has to offer")
        clear_screen()
    elif currentnode.character == token and currentnode.character.item == faithcd:
        print("Token says : \nGreat! Now I can listen to our best hits. Here take this as a \"Token\"")
        clear_screen()
        inv.append(bassguitar)
        print("You take Tokens Bass Guitar")
        clear_screen()
        print("Haha! get it \"Token\". Nah I'm just kidding")
        print("Find a house of light brown, and they may trade with you, the most prestigious of binders")


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


antoniodoll = Item("Antonio Banderas doll", "A nearly-lifesize doll of Antonio Banderas")
trapperkeeper = Item("Trapper Keeper", "An all-in-one binder, notebook, folder, calculator, pencil-holder, "
                                       "and much much more")
cootiecatcher = Item("Cootie-Catcher", "A future telling device created by the girls, the boys will do anything to get"
                                       " their hands on this")
faithcd = Item("Faith +1 CD", "An album created by Eric Carman's christian rock band with Token and Budders")
stickoftruth = Item("Stick Of Truth", "A mythical item that allows the holder to bring peace to all, said to be a "
                                      "legend")
wizzardhat = Item("Wizzard Hat", "An item that, when in possesion by Cartman, will give him special wizzard-like "
                                 "powers, like seeing R-rated movies without permission from his mom")
bassguitar = Item("Bass Guitar", "A guitar famously used by Token while in the band Faith +1")


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
cartman = Friendly("Eric Cartman", "a fat kid your age, wearing a red coat and a blue poofball hood",
                   125, 20)
stan = Friendly("Stan Marsh", "a kid your age, wearing a brown coat with a blue hat", 100, 25)
kyle = Friendly("Kyle Broflovski", "a kid your age wearing a green coat with an orange hat", 100, 30)
kenny = Friendly("Kenny McCormick", "a kid your age wearing an orange coat with the hood covering most of his face",
                 85, 40)
butters = Enemy("Butters Stotch", "a kid your age wearing a light-blue coat", 90, 25)
jimmy = Friendly("Jimmy Valmer", "a kid your age with crutches wearing a yellow shirt", 140, 40)
craig = Friendly("Craig Tucker", "a kid your age weaing a blue coat, with a matching blue hood", 100, 30)
clyde = Friendly("Clyde Donovan", "a kid your age wearing a red and blue coat", 100, 25)
bebe = Friendly("Bebe Stevens", "a girl your age with blonde curly hair, wearing a bright red coat", 120, 20)
al = Friendly("Big Al", "a man in his late thirties wearing a pink hawaiian T-shirt and constantly smoking a cigar",
              150, 30)
token = Friendly("Token Black", "a kid your age with an afro, wearing a purple shirt", 100, 25)
cartmansmom = Friendly("Mrs.Cartman", "young lady wearing a light-blue blouse", 150, 15, 0, antoniodoll)


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
                  "inside_yourhouse", None, None, None)
randomtree = Place("Random Tree", "You see a random tree", None, None, "buttershouse", "yourhouse",
                   "inside_buttershouse", None, None, cartman)
buttershouse = Place("Butters\'house", "You see a red brownish house", None, None, "cartmanshouse", "randomtree",
                     "inside_buttershouse", None, None, butters)
cartmanshouse = Place("Cartman\'s house", "You see a bright green house", None, None, "stanshouse", "buttershouse",
                      "inside_cartmanshouse", None, None, cartmansmom)
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

itemcom = ["grab", "take", "pickup", "pick up"]
bagcom = ["bag", "inventory", "inv", "i"]
fightcom = ["fight", "attack"]
directions = ["north", "south", "east", "west", "enter", "exit", "up", "down"]
shortened = ["n", "s", "e", "w", "in", "out", "u", "d"]
currentnode = yourhouse

while you.health > 0:
    print("Type in \"?\" for a list of all commands")
    print("Type in \"Directions\" to see where you can go")
    print()
    print(currentnode.name)
    print(currentnode.description)

    if currentnode.character is not None:
        if currentnode.character.health > 0:
            print("You see %s" % currentnode.character.name)

    if currentnode.character == cartman:
        if close == 0:
            print("You hear Eric Cartman mumble something about his birthday present that his mom has\n"
                  "He must really want it(*Hint*Hint*)")
            clear_screen()
            close += 1

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

    elif command in bagcom:
        if len(inv) == 1:
            print("You open your bag")
            inventory()
        else:
            print("You have no items in your bag")
            clear_screen()

    elif command in fightcom:
        if currentnode.character is not None and isinstance(currentnode.character, Enemy) \
                and currentnode.character.health > 0:
            print("You challenge %s" % currentnode.character.name)
            fight(currentnode.character)
            currentnode.character = None
        else:
            if currentnode.character is None:
                print("There is nobody here. \nIf someone was here, they'd laugh at you")
            else:
                print("There is nobody here willing to fight. \nDon\'t be mean like that")

    elif command in itemcom:
        if currentnode.item is not None:
            if len(inv) > 0:
                print("You can only have one item in your inventory at a time")
            else:
                print("You picked up %s" % currentnode.item.name)
                inv.append(currentnode.item)
            currentnode.item = None
        elif isinstance(currentnode.character, Friendly):
            if currentnode.character.item is not None:
                if len(inv) > 0:
                    print("You can only have one item in your inventory at a time")
                else:
                    print("%s gives you %s" % (currentnode.character.name, currentnode.character.item.name))
                    inv.append(currentnode.character.item)
                    currentnode.character.item = None
                    clear_screen()
            else:
                print("%s has no items to give" % currentnode.character.name)
        else:
            print("There are no items in this room")

    elif "description" in command:
        if currentnode.character is not None:
            if currentnode.character.item is not None:
                if currentnode.character.item.name[0].lower() in ["a", "e", "i", "o", "u"]:
                    print("%s named %s holding an %s" % (currentnode.character.description, currentnode.character.name,
                                                         currentnode.character.item.name))
                else:
                    print("%s named %s holding a %s" % (currentnode.character.description, currentnode.character.name,
                                                        currentnode.character.item.name))
            else:
                print("%s named %s" % (currentnode.character.description, currentnode.character.name))
            clear_screen()
        else:
            print("There is nobady here")

    elif "directions" in command:
        print("You can go:\n")

        if currentnode.north is not None:
            print("North")
        if currentnode.south is not None:
            print("South")
        if currentnode.east is not None:
            print("East")
        if currentnode.west is not None:
            print("West")
        clear_screen()

    elif command == "look":
        if currentnode.item is not None:
            if currentnode.item.name[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                print("You see an %s in the room" % currentnode.item.name)
                clear_screen()
            else:
                print("You see a %s in the room" % currentnode.item.name)
                clear_screen()
        else:
            print("You see nothing out of the ordinary")
            clear_screen()

    elif command == "?":
        print("\"grab\", \"take\", \"pickup\", \"pick up\" : \nPicks up any item on the floor, or in a friendly "
              "character's inventory")
        print()
        print("\"bag\", \"inventory\", \"inv\", \"i\" : \nOpens up your bag / inventory")
        print()
        print("\"fight\", \"attack\" : \nInitiates an attack against an enemy")
        print()
        print("\"north\"(\"n\"), \"south\"(\"s\") , \"east\"(\"e\", \"west\"(\"w\" : "
              "\nMovement commands in the map that corrospond to direction")
        print()
        print("\"Description\" : \nIdentifies any characters in the room, as long as displays their "
              "description, name, and any items they may have")
        print("\"Directions\" : \nShows the possible movement commands from your current location on the map")
        print()
        print("\"Look\" : \nShows items in current room")
        clear_screen()

    elif command == "give":
        closealo = 0
        if closealo == 0:
            closealo += 1
            print("*Hint* (Opening your inventory brings you to this same process) ")
            clear_screen()
            inventory()
        else:
            inventory()

    else:
        print("Command not recognized")
