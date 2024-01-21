import random
from tkinter import *


answer = random.randint(1, 100)
small = 1
big = 100
tries = 10

def checking():
    global small
    global big
    global answer
    global x
    if tries != 0:
    
        if answer == int(guess):
            #This is for wining the game
            record.insert(END,'You win')
        
        elif int(guess) >= int(big) or int(guess) <= int(small):
            #This for when "guess" is invalid  
            record.insert(END,'Your answer must be between ' + str(small) + ' to ' + str(big))
            tries -= 1
            guess = input('You have ' + str(tries) + ' tries left. Input a number from ' + str(small) + ' to ' + str(big) + ': ')
        

        elif int(guess) > answer:
            #This is for bigger no.
            big = guess
            record.insert(END,'The answer is smaller then ' + guess)
            tries -= 1
            guess = input('You have ' + str(tries) + ' tries left. Input a number from ' + str(small) + ' to ' + guess + ': ')
            pass
            
        elif int(guess) < answer :
            #This is for smaller no.
            small = guess
            record.insert(END,'The answer is bigger then ' + guess)
            tries -= 1
            guess = input('You have ' + str(tries) + ' tries left. Input a number from ' + guess + ' to ' + str(big) + ': ')
            pass


box = Tk()
box.geometry('600x400')
box.title('guess number')

labell = Label(text = 'Input a number from 1 to 100: ')
labell.place(x=20, y=20)

inbox = Entry(width = 3)
inbox.place(x = 20, y = 40)

btn = Button(text = 'ok', command=checking)
btn.place(x=50, y=40)


record = Text()
record.place(x=200, y=0, width=400, height=600)



box.mainloop()
