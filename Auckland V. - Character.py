"""
Name
Description
Dialogue?
Inventory
Interact
Move?
Climb
Look
Item
Fight
Health
takeDamage
Death
Stats
"""


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
rat.attack(gnome)
gnome.attack(rat)
