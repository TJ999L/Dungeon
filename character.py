Races = [
    {
        "id": "hum",
        "display": ["Human", "Humans"],
        "description": "Inventive and optimistic, Humans will find a way through any situation",
        "stats": {}
    },
    {
        "id": "elf",
        "display": ["Elf", "Elves"],
        "description": "Aloof and unchanging, the Elves keep to themselves and their elegant traditions"
    },
    {
        "id": "dwa",
        "display": ["Dwarf", "Dwarves"],
        "description": "Industrious and contentous, Dwarves use brute strength in their inevitable conflicts"
    }
]

Classes = [
    {
        "id": "mel",
        "display": ["Melee", "Melee Fighters"],
    },
    {
        "id": "ran",
        "display": ["Ranged", "Ranged Fighters"],
    },
    {
        "id": "mag",
        "display": ["Magic", "Magic Users"],
    }
]

Specs = [
    {
        "id": "bar",
        "id_class": "mel",
        "display": ["Barbarian", "Barbarians"]
    },
    {
        "id": "war",
        "id_class": "mel",
        "display": ["Warrior", ]
    },
    {
        "id": "rog",
        "id_class": "mel",
        "display": ["Rogue"]
    },
    {
        "id": "arc",
        "id_class": "ran",
        "display": ["Archer"]
    },
    {
        "id": "hun",
        "id_class": "ran",
        "display": ["Hunter"]
    }
]

Weapons = [
    {
        "id": "axe",
        "display": ["Axe"],
        "description": "",
        "ids_spec": ["bar"]
    },
    {
        "id": "swo",
        "display": ["Sword"],
        "description": "",
        "ids_spec": ["bar", "war", "rog"]
    },
    {
        "id": "ham",
        "display": ["Hammer"],
        "description": "",
        "ids_spec": ["bar"]
    },

    {
        "id": "lon",
        "display": ["Longbow"],
        "description": "",
        "ids_spec": ["bar"]
    },
    {
        "id": "dag",
        "display": ["Dagger"],
        "description": "",
        "ids_spec": ["rog", "bar"]
    }
]



def getDisplay(obj, singular=True):
    field = obj["display"]
    fieldType = type(obj["display"])
    if fieldType == list:
        count = len(field)
        if count == 1:
            return field[0]
        else:
            return field[0] if singular else field[1]
    else:
        return field+"s"

def getDisplaySingular(obj):
    return getDisplay(obj, True)

def getDisplayPlural(obj):
    return getDisplay(obj, False)

def inputValidateChoice(message, items, singular=True):
    options = []
    for (i, item) in enumerate(items):
        options.append(f"({ (i+1) }){getDisplay(item, singular)}")

    query = f"{message} {englishJoin(options, False)} ?"

    choice = input(query)
    try:
        choiceInt = int(choice)
        lookup = items[choiceInt]
        return lookup
    except:
        print("Please select one of the options")
        inputValidateChoice(message, items, singular)
    
def collectField(parts, extractor):
    """ Iterate over an array of objects, returning a new array of fields returned by the extractor function """
    output = []
    for part in parts:
        output.append(extractor(part))
    return output

def englishJoin(parts, inclusive=True):
    """ Turn an array into normal oxford comma text """
    word = "and" if inclusive else "or"
    if len(parts) < 3:
        return (" "+ word +" ").join(parts)
    else:
        return ", ".join(parts[:-1]) + ", " + word + " " + parts[-1]



# def Create():
#     
#     player = {
#         "name": "",
#         "race": "",
#         "class": "",
#         "spec": ""
#     }
# 
#     input(f"Enter a world of {englishJoin(collectField(Races, getDisplayPlural))}. (press any key)") 
# 
#     for race in Races:
#         input(race["description"] + "(continue)")
# 
#     message = "Are you a "
#     for (i, race) in enumerate(Races):
#         message += f"({ (i+1) }){race["display"][0]} "
# 
#     index = int(input(message)) - 1
#     race = Races[index]
#     player["race"] = race["id"]
# 
#     player["name"] = input("Enter character name: ")
# 
#     print(f"You are {player["name"]}, of the {race["display"][1]}.")
#     input("Enter character name: ")
# 
#     return player


if __name__ == "__main__":
    inputValidateChoice("Choose your race", Races)
