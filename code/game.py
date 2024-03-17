import os

def load_player_data(player_name, character_name):
    player_file = f"{player_name}_{character_name}.txt"
    if os.path.exists(player_file):
        with open(player_file, 'r') as file:
            player_data = file.readlines()
            return [data.strip() for data in player_data]
    else:
        print(f"Player file '{player_file}' not found.")
        return None

def save_player_data(player_name, character_name, data):
    player_file = f"{player_name}_{character_name}.txt"
    with open(player_file, 'w') as file:
        for line in data:
            file.write(line + '\n')

def create_new_character(player_name):
    character_name = input("Enter character name: ")
    loaded_data = load_player_data(player_name, character_name)
    if loaded_data:
        print("Loading existing character data...")
        return loaded_data
    else:
        print("Creating new character...")
        gamer_tag = input("Please enter your gamer tag: ")
        answer = input(f"So your gamer tag is {gamer_tag}? (yes/no) ")

        #-------------------- get feedback on gamer tag---------------------------
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

        #---------------------- proceed with game ---------------------------------
        print(f"Hello {gamer_tag}")
        player_race = input("Are you a human, dwarf, or elf? (human/dwarf/elf): ").lower()
        player_category = input(f"Is your {player_race} a ranged {player_race} or a close combat {player_race}? (ranged/close combat): ").lower()
        if player_category == "close combat":
            player_class = input("Are you a barbarian with increased attack power and less intelligence, a warrior with balanced stats, or a rogue with increased intelligence and less attack power? (barbarian/warrior/rogue): ").lower()
            if player_class == "barbarian":
                weapon_skill = input(f"Will your {gamer_tag} be skilled with axes, swords, or hammers? (axes/swords/hammers): ").lower()
            elif player_class == "warrior":
                weapon_skill = input(f"Will your {gamer_tag} be skilled with longswords, swords, or daggers? (longswords/swords/daggers): ").lower()
        elif player_category == "ranged":
            player_class = input(f"Are you an archer with increased intelligence and less attack power or a dead shot with increased attack power and less intelligence? (archer/dead shot): ").lower()
            if player_class == "archer":
                weapon_skill = input(f"Will your {gamer_tag} be skilled with longbows, throwing daggers, or shortbows? (longbows/throwing daggers/shortbows): ").lower()
            elif player_class == "dead shot":
                weapon_skill = input(f"Will your {gamer_tag} be skilled with crossbows, slings, or magic bows? (crossbows/slings/magic bows): ").lower()

    return [gamer_tag, player_race, player_category, player_class, weapon_skill]

def main():
    player_name = input("Enter player name: ")
    characters = int(input("How many characters do you want to create?: "))
    for i in range(characters):
        print(f"Creating character {i + 1}...")
        character_data = create_new_character(player_name)
        save_player_data(player_name, f"character_{i + 1}", character_data)
    # Continue with your story or additional code here
    print("You wake up on a shore not remebering anything")
    player_option1 = input("You see a small hut with the smell of food making you start to feel hungery. Or their is a nearby cave that might have food. What do you do? (walk over/go to cave)")

if __name__ == "__main__":
    main()