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
    """
    Use an object's (or array of objects') `display` property to get a display name.
    If `display` is an array, use the first item if singular, the 2nd if plural.
    If there's only one item in the array, use that word for all cases.
    If `display` is a *string*, return that for singular or automatically add an `s` at the end for plural
    """

    if type(obj) == list:
        output = []
        for item in obj:
            output.append(getDisplay(item, singular))
        return output

    field = obj["display"]
    fieldType = type(obj["display"])
    if fieldType == list:
        count = len(field)
        if count == 1:
            return field[0]
        else:
            return field[0] if singular else field[1]
    else:
        return field+("s" if not singular else "")

def inputValidateChoice(message, items, singular=True, doubleCheck=True):
    """
    Let the user select from an array of *objects* using number keys.
    Returns the users final selection (the object from the list).
    You can optionally `doubleCheck=True` to add a confimration message
    """
    options = []
    for (i, item) in enumerate(items):
        options.append(f"({ (i+1) }){getDisplay(item, singular)}")

    choice = input(f"{message} {englishJoin(options, False)} ?")
    try:
        choiceInt = int(choice)
        choiceObject = items[choiceInt-1]
        choiceName = getDisplay(choiceObject, singular)
        finalMessage = f"You chose {choiceName}."
        if doubleCheck :
            confirm = input(finalMessage + " Are you sure? (y/n)").lower()
            if confirm[0] == "y":
                print(f"You settle on {choiceName}.")
                return choiceObject
            else:
                inputValidateChoice(message, items, singular, doubleCheck)
        else:
            print(finalMessage)
        return choiceObject
    except:
        print("Please select one of the options")
        inputValidateChoice(message, items, singular, doubleCheck)


def englishJoin(parts, inclusive=True):
    """ Turn an array into normal oxford comma plain text """
    word = "and" if inclusive else "or"
    count = len(parts)
    if count < 2:
        return "".join(parts)
    if count < 3:
        return (" "+ word +" ").join(parts)
    else:
        return ", ".join(parts[:-1]) + ", " + word + " " + parts[-1]


def Create():
    
    player = {
        "name": "",
        "race": "",
        "class": "",
        "spec": ""
    }

    # tell about each of the Races
    input(f"Enter a world of { englishJoin(getDisplay(Races, False)) }. (press any key)") 
    for race in Races:
        input(race["description"] + " (continue)")

    race = inputValidateChoice("Are you a", Races, doubleCheck=True)
    player["race"] = race["id"]

    player["name"] = input("Enter character name: ")

    print(f"You are { player['name'] }, of the { getDisplay(race, False) }.")
    return player


if __name__ == "__main__":
    Create()
