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

class Characters(object):
    def __init__(self, description, interact, item, health, stats):
        self.description = "description"
        self.interact = "interact"
        self.item = "item"
        self.health = "health"
        self.stats = "stats"


    def takeDamage(self, amount):
        health =- amount

    def fight(self, target):

    def give(self):
