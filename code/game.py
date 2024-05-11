import os

def load_player_data(gamer_folder_path, character_name):
    player_file = os.path.join(gamer_folder_path, f"{character_name}.txt")
    if os.path.exists(player_file):
        with open(player_file, 'r') as file:
            player_data = file.readlines()
            return [data.strip() for data in player_data]
    else:
        print(f"Player file '{player_file}' not found.")
        return None

def print_character_data(character_data):
    print(f"                                           ")
    print(f"For profile {character_data[0]}")
    print(f"                                           ")
    print(f" -`♡´- {character_data[1]} -`♡´-  ")
    print(f"Player Race     🗺 : { character_data[2]}")
    print(f"Player Category 🤹 : { character_data[3]}")
    print(f"Player Class    🏛 : { character_data[4]}")
    print(f"Weapon Skill    ⚔: : { character_data[5]}")


def save_player_data(gamer_folder_path,  data):
    player_file = os.path.join(gamer_folder_path, f"{data[1]}.txt")
    with open(player_file, 'w') as file:
        for line in data:
            file.write(line + '\n')

def create_new_character(gamer_tag):

    character_name = input("Enter character name: ")
    player_race = input("Are you a human, dwarf, or elf? (human/dwarf/elf): ").lower()
    player_category = input(f"Is your {player_race} a ranged {player_race} or a close combat {player_race}? (ranged/close_combat): ").lower()
    if player_category == "close_combat":
        player_class = input("Are you a barbarian with increased attack power and less intelligence, a warrior with balanced stats, or a rogue with increased intelligence and less attack power? (barbarian/warrior/rogue): ").lower()
        if player_class == "barbarian":
            weapon_skill = input(f"Will your {character_name} be skilled with axes, swords, or hammers? (axes/swords/hammers): ").lower()
        elif player_class == "warrior":
            weapon_skill = input(f"Will your {character_name} be skilled with longswords, swords, or daggers? (longswords/swords/daggers): ").lower()
    elif player_category == "ranged":
        player_class = input(f"Are you an archer with increased intelligence and less attack power or a dead shot with increased attack power and less intelligence? (archer/dead shot): ").lower()
        if player_class == "archer":
            weapon_skill = input(f"Will your {character_name} be skilled with longbows, throwing daggers, or shortbows? (longbows/throwing daggers/shortbows): ").lower()
        elif player_class == "dead shot":
            weapon_skill = input(f"Will your {character_name} be skilled with crossbows, slings, or magic bows? (crossbows/slings/magic bows): ").lower()

    return [gamer_tag, character_name, player_race, player_category, player_class, weapon_skill]

def main():
    #------------get the current directory and find the profiles folder---------------
    # get working directory
    wdir = os.path.dirname(os.path.abspath(__file__))
    # create reference to profiles folder
    profiles_folder_path = os.path.join(wdir, "profiles")
    # Check if "profiles" folder exists
    if not os.path.exists(profiles_folder_path):
        # If it doesn't exist, create it
        os.makedirs(profiles_folder_path)


    # ---------------retrieve or setup new game---------------------------------
    while True:
        gamer_tag = input("Please enter your gamer tag: ")
        answer = input(f"Is '{gamer_tag}' your gamer tag? (yes/no): ").lower()
        if answer.startswith('y'):
            print("Gamer tag verified.")
            break
        elif answer.startswith('n'):
            print("Please re-enter your gamer tag.")
        else:
            print("Sorry, response must be yes or no.")

    # get gamer profiles location
    gamer_folder_path = os.path.join(profiles_folder_path, gamer_tag)
    if os.path.exists(gamer_folder_path):
        print(f"Found existing profile for '{gamer_tag}'.")
        # Do something with the existing folder
    else:
        print(f"No profile found for '{gamer_tag}'. Creating one...")
        os.makedirs(gamer_folder_path)

    #--------------get number of character files--------------------------------
    character_files = os.listdir(gamer_folder_path)
    num_characters = len(character_files)

    # Print names of each character found, if they exist
    if num_characters == 0:
        how_many = int(input(f"No characters found for '{gamer_tag}'. How many do you want to create?"))
        for i in range(how_many):
            print(f"Creating {i + 1} character(s):")
            character_data = create_new_character(gamer_tag)
            save_player_data(gamer_folder_path, character_data)
            print_character_data(character_data)
    else:
        print(f"{num_characters} characters found for '{gamer_tag}':")

    while True:
        dowhat = input(f"so you have {num_characters} setup, what do you want to do? [ ADD(a) SHOW(s) SELECT(t)]")
        if dowhat == "a":
            character_data = create_new_character(gamer_tag)
            print(character_data)
            save_player_data(gamer_folder_path, character_data)
        elif dowhat == "s":
            for character_file in character_files:
                # Extract character name from the file name
                character_name = os.path.splitext(character_file)[0]
                print(f"Loading character: {character_name}")
                
                # Load character data
                character_data = load_player_data(gamer_folder_path, character_name)
                
                # Check if character data is loaded successfully
                if character_data is not None:
                    # Process or use character data here
                    print_character_data(character_data)
                else:
                    print(f"Failed to load character data for '{character_name}'")
        elif dowhat == "t":
            chose = input("which character do you want to use?")
            break



    #-------------decide which character to play with----------------------------

    #--------------initiate story-----------------------------------------------------
    #----------- Continue with your story or additional code here-----------------
    print("You wake up on a shore not remebering anything")
    player_option1 = input("You see a small hut with the smell of food making you start to feel hungery. Or their is a nearby cave that might have food. What do you do? [ GO TO HUT(h) GO TO CAVE(c)]")
    if player_option1 == "c":
        print(f"{gamer_tag} walks over to the cave and finds nothing.")

    #elif player_option1 == "h":
        print("You walk over to the hut and knock on the door.")
    else:
        print("That is not an option") 
    print("A man awnsers the door and tells you to come in. You decide to listen to him and you enter his cozy house.")
    print("The man then tells you were you are. He says that you are in a empire called Trellon. He then asks what side you are on and you say that you remember nothing since before you crashed.")
    print("The man tells you about what is going on. He says that there is a rebellion and that they are fighting for a new empire were all are equal. He then states that the empire is trying to find all who disagree with the rebellion and either throw them in the dungeon or murder them.") 
    player_side = input("Later that night 🌙 you remember one of the sides sent you. Which one was it? [ EMPIRE(e) REBELS(e)]")
    if player_side == "e":
        ("")

if __name__ == "__main__":
    main()
