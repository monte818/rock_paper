import random


probabilites = ["Rock", "Paper", "Scissors"]
score = 0
games_played = 0
comp_score = 0

while True:
    user_action = input("Lets play rock paper scissors Type (rock,paper,scissors) or quit to stop ")
    comp_answ = random.choice(probabilites)
    
    if user_action.lower() == "rock":
        games_played += 1
        print(f"I choose {comp_answ}")
        if comp_answ == "Scissors":
            print("nice you win")
            score += 1
        elif comp_answ == "Rock":
            print("you tied")
        elif comp_answ == "Paper":
            print("you Lose")
            comp_score += 1
    elif user_action.lower() == "scissors":
        games_played += 1
        print(f"I choose {comp_answ}")
        if comp_answ == "Rock":
            print("you lost that one")
            comp_score += 1
        elif comp_answ == "Paper":
            print("Nice you won that round")
            score += 1
        elif comp_answ == "Scissors":
            print("we tied thats ok")
    elif user_action.lower() == "paper":
        games_played += 1
        print(f"I choose {comp_answ}")
        if comp_answ == "Rock":
            print("Nice you won that round")
            score += 1
        elif comp_answ == "Paper":
            print("we tied thats ok") 
        elif comp_answ == "Scissors":
             print("you lost that one loser")
             comp_score += 1      
    elif user_action.lower() == "quit":
        break


print(f"nice you got {score} out of {games_played}")
print(f"I got {comp_score} out of {games_played}")

