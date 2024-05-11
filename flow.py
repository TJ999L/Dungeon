import json
import know as Know
import show as Show

Phases = {}
Char = {}

def StateLoad():
    global Phases
    global Char
    with open('./state/phases.json', 'r') as f:
        Phases = json.load(f)

    with open('./state/character.json', 'r') as f:
        Char = json.load(f)

def StateSave():
    global Phases
    global Char
    with open('./state/phases.json', 'w') as f:
        json.dump(Phases, f)

    with open('./state/character.json', 'w') as f:
        json.dump(Char, f)

def lookup(list, id):
    for item in list:
        if item["id"] == id:
            return item
    return False

def update():
    phase = lookup(Phases, Char["phase"])
    render = getattr(Show, phase["show"])
    result = render(Char, phase)

    StateSave()

    if result:
        exit()
    else:
        update()


StateLoad()
update()