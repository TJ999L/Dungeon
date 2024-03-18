import os

def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    history_line = ''  # Initialize the history line
    
    while True:
        clear_screen()  # Clear the screen before prompting for input
        
        # Print the history line at the top
        print(history_line)
        
        user_input = input('> ')  # Prompt the user for input
        
        # Process user input
        if user_input.lower() == 'exit':
            break
        else:
            # Update the history line with multiple lines
            history_line = f"You entered:\n{user_input}"  
            # Adjust the height of the history line if necessary
            num_lines = history_line.count('\n') + 1
            history_line += '\n' * (2 - num_lines)  # Adjust to ensure only one line is shown

if __name__ == "__main__":
    main()
