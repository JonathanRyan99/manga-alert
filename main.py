#this program is made specifically this website as of 23/11/2020 
#https://w20.readheroacademia.com/

import custom_scraps
import log_control
import webbrowser
import sys


def academia():
    chapter = log_control.logCheck()
    print("chapter: ",chapter)

    avalible, url = custom_scraps.readHeroAcademia(chapter)

    if  avalible == True:
        print("chapter avaliable")
        webbrowser.open_new_tab(url)
        log_control.logSave(chapter)
    else:
        print("chapter: not avaliable")


academia()
input("press enter to close")
sys.exit(0)














