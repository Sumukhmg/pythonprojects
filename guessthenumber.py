#this is a number guess game.
import random
secretnumber=random.randint(1,50)

#asking player to guess 6 times.
for guesstaken in range(1,7):
    print(" guess number between 1 to 50 :)")
    guess = int(input())
    
    if guess < secretnumber:
        print("your guess is too low. ")
    elif guess>secretnumber:
        print("your guess is too high")
    else:
        break
if guess == secretnumber:
    print("Good Job! you guessed my number in" + " " + str(guesstaken) +"guesses!")
else:
    print("nope. the number i was thinking of was"+" "+ str(secretnumber))