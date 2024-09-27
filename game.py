import random

while True:
    try:
        while True:
        #Promts user for level, if neg no. promt again, else generate answer
            n = int(input("Level: "))
            if n < 0:
                continue
            else:
                correct = random.randrange(1, n+1)
                break

        while True:
        #Promts user for a guess, if neg no. prompt again, else go on
            guess = int(input("Guess: "))
            if guess < 0:
                continue
        #too small too large promt again, if correct guess just right and exit
            elif guess < correct:
                print("Too small!")
                continue
            elif guess > correct:
                print("Too large!")
                continue
            elif guess == correct:
                print("Just right!")
                break


    except (ValueError, TypeError):
        continue

    break
