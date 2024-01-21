#coding:UTF-8

from tkinter import *
from random import *

root = Tk()
root.geometry("600x400")

#land[0]=地名,[1]=顏色,[2]=售價,[3]抵押[4]租金[5]1屋[6]2屋[7]3屋[8]4屋[9]酒店[10]建築成本
place0 = ["start", "white"]
place1 = ["place1","yellow",2200,1100,20,100,300,750,925,1100,150]
place2 = ["place2","blue",2200,1100,20,100,300,750,925,1100,150]


landinfo_show =Text(width=200,height=600)
landinfo_show.place(x=400,y=0)

canvas0= Canvas(width=100,height=100,bg="white")
canvas0.place(x=0,y=0)
canvas1= Canvas(width=100,height=100,bg="white")
canvas1.place(x=100,y=0)
canvas2= Canvas(width=200,height=100,bg="white")
canvas2.place(x=200,y=0)



map = [canvas0,canvas1,canvas2]
list_street = [place0, place1, place2]

dice0 = 0
dice1 = 0
turn = 1
#[0]number, [1]str(name), [2]postion, [3]money, [4]double times
player0 = (0, "player0", 0, 2000, 0)
player1 = (1, "player1", 0, 2000, 0)
player2 = (2, "player2", 0, 2000, 0)
player3 = (3, "player3", 0, 2000, 0)


list_player = [player0, player1, player2, player3]

#for drawing the colour borders at the top
def draw_street(canvas, colour):
    canvas.create_rectangle(0,0,100,25,fill=colour,outline=colour)

for i in range(3):
    draw_street(map[i], list_street[i][1])



#for printing 
def show_info(land):
    landinfo_show.insert(END,land[0]+"\n")
    landinfo_show.insert(END,"售價："+str(land[2])+"\n")
    
#for drawing house
def build_house(canvas,number):
    canvas.create_polygon(12.5+25*number,0,0+25*number,8,25+25*number,8,fill="green",outline="green")
    canvas.create_rectangle(4+25*number,8,21+25*number,25,fill="green",outline="green")

#for drawing hotel
def build_hotel(canvas,colour):
    for i in range(4):
        canvas.create_polygon(12.5+25*i,0,0+25*i,8,25+25*i,8,fill="green",outline="green")
        canvas.create_rectangle(4+25*i,8,21+25*i,25,fill="green",outline="green")
    canvas.create_polygon(12.5,0,0,8,25,8,fill="red",outline="red")
    canvas.create_rectangle(4,8,21,25,fill="red",outline="red")

#for move and draw players
def move(player, start, stop):
    if player == 0:
        map[start].create_oval(15,30,35,50,fill="white",outline="white")
        map[stop].create_oval(15,30,35,50,fill="red",outline="red")
    elif player == 1 :
        map[start].create_oval(55,30,75,50,fill="white",outline="white")
        map[stop].create_oval(55,30,75,50,fill="blue",outline="blue")
    elif player == 2:
        map[start].create_oval(15,60,35,80,fill="white",outline="white")
        map[stop].create_oval(15,60,35,80,fill="green",outline="green")
    elif player == 3:
        map[start].create_oval(55,60,75,80,fill="white",outline="white")
        map[stop].create_oval(55,60,75,80,fill="yellow",outline="yellow")

def roll():
    global dice1
    global dice2
    global turn
    global player1
    global player2
    global list_street
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    start = list_player[turn-1][2]
    end = start + dice1 + dice2
    #print("dice1" + str(dice1))
    #print("dice2" + str(dice2))
    #print("start" +str(start))
    #list_player: [player1,player2]
    #player[0]number, [1]name, [2]postion, [3]money
    while end > 2:
        end -=3
        list_player[turn-1][3] += 2000
        
    move(list_player[turn-1],start,end)
    list_player[turn-1][2] = end
    #print("end"+str(end))
    #print("turn"+str(turn))
    turn +=1
    if turn == 3:
        turn = 1
    if dice1==dice2:
        turn -=1
        tmsg.showinfo("lucky","roll once more")
        list_player[turn-1][4] +=1
    if list_player[turn-1][4] == 3:
        tmsg.showerror("oops!","go to jail")
    tmsg.showinfo("roll",dice1+dice2)



move(0, 0, 0)
move(1, 0, 0)
move(2, 0, 0)
move(3, 0, 0)

move(1, 0, 2)



root.mainloop()

