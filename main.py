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




# class trackerFrame(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.myarry= [1,2,3]
#         self.MakeWidgets()

#     def printValue(self,value):
#         print(value)

#     def MakeWidgets(self):
#         for item in self.myarry:
#             self.button = tk.Button(trackerFrame, text="button", command= lambda: self.printValue(item))
#             self.button.grid(row=0,column=0)


        

# root = tk.Tk()
# tracker = trackerFrame(master=root)
# tracker.mainloop()



# def buttonValue(value):
#     print("button clicked: ", value)



# for i in range(1,10):
#     trackerFrame = tk.Frame(root, padx=20, pady=0)
#     trackerFrame.pack(padx=50, pady=10)

#     button = tk.Button(trackerFrame, text= str(i), command=lambda: buttonValue(i) )
#     button.grid(row=0,column=0)

#     label = tk.Label(trackerFrame, text="im a label")
#     label.grid(row=0,column=1)











# chapter = 20
# #link = custom_scraps.readHeroAcademia(chapter)
# link = custom_scraps.NEL("https://manganelo.com/manga/hn918480",chapter)
# try:
#     webbrowser.open(link)
# except: 
#     print("chapter:",chapter, " not found")

# link = custom_scraps.readHeroAcademia("https://w20.readheroacademia.com/manga/boku-no-hero-academia-chapter-",chapter)
# try:
#     webbrowser.open(link)
# except: 
#     print("chapter:",chapter, " not found")


# log_contents =log_control.readFromLog()
# for i in range(len(log_contents)):
#     print(log_contents[i]['title'])

















