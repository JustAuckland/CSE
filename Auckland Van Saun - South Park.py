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


steve = Character("Steve", "It's Steve", None, 100, 20, 10)
enemy = Character("Enemy", "Enemy", None, 100, 10)
steve.attack(enemy)
enemy.attack(steve)
rat = Character("Rat", "Smelly Sewer Rat", None, 20, 5, 0)
gnome = Character("Underpants Gnome", "He gon take your underwear!", None, 50, 10, 5)


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
                                        "beyond road you see a bus stop",
                      None, None, "yourhouse", "busstop", None, None, None)
road = Place("Road", "A road blocks your path", None, None, "southparksign", "busstop", None, None, None)
busstop = Place("Bus Stop", "You see the local elementary school's bus stop", None, None, "road, ")
jimmyshouse = Place("Jimmy\'s house", "You see a red house", None, None, "busstop", "craigshouse", "insidejimmyshouse",
                    None, None)
