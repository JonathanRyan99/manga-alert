
import custom_scraps
import log_control
import webbrowser
from tkinter import *
#to do
#add a "new tracker button" so the user can start adding trackers in case of blank log.csv
#add "delete tracker button to frame"
#refresh interface after writing to file

class program():

    def __init__(self,master,logContents):
        myFrame = Frame(master)
        myFrame.pack()
        self.logContents = logContents
        for i in range(len(self.logContents)):
            self.addFrame(myFrame,self.logContents[i],i)
    


    def addFrame(self,location,logItem,i):
        self.button = Button(location, text="X", command= lambda: self.deleteFromFile(logItem) )
        self.button.grid(row=(0+i),column= 0)
        
        self.label = Label(location, text=logItem['title'])
        self.label.grid(row=(0+i),column=1)

        self.label = Label(location, text=logItem['chapter'])
        self.label.grid(row=(0+i),column=2)
        
        #button on/off if chapter is avalible
        link = self.getChapterRelease(logItem)
        if (str(link) == "None"):
            self.button = Button(location, text="open", state=DISABLED)
            self.button.grid(row=(0+i),column= 3)
        else:
            self.button = Button(location, text="open", command= lambda: (self.openLink(link), self.incrementLog(logItem) ) )
            self.button.grid(row=(0+i),column= 3)

    def getChapterRelease(self,logItem):
        if logItem['scraper'] == "NELO":
            link = custom_scraps.NELO(logItem['url'],logItem['chapter'])
            return link

        if logItem['scraper'] == "readHeroAcademia":
            link = custom_scraps.readHeroAcademia(logItem['url'],logItem['chapter'])
            return link

    def incrementLog(self,logItem):
        for item in self.logContents:
            if item['title'] == logItem['title']:
                chapter = int(item['chapter'])
                item['chapter'] = str(chapter + 1)
        
        self.writeToFile()
    
    def writeToFile(self):
        log_control.writeToLog(self.logContents)
        print("written to log file")

    def deleteFromFile(self, logItem):
       index = self.logContents.index(logItem)
       del self.logContents[index]
       self.writeToFile()
       print("index: ",index," removed")

    def openLink(self,link):
        webbrowser.open(link)

        



#names = ["academia","one Punch", "fire force"]
#links = ["www.academia.com","www.onePunch.com","www.fireForce.com"]

#fieldnames = ['title', 'scraper','url', 'chapter']
logContents = log_control.readFromLog()

# for i in range(len(logContents)):
#     print(logContents[i]['title'],logContents[i]['scraper'],logContents[i]['url'])


root = Tk()
myProgram = program(root,logContents)
root.mainloop()


