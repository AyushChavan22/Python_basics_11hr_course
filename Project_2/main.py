import random
n = random.randint(1,100)
a = -1
guesses=1
while (a != n):
    a = int(input("Guess the number between 1 to 100: "))
    if (a>n):
        print ("Lower number please!")
        guesses += 1
    elif (a<n):
        print ("Higher number please!")
        guesses += 1
if (guesses == 1):
    print (f"YOU ARE GODDAMN MAGICIAN! You guessed the number {n} in just 1 attempt")
elif(guesses < 10):
    print(f"You got some tremendous guessing power!! You guessed the number {n} in just {guesses} attempts!!")
else:
    print(f"Yippiee!! You have guessed the number {n} in {guesses} attempts")

    