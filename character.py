
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
        "display": ["Melee"],
    },
    {
        "id": "ran",
        "display": ["Ranged"],
    },
    {
        "id": "mag",
        "display": ["Magic"],
    }
]

Specs = [
    {
        "id": "bar",
        "id_class": "mel",
        "display": ["Barbarian"]
    },
    {
        "id": "war",
        "id_class": "mel",
        "display": ["Warrior"]
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



def Create():
    
    player = {
        "name": "",
        "race": "",
        "class": "",
        "spec": ""
    }


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

    input(f"Enter a world of {englishJoin(collectField(Races, lambda race: race["display"][1]))}. (press any key)") 

    for race in Races:
        input(race["description"] + "(continue)")

    message = "Are you a "
    for (i, race) in enumerate(Races):
        message += f"({ (i+1) }){race["display"][0]} "

    index = int(input(message)) - 1
    race = Races[index]
    player["race"] = race["id"]

    player["name"] = input("Enter character name: ")

    print(f"You are {player["name"]}, of the {race["display"][1]}.")
    input("Enter character name: ")

    return player


if __name__ == "__main__":
    Create()
