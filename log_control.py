
import csv


def writeToLog(log_contents):
    with open('log.csv', 'w', newline='') as csvfile:
        fieldnames = ['title', 'url', 'chapter']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'title': 'academia', 'url': 'https://w20.readheroacademia.com/manga/boku-no-hero-academia-chapter-', 'chapter':'22'})
        writer.writerow({'title': 'Gokushufudou', 'url': 'https://manganelo.com/manga/ya23ux2738298723', 'chapter':'22'})


def readFromLog():
    log_contents = []
    with open('log.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            log_contents.append(row)
        return log_contents
        


   
# for i in range(len(log_contents)):
#     print(log_contents[i]['title'])


   