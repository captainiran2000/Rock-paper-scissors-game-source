import random
choices = ["Rock", "Paper", "Scissors"]
print("Welcome to Rock, Paper, Scissors!")
print("Choose one of the following: Rock, Paper, or Scissors.")

rounds = 3
player_score = 0
computer_score = 0

for round in range(1, rounds + 1):
    print(f"\nRound {round}/{rounds}:")
    
    player_choice = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()
    
    if player_choice not in choices:
        print("Invalid choice! Please choose Rock, Paper, or Scissors.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Scissors" and computer_choice == "Paper") or \
         (player_choice == "Paper" and computer_choice == "Rock"):
        print(f"You win this round! {player_choice} beats {computer_choice}.")
        player_score += 1
    else:
        print(f"You lose this round! {computer_choice} beats {player_choice}.")
        computer_score += 1

print(f"\nFinal Score: You {player_score} - {computer_score} Computer")

if player_score > computer_score:
    print("Congratulations! You won the game!")
elif player_score < computer_score:
    print("Sorry! You lost the game. Better luck next time!")
else:
    print("It's a draw! Well played!")
