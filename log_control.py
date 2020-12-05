
import csv
#create new entry
#proper save function


def writeToLog():
    with open('log.csv', 'w', newline='') as csvfile:
        fieldnames = ['title', 'scraper','url', 'chapter']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'title': 'academia', 'scraper': 'readHeroAcademia' , 'url': 'https://w20.readheroacademia.com/', 'chapter':'22'})
        writer.writerow({'title': 'Gokushufudou','scraper': 'NELO', 'url': 'https://manganelo.com/manga/ya23ux2738298723', 'chapter':'22'})


def readFromLog():
    log_contents = []
    with open('log.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            log_contents.append(row)
        return log_contents
        




# for i in range(len(log_contents)):
#     print(log_contents[i]['title'])


   