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
        global currentnode
        currentnode = globals()[getattr(self, direction)]


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
                      None, None, "yourhouse", "road", None, None, None)
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
playground = Place("playground", "you see a basketball court and a small playground to the right", None, "stonepath",
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
    print(currentnode.name)
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

