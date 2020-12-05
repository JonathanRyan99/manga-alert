from bs4 import BeautifulSoup
import requests

#find a better was to accomodate the new half issues

def readHeroAcademia(url,chapter):
    req = requests.get(url)
    chapter = chapter + 2 #2 half issues currently
    soup = BeautifulSoup(req.text, "html.parser")
    chapterlist = soup.find("table",{"class": "chap_tab"})
    chapterlist = chapterlist.find_all("a")
    #chapter list has newest issue as [0]
    released = len(chapterlist)
    current = released - chapter 
    if (current <= released) & (current >= 0):
        print(chapterlist[current])
        link = chapterlist[current].get("href")
        return link
    
    
    
    
    #print(len(chapterlist))
 #22   


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
    





link = readHeroAcademia("https://w20.readheroacademia.com/",293)
print(link)
