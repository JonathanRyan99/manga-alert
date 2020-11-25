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

    