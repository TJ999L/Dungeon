from know import Race as Races
import util as Util

def CharacterCreate(char, phase):

    # tell about each of the Races
    input(f"Enter a world of { Util.englishJoin(Util.getDisplay(Races, False)) }. (press any key)") 
    for race in Races:
        input(race["description"] + " (continue)")

    race = Util.inputValidateChoice("Are you a", Races, doubleCheck=True)
    char["race"] = race["id"]
    char["name"] = input("Enter character name: ")
    print(f"You are { char['name'] }, of the { Util.getDisplay(race, False) }.")

    choice = Util.inputValidateChoice("what next", phase["step"])
    char["phase"] = choice["id"]


def Quit(char, phase):

    print("quitting")

    return "exit"