import random

def get_computer_choice():
    """Returns the computer's choice randomly."""
    choices = ['snake', 'water', 'gun']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    """Determines the winner based on the rules of the game."""
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'snake' and computer_choice == 'water') or \
         (player_choice == 'water' and computer_choice == 'gun') or \
         (player_choice == 'gun' and computer_choice == 'snake'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Main function to play the Snake, Water, Gun game."""
    print("Welcome to Snake, Water, Gun Game!")
    print("Rules: Snake beats Water, Water beats Gun, Gun beats Snake.")
    
    while True:
        # Get player's choice
        player_choice = input("\nChoose your move (snake/water/gun): ").lower()
        if player_choice not in ['snake', 'water', 'gun']:
            print("Invalid choice! Please choose either 'snake', 'water', or 'gun'.")
            continue
        
        # Get computer's choice
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

# Run the game
if __name__ == "__main__":
    play_game()