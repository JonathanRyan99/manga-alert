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


    #looks for upload timer, if present then the chapter has not been released
    try:
        countdown = soup.find("div",{"class": "entry-content"})
        countdown = countdown.h1.strong
        avalible = False
    except:
        avalible = True


    return page,avalible, url