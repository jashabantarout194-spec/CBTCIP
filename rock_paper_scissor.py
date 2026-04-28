import random

def decide_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissor") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissor" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    choices = ["rock", "paper", "scissor"]
    print("Welcome to Rock-Paper-Scissors!")
    print("Winning Rules:")
    print("1. Rock vs Paper -> Paper wins")
    print("2. Rock vs Scissor -> Rock wins")
    print("3. Paper vs Scissor -> Scissor wins\n")

    player_choice = input("Enter your choice (rock/paper/scissor): ").lower()
    if player_choice not in choices:
        print("Invalid choice. Please select rock, paper, or scissor.")
        return

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    result = decide_winner(player_choice, computer_choice)
    print(result)

# Run the game
play_game()
