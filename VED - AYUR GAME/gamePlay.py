from tkinter import *
import os
import firstpage

name1 = None
name2 = None
winamount = None


def screenn1():  
    global name1,name2,winamount
    firstpage.screen1(name1,name2,winamount)
def data():  
    global name1,name2,winamount
    root = Tk()   
    root.title('Ved-Ayur')
    root.iconbitmap('C:/Users/HP/Documents/DS/Monopoly-game-master/images/dice6.png')
    intro = Label(root, text = 'Welcome, you have kept your first step in ReDiscovering Ayurveda in ModEra\n')
    intro.grid(row = 0, column = 0, sticky = E)

    name1 = Label(root, text = 'Abhineta 1 name: ')
    name2 = Label(root, text = 'Abhineta 2 name: ')
    winamount = Label(root, text = 'Set your KANISHK to win: ')
    name1.grid(row = 1,column = 0, sticky = W)
    name2.grid(row = 2,column = 0, sticky = W)
    winamount.grid(row = 3, column = 0, sticky = W)

    name1 = Entry(root)
    name2 = Entry(root)
    winamount = Entry(root)

    name1.grid(row=1,column = 1)
    name2.grid(row = 2,column =1)
    winamount.grid(row = 3,column = 1)

    nextt = Button(root, text = 'PLAY',command = screenn1)
    nextt.grid(columnspan = 2, sticky = W)
    root.mainloop()

    

#firstpage.screen1(name1,name2,winamount)     #calling the function to call the first screen



    
data()    

