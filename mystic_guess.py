# Akinola Jonathan Oyerinsola
# 24/14642
# Software Engineering
import random

def get_valid_integer():
    """Helper to ensure user enters a number."""
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            return guess
        except ValueError:
            print("[!] Invalid input. Please enter a number.")

def config_difficulty():
    """Sets the max_lives based on user choice."""
    # Matches SDLC Phase 2: Modules
    print("\n--- DIFFICULTY SETTINGS ---")
    print("type 'easy' for 10 lives")
    print("type 'hard' for 5 lives")
    
    while True:
        choice = input("Choose difficulty: ").lower().strip()
        if choice == 'easy':
            return 10
        elif choice == 'hard':
            return 5
        else:
            print("Please type 'easy' or 'hard'.")

def start_engine():
    """The main game loop."""
    print("\n=== WELCOME TO MYSTIC NUMBER ===")
    
    # Matches SDLC Phase 2: State Variables
    current_lives = config_difficulty()
    hidden_target = random.randint(1, 100)
    
    print(f"\nI have selected a number between 1 and 100.")
    print(f"You have {current_lives} attempts to find it.\n")

    while current_lives > 0:
        # Input handling from Phase 3
        player_guess = get_valid_integer()
        
        # Logic Loop
        if player_guess == hidden_target:
            print(f"\n🎉 CORRECT! The number was {hidden_target}.")
            print(f"You won with {current_lives - 1} lives remaining!")
            return # End game on win

        elif player_guess < hidden_target:
            print("🔼 Too Low! Try higher.")
        else:
            print("🔽 Too High! Try lower.")

        # Decrement lives
        current_lives -= 1
        print(f"Lives remaining: {current_lives}")

    # End game on loss
    print(f"\n💀 GAME OVER. The number was {hidden_target}.")

if __name__ == "__main__":
    start_engine()
