import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]
#options[o] will give first element in list. change number and it goes to next item


while True:
    user_input = input("Type Rock/Paaper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue#takes them to type correct keys

    random_number = random.randint(0 , 2)
    #rock: 0, paper: 1 , scissors: 2
    computer_pick = options[random_number]
    print("Computer picked ",computer_pick + ".")#a comma automatically adds spacing

    if user_input == "rock" and computer_pick == "scissors":#and ckecks if both statements are true
        print("You Won!!")
        user_wins += 1
        

    elif user_input == "paper" and computer_pick == "rock":#and ckecks if both statements are true
        print("You Won!!")
        user_wins += 1
        

    elif user_input == "scissors" and computer_pick == "paper":#and ckecks if both statements are true
        print("You Won!!")
        user_wins += 1

    else:
        print("You Lost!!")
        computer_wins += 1

print("You won", user_wins,"times.")
print("The computer won", computer_wins,"times.")
        
print("GoodBye")
