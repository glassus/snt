# Étude des passagers du Titanic


<p align="center">
<img src="data/pic.png" , width=100%/> 
</p>



## 1. Le fichier titanic.csv
1. Téléchargez le fichier [titanic.csv](http://glassus1.free.fr/titanic.csv)
2. Ouvrez le avec **un éditeur de texte** (le Bloc-Notes de Windows, par exemple).
3. Que remarque-t-on sur la structure de ce document ?


>Les fichiers CSV (pour Comma Separated Values) sont des fichiers-texte (ils ne contiennent aucune mise en forme) utilisés pour stocker des données, séparées par des virgules (ou des points-virgules, ou des espaces...).

## 2. Utilisation d'un tableur
1. Ouvrez LibreOffice Calc
2. Depuis Calc, ouvrez le fichier titanic.csv.
3. Combien y a-t-il de passagers dans cette liste. Cela correspond-il à la totalité des passagers enregistrés sur le Titanic ?
4. Cliquez sur Données / Autofiltre et répondez à la question suivante : quel est le nom du passager de sexe masculin, âgé de 26 ans, ayant embarqué à Cherbourg en 1ère classe ?


## 3. Exploitation avec Python
Il est possible d'exploiter les données d'un fichier csv. On peut, par exemple, utiliser le module csv de Python.

### 3.1 Récupération des données
1. Dans Thonny, copiez-coller le code ci-dessous :

```python
import csv
f = open('titanic.csv', "r", encoding = 'utf-8')
donnees = csv.DictReader(f)
passagers = []
for ligne in donnees:
    passagers.append(dict(ligne))
    
f.close()
```
2. Exécutez ce code, puis tapez ```passagers``` en console.
La structure (complexe) de la variable ```passagers``` est appelée une **liste de dictionnaires**.

3. Tapez ```passagers[0]``` en console et observez le résultat.
4. Tapez ```passagers[12]['Nom']``` en console et observez le résultat.

### 3.2 Début d'analyse
1. Copiez-collez-exécutez le code ci-dessous :
```python
s = 0
for passager in passagers :
    if int(passager["survivant"]) == 1 :
        s = s + 1
print(s)
```
Que calcule ce code ?

2. Modifiez le code ci-dessus pour qu'il donne le nombre de passagers de troisième classe.

### 3.3 Fonctions avancées
1. Copiez-collez-exécutez le code ci-dessous :
```python
def survie(classe):
    surv = 0
    tot = 0
    for passager in passagers :
        if int(passager["classe"]) == classe :
            tot = tot + 1
            if int(passager["survivant"]) == 1 :
                surv =  surv + 1
    return surv / tot
```
2. À l'aide de cette fonction, donnez le taux de survie en 1ère, 2ème et 3ème classe.
