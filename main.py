
import custom_scraps
import log_control
import webbrowser
from tkinter import *
#to do
#add a "new tracker button" so the user can start adding trackers in case of blank log.csv
#refresh interface after writing to file

class program():

    def __init__(self,master):
        self.myFrame = Frame(master)
        self.myFrame.pack()
        self.generateInterface()

        
        
    #this kinda 
    def refreshFrame(self):
        self.myFrame.destroy()
        self.__init__(root)

          
        
        
    def generateInterface(self):
        self.button = Button(self.myFrame, text="refresh", command= lambda: self.refreshFrame() )
        self.button.grid(row= 0, column=2)

        

        self.logContents = log_control.readFromLog()
        for i in range(len(self.logContents)):
            self.addFrame(self.logContents[i],i)
    
   
    #possible: in the add frame need to create a frame, pack that
    #at the moment these arent frames they're just grid ordered

    def addFrame(self,logItem,i):
        self.button = Button(self.myFrame, text="X", command= lambda: self.deleteFromFile(logItem) )
        self.button.grid(row=(1+i),column= 1)
        
        self.label = Label(self.myFrame, text=logItem['title'])
        self.label.grid(row=(1+i),column=2)

        self.label = Label(self.myFrame, text=logItem['chapter'])
        self.label.grid(row=(1+i),column=3)
        
        #button on/off if chapter is avalible
        link = self.getChapterRelease(logItem)
        if (str(link) == "None"):
            self.button = Button(self.myFrame, text="open", state=DISABLED)
            self.button.grid(row=(1+i),column= 4)
        else:
            self.button = Button(self.myFrame, text="open", command= lambda: (self.openLink(link), self.incrementLog(logItem) ) )
            self.button.grid(row=(1+i),column= 4)

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
        self.refreshFrame()


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


# for i in range(len(logContents)):
#     print(logContents[i]['title'],logContents[i]['scraper'],logContents[i]['url'])


root = Tk()
myProgram = program(root)
root.mainloop()


