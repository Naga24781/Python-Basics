import random

n = random.randint(1, 1000)
guess = None

while guess != n:
    guess = int(input("Enter a number: "))
    
    if guess < n:
        print("Too low! Try again.")
    elif guess > n:
        print("Too high! Try again.")
    else:
        print("🎉 Correct number Matched:", n)
