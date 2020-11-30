from bs4 import BeautifulSoup
import requests

def readHeroAcademia(url,chapter):
    url = url + str(chapter)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    #looks for chapter title to confirm valid page
    try:
        title = soup.find("h1",{"class": "entry-title"})
        print(title.text) # if you delete this line it breaks, page will always return TRUE i have no idea why
        page = True
    except:
        page = False

#looks for upload timer, if present then the chapter has not been released
    try:
        countdown = soup.find("div",{"class": "entry-content"})
        countdown = countdown.h1.strong
        countdown = True
    except:
        countdown = False

    #print("page: ", page , "countdown: ", countdown)
    if (page == True) & (countdown == False):
        return url     
        
    


#url is manga root page
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
    







