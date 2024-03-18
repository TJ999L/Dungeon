def main():
    last_response = ""

    try:
        while True:
            # Clear the screen
            print("\033[H\033[J")
            
            # Print previous response
            if last_response:
                print("Last response:", last_response)

            # Get user input
            user_input = input("Enter your message: ")

            # Update last_response
            last_response = user_input

    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
