"""

- import statements
-class definitions
    -items
    -characters
    -rooms
-institution of classes
-controller

"""


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
        self.amor = armor


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
        print("You stab %s")


# Characters


class Character(object):
    def __init__(self, name, description, item, health, stats, armor=5):
        self.name = name
        self.description = description
        self.item = item
        self.health = health
        self.stats = stats
        self.armor = armor

    def takedamage(self, amount):
        dmg = amount - self.armor
        if dmg < 0:
            dmg = 0
            print("The attack was not very effective...")
        self.health -= dmg
        print("%s has %d hp left" % (self.name, self.health))

    def health1(self):
        pass

    def attack(self, target):
        print("%s attacks %s" % (self.name, target.name))
        target.takedamage(self.stats)
        print()


# steve = Character("Steve", "It's Steve", None, 100, 20, 10)
# enemy = Character("Enemy", "Enemy", None, 100, 10)
# steve.attack(enemy)
# enemy.attack(steve)
# rat = Character("Rat", "Smelly Sewer Rat", None, 20, 5, 0)
# gnome = Character("Underpants Gnome", "He gon take your underwear!", None, 50, 10, 5)
cartman = Character("Eric Cartman", "A fat kid your age, wearing a red coat and a blue poofball hood", None,
                    125, 20)
stan = Character("Stan Marsh", "A kid your age, wearing a brown coat with a blue hat", None, 100, 25)
kyle = Character("Kyle Broflovski", "A kid your age wearing a green coat with an orange hat", None, 100, 30)
kenny = Character("Kenny McCormick", "A kid your age wearing an orange coat with the hood covering most of his face",
                 "None", 85, 40)


# World Map


class Place(object):
    def __init__(self, name, description, north, south, east, west, enter, up, down):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.enter = enter
        self.up = up
        self.down = down

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


yourhouse = Place("Your House", "You see a bright red house", None, None, "randomtree", "southparksign",
                  "inside_yourhouse", None, None)
randomtree = Place("Random Tree", "You see a random tree", None, None, "buttershouse", "yourhouse",
                   "inside_buttershouse", None, None)
buttershouse = Place("Butters\'house", "You see a red brownish house", None, None, "cartmanshouse", "randomtree",
                     "inside_buttershouse", None, None)
cartmanshouse = Place("Cartman\'s house", "You see a bright green house", None, None, "stanshouse", "buddershouse",
                      "inside_cartmanshouse", None, None)
stanshouse = Place("Stan\'s house", "You see a dark green house", None, None, "kyleshouse", "cartmanshouse",
                   "insidestanshouse", None, None)
kyleshouse = Place("Kyle\'s house", "You see a moss green house", None, None, "stonepath", "stanshouse",
                   "insidekyleshouse", None, None)
stonepath = Place("Stone Path", "You see a paved path to your left leading to what looks like a park", "playground",
                  None, "traintracks", "kyleshouse", None, None, None)
traintracks = Place("Train Tracks", "You see train tracks almost hidden under a trick layer of snow", None, None,
                    "sodosopa", "stonepath", None, None, None)
sodosopa = Place("Sodosopa", "You see a broken down, olive green house, surrounded almost completely by what seems "
                             "to be a modernized restaurant",
                 None, None, None, "traintracks", "insidekennyshouse", "insidesodosopa", None)
southparksign = Place("SouthPark Sign", "You see a sign that says \"South Park\" \non your left lies a road\n"
                                        "beyond the road you see a bus stop",
                      None, None, "yourhouse", "busstop", None, None, None)
road = Place("Road", "A road blocks your path", None, None, "southparksign", "busstop", None, None, None)
busstop = Place("Bus Stop", "You see the local elementary school's bus stop", None, None, "road", "jimmyshouse",
                None, None, None)
jimmyshouse = Place("Jimmy\'s house", "You see a red house", None, None, "busstop", "craigshouse", "inside_jimmyshouse",
                    None, None)
craigshouse = Place("Craig\'s house", "You see a light brown house", None, None, "jimmyshouse", "clydeshouse",
                    "inside_craigshouse", None, None)
clydeshouse = Place("Clyde\'s house", "You see a dark brown house", None, None, "craigshouse", "bebeshouse",
                    "inside_clydeshouse", None, None)
bebeshouse = Place("Bebe\'s house)", "You see a red house", None, None, "clydeshouse", "communitycenter",
                   "insidebebeshouse", None, None)
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
playground = Place("playground", "you see a basketball court and a small playground to th right", None, None,
                   "alshouse", "tacoshop", "insideplayground", None, None)
alshouse = Place("Al\'s House", "You see a bright red house", "coffeeshop", None, None, "playground", "insidealshouse",
                 None, None)
coffeeshop = Place("Tweal Bro\'s Coffee", "You see a small tan building with a coffee sign", None, "alshouse", None,
                   "theatre", "insidecoffeeshop", None, None)
theatre = Place("Movie Theatre", "You see a large orange and red theatre", None, None, "coffeeshop", "tokenshouse",
                "insidetheatre", None, None)
tokenshouse = Place("Token\'s House", "You see a very large fenced-off light brown manor", None, None, "theatre",
                    "mall", "insidetokenshouse", None, None)
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


# Controller


directions = ("north", "south", "east", "west", "enter", "up", "down")
shortened = ("n", "s", "e", "w", "in", "u", "d")
currentnode = yourhouse
while True:
    print (currentnode.name)
    print(currentnode.description)
    command = input(">_").lower().strip()
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
    else:
        print("Command not recognized")
