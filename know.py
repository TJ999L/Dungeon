Race = [
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
Role = [
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
Spec = [
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
Weap = [
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
