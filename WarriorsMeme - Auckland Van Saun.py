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
            "WEST": "TWOLEGROAD1"
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
            "EAST": "NETALLPINES",
            "NORTH": "TWOLEGROAD6",
            "SOUTH": "TWOLEGROAD4"
        }
    },
    "TWOLEGROAD6": {
        "NAME": "TWOLEG ROAD",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "EAST": "TWOLEGROAD",
            "NORTH": "TWOLEGROAD3",
            "SOUTH": "TWOLEGROAD5"
        }
    },
    "TWOLEGROAD7": {
        "NAME": "TWOLEG ROAD",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "EAST": "TWOLEGROAD7",
            "NORTH": "SANDYHOLLOW",
            "WEST": "TWOLEGROAD2",
            "SOUTH": "NETALLPINES"
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
            "EAST": "TWOLEGROAD",
            "NORTH": "TWOLEGROAD4",
            "WEST": "TWOLEGROAD3"
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
    "TREECUTPLACE": {
        "NAME": "TREECUT PLACE",
        "DESCRIPTION": "Insert desciption here",
        "PATHS": {
            "EAST": "TWOLEGROAD3",
        }
    }
}

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
