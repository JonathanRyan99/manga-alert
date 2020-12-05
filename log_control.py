
import csv
#create new entry
#proper save function


def writeToLog(logContents):
    with open('log.csv', 'w', newline='') as csvfile:
        fieldnames = ['title', 'scraper','url', 'chapter']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in logContents:
            writer.writerow(item)


def readFromLog():
    log_contents = []
    with open('log.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            log_contents.append(row)
        return log_contents
        




# for i in range(len(log_contents)):
#     print(log_contents[i]['title'])


   