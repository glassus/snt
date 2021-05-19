
import csv
f = open('titanic.csv', "r", encoding = 'utf-8')
donnees = csv.DictReader(f)
passagers = []
for ligne in donnees:
    passagers.append(dict(ligne))
    
f.close()


def survie(classe):
    surv = 0
    tot = 0
    for passager in passagers :
        if int(passager["classe"]) == classe :
            tot = tot + 1
            if int(passager["survivant"]) == 1 :
                surv =  surv + 1
    return surv / tot