
import custom_scraps
import log_control
import webbrowser
from tkinter import *


class program():

    def __init__(self,master,logContents):
        myFrame = Frame(master)
        myFrame.pack()
        self.logContents = logContents
        for i in range(len(self.logContents)):
            self.addFrame(myFrame,self.logContents[i],i)
    

    def getChapterRelease(self,logItem):
        if logItem['scraper'] == "NELO":
            link = custom_scraps.NELO(logItem['url'],logItem['chapter'])
            return link

        if logItem['scraper'] == "readHeroAcademia":
            link = custom_scraps.readHeroAcademia(logItem['url'],logItem['chapter'])
            return link

    def addFrame(self,location,logItem,i):
        link = self.getChapterRelease(logItem)
        self.button = Button(location, text="open", command= lambda: self.openLink(link))
        self.button.grid(row=(0+i),column= 0)

        self.label = Label(location, text=logItem['title'])
        self.label.grid(row=(0+i),column=1)

    
    def openLink(self,link):
        print(link)

        



#names = ["academia","one Punch", "fire force"]
#links = ["www.academia.com","www.onePunch.com","www.fireForce.com"]

#fieldnames = ['title', 'scraper','url', 'chapter']
logContents = log_control.readFromLog()

# for i in range(len(logContents)):
#     print(logContents[i]['title'],logContents[i]['scraper'],logContents[i]['url'])


root = Tk()
myProgram = program(root,logContents)
root.mainloop()


