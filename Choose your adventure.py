name = input("Type your name: ")
print("Welcome",name, "to an advenrure :)")

answer = input(
    "You are on a road it has come to an end choose which side to go Left or Right? ").lower()

if answer == "left":
    answer = input(
        "You have gone to the river. Do you want to swim across or walk around it?Type walk to go around or Swim to swim through. ").lower()
    
    if answer == "swim":
        print("You swam across.Unfortunately there were crocs. You died. :(")
    elif answer == "walk":
        print("The walk was so long. You got exhausted and gave up halfway. :(")
    else:
        print("No valid option. You loose :(")


elif answer == "right":
    answer = input("You come to a bridge. Its very wobbly. Do you wanna cross or go back.Cross or back? ").lower()

    if answer == "cross":
        answer = input("Yay you made it to the other side.There is a stranger at the end.Enter Talk to speak to him or No to continue.").lower()
        if answer =="yes":
            print("The stranger was a secret pass.You got gold.Yay!!You WIN.")
        elif answer == "no":
            print("Not every stranger is bad.You offended him.Now you loose.")
        else:
            print("No valid option. You loose :(")

    elif answer == "back":
        print("Never turn back. You loose. :(")
    else:
        print("No valid option. You loose :(")

else:
    print("No valid option. You loose :(")   

print("Thank you for playing",name)