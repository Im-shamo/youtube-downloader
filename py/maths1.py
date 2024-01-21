import random

number = random.randint(1,100)
guess = None
tries_left = None
big = 100
small = 1


print(number)
tries_left = int(input("Please input the number of tries you want: "))
for i in range(tries_left): 
    if tries_left - i > 1:
        print(f"You have {tries_left - i} tries left.")

    elif tries_left - i == 1:
        print("You have 1 try left.")
    
    guess = int(input("Please input the a number between "+ str(small)+ " to "+ str(big)+ ": "))
    if guess > big or guess < small:
        print("Your guess is invild it must be between "+ str(small)+ " to "+ str(big)+ ": ")
        continue
    elif guess == number:
        print("You win")
        break
    
    elif guess < number:
        small = guess
        continue
    
    elif guess > number:
        big = guess
        continue


if guess != number:
    print("You Lose")
    