#this program is made specifically this website as of 23/11/2020 
#https://w20.readheroacademia.com/

from bs4 import BeautifulSoup
import requests
import webbrowser
import sys



def pageAvaliable(chapter):
    url = "https://w20.readheroacademia.com/manga/boku-no-hero-academia-chapter-" + str(chapter) + "/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    #looks for chapter title to confirm valid page
    try:
        title = soup.find("h1",{"class": "entry-title"})
        page = True
    except:
        page = False


    #looks for upload timer, if present then the chapter has not been released
    try:
        countdown = soup.find("div",{"class": "entry-content"})
        countdown = countdown.h1.strong
        avalible = False
    except:
        avalible = True


    return page,avalible, url

def logCheck():
    try:
        f = open("log.txt","r")
        chapter = f.read()
        f.close()
    except:
        print("file not found")
        f = open("log.txt","w")
        chapter = input("ENTER CHAPTER NUMBER: ")
        f.write(chapter)
        f.close()
    
    return chapter

def logSave(chapter):
    chapter = int(chapter)
    newChapter = chapter + 1
    newChapter = str(newChapter)
     
    f = open("log.txt" ,"w")
    f.write(newChapter)
    f.close()

    

chapter = logCheck()
print("chapter: ",chapter)

page, avalible, url = pageAvaliable(chapter)

if page & avalible == True:
    print("chapter avaliable")
    webbrowser.open_new_tab(url)
    logSave(chapter)
else:
    print("chapter: not avaliable")

input("press enter to close")
sys.exit(0)














