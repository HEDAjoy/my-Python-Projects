print("Welcome to my Quiz!")

playing = input("Do you wanna play? ")

if playing.lower() != "yes":
    quit()

print("Okay Let's Play!! :)")
score = 0

answer = input("Which zodiac sign is after Aries? ")
if answer.lower() == "tarus":
    print("Correct!")
    score += 1
else:
    print('Nah!!')

answer = input("Between sun and monn which one is bigger? ")
if answer.lower() == "sun":
    print("Correct!")
    score += 1
else:
    print('Nah!!')

answer = input("Which country is north of Kenya? ")
if answer.lower() == "sudan":
    print("Correct!")
    score += 1
else:
    print('Nah!!')

answer = input("Who played spider man in End game? ")
if answer.lower() == "tom holland":
    print("Correct!")
    score += 1
else:
    print('Nah!!')

print("You got "+ str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%")