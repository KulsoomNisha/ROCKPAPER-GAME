import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    scores = {"user": 0, "ai": 0}
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors (or type 'exit' to quit): ").lower()
        if user_choice == "exit":
            break
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        
        ai_choice = random.choice(choices)
        print(f"AI chose: {ai_choice}")
        
        if user_choice == ai_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and ai_choice == "scissors") or \
             (user_choice == "scissors" and ai_choice == "paper") or \
             (user_choice == "paper" and ai_choice == "rock"):
            print("You win this round!")
            scores["user"] += 1
        else:
            print("AI wins this round!")
            scores["ai"] += 1
        
        print(f"Scores -> You: {scores['user']}, AI: {scores['ai']}")
    
    print("Game over! Final Scores:")
    print(f"You: {scores['user']} | AI: {scores['ai']}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
