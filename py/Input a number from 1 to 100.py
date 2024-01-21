import random



answer = random.randint(1, 100)
small = 1
big = 100

tries = input('Plase enter the amount of tries you want: ')
x = int(tries)
tries = int(tries) - 1


guess = input('You have ' + str(x) + ' tries left. Input a number from 1 to 100: ')

for i in range(int(tries)):
    if answer == int(guess):
        #This is for wining the game
        print('You win')
        break
    
    elif int(guess) >= int(big) or int(guess) <= int(small):
        #This for when "guess" is invalid  
        print('Your answer must be between ' + str(small) + ' to ' + str(big))
        x -= 1
        guess = input('You have ' + str(x) + ' tries left. Input a number from ' + str(small) + ' to ' + str(big) + ': ')
        continue

    elif int(guess) > answer:
        #This is for bigger no.
        big = guess
        print('The answer is smaller then ' + guess)
        x -= 1
        guess = input('You have ' + str(x) + ' tries left. Input a number from ' + str(small) + ' to ' + guess + ': ')
        pass
        
    elif int(guess) < answer :
        #This is for smaller no.
        small = guess
        print('The answer is bigger then ' + guess)
        x -= 1
        guess = input('You have ' + str(x) + ' tries left. Input a number from ' + guess + ' to ' + str(big) + ': ')
        pass
    
#This for losing the game
print('You ran out of tries. You loss the game :(')

