#this program is made specifically this website as of 23/11/2020 
#https://w20.readheroacademia.com/

import custom_scraps
import log_control
import webbrowser
# import tkinter as tk
from tkinter import *


class program():

    def __init__(self,master,names,links):
        myFrame = Frame(master)
        myFrame.pack()
        self.names = names
        self.links = links
        for i in range(0,len(names)):
            self.addFrame(myFrame,names[i],links[i],i)
    

    def addFrame(self,location,name,link,i):
        self.button = Button(location, text="open", command= lambda: self.openLink(link))
        self.button.grid(row=(0+i),column= 0)

        self.label = Label(location, text=name)
        self.label.grid(row=(0+i),column=1)

    def openLink(self,link):
        print(link)
        



names = ["academia","one Punch", "fire force"]
links = ["www.academia.com","www.onePunch.com","www.fireForce.com"]

root = Tk()
myProgram = program(root,names,links)
root.mainloop()


