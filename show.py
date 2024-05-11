import know as Know
import util as Util



def CharacterCreate(char, phase):

    # tell about each of the Races
    input(f"Enter a world of { Util.englishJoin(Util.getDisplay(Know.Race, False)) }. (press any key)") 
    for race in Know.Race:
        input(race["description"] + " (continue)")

    race = Util.inputValidateChoice("Are you a", Know.Race)
    char["race"] = race["id"]
    char["name"] = input("Enter character name: ")
    print(f"You are { char['name'] }, of the { Util.getDisplay(race, False) }.")

    Util.takeStep(char, phase)

def Main(char, phase):
    print("You are standing in the main room")
    Util.takeStep(char, phase)

def Cave(char, phase):
    print("You stand in a massive cavern. Its too dark to continue")
    Util.takeStep(char, phase)

def Attic(char, phase):
    print("You make your way to the attic. while dim and dusty, a beam of light streams in from a window.")
    Util.takeStep(char, phase)

def Quit(char, phase):

    print("quitting")

    return "exit"