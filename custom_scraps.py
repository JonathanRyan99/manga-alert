from bs4 import BeautifulSoup
import requests


def readHeroAcademia(url,chapter):
    #gets chapter list in bs4 object
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    chapterlist = soup.find("table",{"class": "chap_tab"})
    chapterlist = chapterlist.find_all("a")
    #  THIS METHOD DOESNT WORK FOR CHAPTERS BEFORE THE HALF ISSUES

    #chapter list has newest issue as [0]
    released = len(chapterlist)
    #issue of set is how many half issues there are these add an idex[] to the chapterlist without changing chapter number
    issueOfSet = released - int(chapterlist[0].text[33:])
    #if theres 2 half chapters and its on chapter 300, there are 302[] index values
    chapter = int(chapter) + issueOfSet 
    current = released - chapter 
    if (current <= released) & (current >= 0):
        #print(chapterlist[current])
        link = chapterlist[current].get("href")
        return link 


#url is manga root page
def NELO(url,chapter):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    chapterlist = soup.find_all("a",{"class": "chapter-name text-nowrap"})
    chapter = "Chapter " + str(chapter)
    
    for item in chapterlist:
        if item.text == chapter:
            #print(item.text)
            link = item.get('href')
            #print(link)
            return link
    





