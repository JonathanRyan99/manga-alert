#this program is made specifically this website as of 23/11/2020 
#https://w20.readheroacademia.com/

import custom_scraps
import log_control
import webbrowser
import sys





chapter = 20
#link = custom_scraps.readHeroAcademia(chapter)
link = custom_scraps.NEL("https://manganelo.com/manga/hn918480",chapter)
try:
    webbrowser.open(link)
except: 
    print("chapter:",chapter, " not found")

link = custom_scraps.readHeroAcademia("https://w20.readheroacademia.com/manga/boku-no-hero-academia-chapter-",chapter)
try:
    webbrowser.open(link)
except: 
    print("chapter:",chapter, " not found")






input("press enter to close")
sys.exit(0)














