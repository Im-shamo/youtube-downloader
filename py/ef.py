#coding: UTF-8
from tkinter import *

root = Tk()
root.geometry("600x400")

#place1[0]=landName, [1]=colour, 
place1 = ['place1', 'red', 2200, 1100, 20, 100, 300, 750, 925, 110, 150]



landinfo = Text(width=200,height=600)
landinfo.place(x=400, y=0)

canvas0 = Canvas(width=100,height=100,bg="white")
canvas0.place(x=0,y=0)
canvas1 = Canvas(width=100,height=100,bg="white")
canvas1.place(x=100,y=0)
map = [canvas0, canvas1]

canvas1.create_rectangle(0,0,100,25,fill="yellow",outline="yellow")

def showInfo(land):
    landinfo.insert(END, land[0]+ "\n")
    landinfo.insert(END, "sale: "+str(land[2])+"\n")

def buildHouse(canvas,number,):
    canvas.create_polygon(12.5+25*number,0,0+25*number,8,25+25*number,8,fill='green',outline='green')
    canvas.create_rectangle(4+25*number,8,21+25*number,25,fill='green',outline='green')

def buildHotel(canvas,color):
    for i in range(4):
        canvas.create_polygon(12.5+25,0,0+25,8,25+25,8,fill='yellow',outline='yellow')
        canvas.create_rectangle(4+25,8,21+25,25,fill='yellow',outline='yellow')




showInfo(place1)
buildHouse(map[1],0)
buildHouse(map[0],0)
buildHotel(map[0],1)

root.mainloop()
