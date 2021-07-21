import random
randomNumber = random.randint(1,9)
chance = 0
while chance <5:
    guess = int(input("Enter Your Guess: "))
    if guess==randomNumber:
        print("You Win")
    elif guess<randomNumber:
        print("Your Guess Was Too Low Try a Highr Number")
    else :
        print("Your Guess Was Too High Try a lower Number")
    chance = chance+1
if not chance<5:
    print("YOU LOSE,the number was: ",randomNumber)