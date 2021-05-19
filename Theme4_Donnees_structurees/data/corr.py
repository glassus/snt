
import csv
f = open('titanic.csv', "r", encoding = 'utf-8')
donnees = csv.DictReader(f)
passagers = []
for ligne in donnees:
    passagers.append(dict(ligne))
    
f.close()


for passager in passagers :
    if passager["Nom"] == 'LAROCHE  Miss. Louise' :
        print(passager)