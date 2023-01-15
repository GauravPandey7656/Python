# ROCK PAPER SCISSOR GAME
# Rock beats Scissors,Scissors beats Paper,Paper beats Rock
import random
user_input=input("Enter a choice:(rock,paper,scissor)")
possible_actions=['rock','paper','scissor']
computer_action=random.choice(possible_actions)

# print user action and computer action 

print("You choose:",user_input)
print("Computer chooses:",computer_action)

if (user_input==computer_action):
    print("It's a TIE!")
elif (user_input!=computer_action):
    if (user_input == "rock") and (computer_action == "paper"):
        print("You lose,Paper beats rock")
    elif (user_input == "rock") and (computer_action == "scissor"):
        print("You won,Rock beats Scissor")
    elif (user_input == "scissor") and (computer_action == "paper"):
        print("You won,Scissor beats Paper")
    elif (user_input == "scissor") and (computer_action == "rock"):
        print("You lose,Rock beats Scissor")
    elif (user_input == "paper") and (computer_action == "rock"):
        print("You won, Paper beats Rock")
    elif (user_input == "paper") and (computer_action == "scissor"):
        print("You lose,Scissor beats Paper")  
else:
    print("Invalid Input")      
            
