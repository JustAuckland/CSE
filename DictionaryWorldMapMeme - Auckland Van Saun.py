word_map = {
    "WESTHOUSE": {
        "NAME": "WESTHOUSE",
        "DESCRIPTION": "You are west of a small house",
        "PATHS": {
            "NORTH": "NORTHOUSE",
            "SOUTH": "SOUTHHOUSE"
        }
    },
    "NORTHHOUSE": {
        "NAME": "NORTH OF HOUSE",
        "DESCRPTION": "Insert desciption here",
        "PATHS": {
            "WEST": "WESTHOUSE"
        }
    },
    "SOUTHHOUSE": {
        "NAME": "SOUTH OF HOUSE",
        "DESCRIPTION": "Insert desciption here",
        "PATHS": {
            "WEST": "WESTHOUSE"
        }
    }
}

current_node = word_map["WESTHOUSE"]
print(current_node["NAME"]["DESCRIPTION"])
