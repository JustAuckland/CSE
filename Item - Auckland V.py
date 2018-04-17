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


