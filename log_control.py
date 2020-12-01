
import csv

with open('log.csv', 'w', newline='') as csvfile:
    fieldnames = ['title', 'url', 'chapter']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'title': 'academia', 'url': 'https://w20.readheroacademia.com/manga/boku-no-hero-academia-chapter-', 'chapter':'22'})
    writer.writerow({'title': 'Gokushufudou', 'url': 'https://manganelo.com/manga/ya23ux2738298723', 'chapter':'22'})
    

with open('log.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['title'], row['url'])

   