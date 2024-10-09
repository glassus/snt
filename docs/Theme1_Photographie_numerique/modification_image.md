# Activité 1 : modification d'une image en Python


Nous allons jouer avec les pixels de l'image ci-dessous.

![](data/fleur.jpg){: .center}

## 1. Ouverture de l'activité Capytale.

Cliquez sur [ce lien](https://capytale2.ac-paris.fr/web/c/bb6c-4241612). 

Vous aurez besoin de vos identifiants Educonnect, car Capytale est un service hébergé par LycéeConnecté.


## 2. Modification des couleurs de l'image ```fleur.jpg```.

!!! abstract "Principe"
    - On parcourt l'image pixel par pixel. Pour chaque pixel :
    - On récupère ses composantes RGB dans des variables ```r```, ```g```, et ```b```.
    - On crée 3 nouvelles variables   ```new_r```, ```new_g```, et ```new_b``` à partir (ou pas) des valeurs originales ```r```, ```g```, et ```b```.
    - On modifie le pixel actuel avec ces nouvelles composantes ```new_r```, ```new_g```, et ```new_b```.


### Si on souhaite travailler avec sa propre image :


![image](data/methode.png){: .center }


Cliquer sur Capytale / Fichiers annexes / Disponibles le temps de la session / Ajouter un fichier disponible le temps de la session.

## 3. Modification des pixels suivant leur couleur d'origine

La condition «Si le pixel est blanc» se traduit dans notre code par le test :
```python
if (r, g, b) == (255, 255, 255):
```

Essayez de modifier uniquement les pixels blancs de notre image (pour les rendre bleus, par exemple).