import random

#r = random.randrange(51)#this does not include 51
#print(r)
#Alternatively random.randrange(start,end)
#if you want to include the number use random.randint(0,11)this will includtop = input("Type a number: ")

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Try a higher number than 0 next time")
        quit()
else:
    print("Please type a number")
    quit()

random_number = random.randint(0 , top_of_range) 

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():#.isdigit()checks if input is a number
        user_guess = int(user_guess)#int converts into integer

    else:
         print("Please type a number next time :) ")
         continue#this brings user to the start of the loop
    
    if user_guess == random_number:
        print("You got it!!")
        break

    elif user_guess > random_number:
            print("You were above the number!!")
    else:
            print("You were below the number!!")

print("You got it in",guesses, "guesses")
        

