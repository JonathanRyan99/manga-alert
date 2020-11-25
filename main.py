#this program is made specifically this website as of 23/11/2020 
#https://w20.readheroacademia.com/

import custom_scraps
import webbrowser
import sys



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

page, avalible, url = custom_scraps.readHeroAcademia(chapter)

if page & avalible == True:
    print("chapter avaliable")
    webbrowser.open_new_tab(url)
    logSave(chapter)
else:
    print("chapter: not avaliable")

input("press enter to close")
sys.exit(0)














