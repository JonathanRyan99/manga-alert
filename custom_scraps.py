from bs4 import BeautifulSoup
import requests

def readHeroAcademia(chapter):
    url = "https://w20.readheroacademia.com/manga/boku-no-hero-academia-chapter-" + str(chapter) + "/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    #looks for chapter title to confirm valid page
    try:
        title = soup.find("h1",{"class": "entry-title"})
        page = True
    except:
        page = False

    if page == True:
        #looks for upload timer, if present then the chapter has not been released
        try:
            countdown = soup.find("div",{"class": "entry-content"})
            countdown = countdown.h1.strong
            avalible = False
        except:
            avalible = True

    return url



def NEL(url,chapter):
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
    



link = NEL("https://manganelo.com/manga/zo921845",2)
print(link)
