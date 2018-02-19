world_map = {
    "TWOLEGPLACE": {
        "NAME": "TWOLEG PLACE",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "NORTH": "TWOLEGROAD",
        }
    },
    "TWOLEGROAD": {
        "NAME": "TWOLEG ROAD",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "SOUTH": "TWOLEGPLACE",
            "NORTH": "LOGS",
            "EAST": "TALLPINES",
            "WEST": "NORTH1"
        }
    },
    "TWOLEGROAD1": {
        "NAME": "TWOLEG ROAD",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "EAST": "TWOLEGROAD",
            "NORTH": "TWOLEGROAD3",
            "WEST": "TWOLEGROAD2"
        }
    },
    "TWOLEGROAD2": {
        "NAME": "TWOLEG ROAD",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "EAST": "TWOLEGROAD1",
        }
    },
    "TWOLEGROAD3": {
        "NAME": "TWOLEG ROAD",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "SOUTH": "TWOLEGROAD1",
            "WEST": "TREECUTPLACE",
            "EAST": "LOGS",
            "NORTH": "RIVERSIDE"
        }
    },
    "TWOLEGROAD4": {
        "NAME": "TWOLEG ROAD",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "EAST": "TALLPINES",
            "NORTH": "TWOLEGROAD5",
            "WEST": "RIVERSIDE",
            "SOUTH": "LOGS"
        }
    },
    "TWOLEGROAD5": {
        "NAME": "TWOLEG ROAD",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "EAST": "NWTALLPINES",
            "NORTH": "TWOLEGROAD6",
            "SOUTH": "TWOLEGROAD4"
        }
    },
    "TWOLEGROAD6": {
        "NAME": "TWOLEG ROAD",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "EAST": "TWOLEGROAD7",
            "SOUTH": "TWOLEGROAD5"
        }
    },
    "TWOLEGROAD7": {
        "NAME": "TWOLEG ROAD",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "EAST": "TWOLEGROAD8",
            "NORTH": "GREATSYCAMORE",
            "WEST": "TWOLEGROAD6",
            "SOUTH": "NWTALLPINES"
        }
    },
    "TWOLEGROAD8": {
        "NAME": "TWOLEG ROAD",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "NORTH": "SNAKEROCKS",
            "WEST": "TWOLEGROAD7"
        }
    },
    "LOGS": {
        "NAME": "PILE OF LOGS",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "NORTH": "TWOLEGROAD4",
            "WEST": "TWOLEGROAD3",
            "SOUTH": "TWOLEGROAD"
        }
    },
    "TALLPINES": {
        "NAME": "TALLPINES",
        "DESCRIPTION": "Insert desciption here",
        "PATHS": {
            "SOUTH": "TWOLEGROAD",
            "WEST": "TWOLEGROAD4",
            "NORTH": "NTALLPINES"
        }
    },
    "RIVERSIDE": {
        "NAME": "RIVERSIDE",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "EAST": "TWOLEGROAD4",
            "SOUTH": "TWOLEGROAD3",
            "NORTH": "RIVERSIDE1"
        }
    },
    "NTALLPINES": {
        "NAME": "NORTH TALLPINES",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "WEST": "NWTALLPINES",
            "SOUTH": "TALLPINES"
        }
    },
    "NWTALLPINES": {
        "NAME": "NORTH-WEST TALPINES",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "EAST": "NTALLPINES",
            "NORTH": "TWOLEGROAD7",
            "WEST": "TWOLEGROAD5"
        }
    },
    "SANDYHOLLOW": {
        "NAME": "SANDY HOLLOW",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "EAST": "GREATSYCAMORE",
            "SOUTH": "RIVERSIDE4",
            "WEST": "RIVERSIDE5"
        }
    },
    "GREATSYCAMORE": {
        "NAME": "GREAT SYCAMORE",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "EAST": "SNAKEROCKS",
            "NORTH": "THUNDERCLANCAMP",
            "WEST": "SANDYHOLLOW",
            "SOUTH": "TWOLEGROAD7"
        }
    },
    "SNAKEROCKS": {
        "NAME": "SNAKEROCKS",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "WEST": "GREATSYCAMORE",
            "SOUTH": "TWOLEGROAD8"
        }
    },
    "THUNDERCLANCAMP": {
        "NAME": "THUNDERCLAN CAMP",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "SOUTH": "GREATSYCAMORE"
        }
    },
    "RIVERSIDE1": {
        "NAME": "RIVERSIDE",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "WEST": "RIVERSIDE2",
            "SOUTH": "RIVERSIDE"
        }
    },
    "RIVERSIDE2": {
        "NAME": "RIVERSIDE",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "EAST": "RIVERSIDE1",
            "WEST": "SUNNINGROCKS"
        }
    },
    "RIVERSIDE3": {
        "NAME": "RIVERSIDE",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "EAST": "RIVERSIDE4",
            "SOUTH": "SUNNINGROCKS"
        }
    },
    "RIVERSIDE4": {
        "NAME": "RIVERSIDE",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "NORTH": "SANDYHOLLOW",
            "WEST": "RIVERSIDE3",
        }
    },
    "SUNNINGROCKS": {
        "NAME": "SUNNINGROCKS",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "EAST": "RIVERSIDE2",
            "NORTH": "RIVERSIDE3",
            "WEST": "RIVERSIDE6",
            "SOUTH": "RIVERSIDE7"
        }
    },
    "RIVERSIDE5": {
        "NAME": "RIVERSIDE",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "EAST": "SANDYHOLLOW",
            "WEST": "TWOLEGPATH4"
        }
    },
    "RIVERSIDE6": {
        "NAME": "RIVERSIDE",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "EAST": "SUNNINGROCKS",
            "WEST": "TWOLEGPATH2"
        }
    },
    "RIVERSIDE7": {
        "NAME": "RIVERSIDE",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "NORTH": "SUNNINGROCKS",
            "SOUTH": "HILL"
        }
    },
    "HILL": {
        "NAME": "HILL",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "NORTH": "RIVERSIDE7",
            "WEST": "HILL1"
        }
    },
    "HILL1": {
        "NAME": "HILL",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "EAST": "HILL",
            "WEST": "RIVERCLANCAMP"
        }
    },
    "RIVERCLANCAMP": {
        "NAME": "RIVERCLAN CAMP",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "EAST": "HILL1",
            "NORTH": "TWOLEGPATH"
        }
    },
    "TWOLEGPATH": {
        "NAME": "TWOLEG PATH",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "NORTH": "TWOLEGPATH1",
            "SOUTH": "RIVERCLANCAMP"
        }
    },
    "TWOLEGPATH1": {
        "NAME": "TWOLEG PATH",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "NORTH": "TWOLEGPATH2",
            "SOUTH": "TWOLEGPATH"
        }
    },
    "TWOLEGPATH2": {
        "NAME": "TOLEG PATH",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "NORTH": "TWOLEGBRIDGE",
            "SOUTH": "TWOLEGPATH1"
        }
    },
    "TWOLEGPATH3": {
        "NAME": "TWOLEG PATH",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "NORTH": "TWOLEGPATH4",
            "SOUTH": "TWOLEGBRIDGE"
        }
    },
    "TWOLEGPATH4": {
        "NAME": "TWOLEG PATH",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "EAST": "RIVERSIDE5",
            "NORTH": "TWOLEGPATH5",
            "SOUTH": "TWOLEGPATH3"
        }
    },
    "TWOLEGPATH5": {
        "NAME": "TWOLEG PATH",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "EAST": "OWLTREE",
            "SOUTH": "TWOLEGPATH4"
        }
    },
    "OWLTREE": {
        "NAME": "OWLTREE",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "WEST": "TWOLEGPATH5"
        }
    },
    "TWOLEGBRIDGE": {
        "NAME": "TWOLEG BRIDGE",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "NORTH": "TWOLEGPATH3",
            "SOUTH": "TWOLEGPATH2"
        }
    },
    "TREECUTPLACE": {
        "NAME": "TREECUT PLACE",
        "DESCRIPTION": "Insert desciption here",
        "PATHS": {
            "EAST": "TWOLEGROAD3",
        }
    }
}
"""
    "": {
        "NAME": "",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "EAST": "",
            "NORTH": "",
            "WEST": "",
            "SOUTH": ""
        }
    },
"""
current_node = world_map["TWOLEGPLACE"]
directions = ["NORTH", "SOUTH", "EAST", "WEST"]

while True:
    print(current_node["NAME"])
    print(current_node["DESCRIPTION"])
    command = input(">_")
    if command == "quit":
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node["PATHS"][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go that way")
    else:
        print("Command not recognized")
    print()
