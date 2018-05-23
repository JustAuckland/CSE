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
        print("You stab %s")


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
