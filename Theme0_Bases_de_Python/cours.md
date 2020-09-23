# 1. Variables et affectation

### 1.1 Stocker une valeur dans une variable
La mémoire d'un ordinateur peut-être perçue comme un ensemble de tiroirs.

Écrire  l'instruction :
```python
a = 2
```

va provoquer chez l'ordinateur (en simplifiant beaucoup) le comportement suivant :
- Est-ce que je possède **déjà** un tiroir appelé ```a``` ? 
    - si oui, je me positionne devant.
    - si non, je crée un tiroir appelé ```a```.


<p align="center">
<img src="data/tiroir.gif" width='20%'/> 
&nbsp;&nbsp;&nbsp;&nbsp;
<img src="data/tir_var.png" width='20%'/> 
&nbsp;&nbsp;&nbsp;&nbsp;
<img src="data/tir_var2.png" width='20%'/> 
</p>

- J'ouvre le tiroir et j'y dépose la valeur numérique 2. Si le tiroir contenait déjà une valeur, celle-ci disparaît. On dit souvent qu'elle est **écrasée**.

> Le sens du signe = n'est donc **pas du tout le même** qu'en mathématiques. On dit que c'est un signe d'**affectation**. 
L'écriture a = 2 signifie donc a ← 2.

⚠ Attention : ici, nous avons stocké un nombre (le nombre 2) dans la variable ```a```. Mais une variable peut contenir une phrase, une liste de nombres, une image...beaucoup d'objets de **type** différent.

### 1.2  Récupérer la valeur stockée dans une variable

#### 1.2.1 Dans un script
Dans un script Python, pour afficher le contenu d'une variable, on utilisera la fonction ```print()```.

```python
a = 2
maison = "Serdaigle"
print(a)
print(maison)
```

renverra la sortie suivante :

```python
2
'Serdaigle'
```

#### 1.2.2 En console

Dans la console interactive de Python, c'est encore plus simple, il suffit d'écrire le nom de la variable et d'appuyer sur Entrée.

```python
>>> a
2
>>> maison
'Serdaigle'
>>> b
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'b' is not defined
```

Bien sûr, il faut que la variable ait été créée au préalable... sinon Python renvoie un message d'erreur.


### 1.3 Modifier le contenu d'une variable

#### 1.3.1 Écraser une ancienne valeur
Comme déjà évoqué, affecter une nouvelle valeur dans une variable déjà existante écrasera l'ancienne valeur. C'est très pratique, mais parfois dangereux.

```python
>>> a = "mon mot de passe ultrasecret"
>>> a
"mon mot de passe ultrasecret"
>>> a = 3
>>> a
3
```
#### 1.3.2 Utiliser des variables pour calculer de nouvelles variables

```python
AB = 3
AC = 4
BC = (AB**2 + AC**2)**0.5
print("l'hypoténuse mesure", BC, "centimètres")
```

*Remarque : en Python, la puissance s'obtient par ```**```. La racine carrée est une puissance ```0.5```.*

#### 1.3.3 Modifier une variable à partir d'elle-même

L'instruction
```python
a = a + 1
```
écrit une égalité mathématique fort peu intéressante (toujours fausse, car elle est équivalente à l'égalité 0 = 1), 
mais est une écriture informatique très utile : la variable ```a``` se modifie à partir d'elle-même.

<p align="center">
<img src="data/tir_var3.png" width='20%'/> 
</p>


```python
a = 10
a = a + 1
print(a)
```

renverra 
```python
11
```

#### 1.3.4 Inverser deux variables

Imaginons les variables suivantes :

```python
maisonHarry = "Serpentard"
maisonMalfoy =  "Gryffondor"
```

Il semblerait qu'une erreur se soit glissée dans ces déclarations de variables... Mais comment faire pour inverser les valeurs ?

▸ **Méthode naïve**

```python
maisonHarry = maisonMalfoy
maisonMalfoy = maisonHarry
```
à l'arrivée, on se retrouve avec 
```python
>>> maisonHarry
'Gryffondor'
>>> maisonMalfoy
'Gryffondor'
```

En effet, la variable ```maisonHarry```  a été écrasée...  et on ne peut plus retrouver sa valeur pour la donner à ```maisonMalfoy```.

▸ **La solution universelle**

Nous allons passer par une variable temporaire qui nous permettra de stocker la valeur écrasée.

```python
maisonHarry = "Serpentard"
maisonMalfoy =  "Gryffondor"

# on procède à l'échange

t = maisonHarry
maisonHarry = maisonMalfoy
maisonMalfoy = t
```

Ainsi, 
```python
>>> maisonHarry
'Gryffondor'
>>> maisonMalfoy
'Serpentard'
```


▸ **La solution «pythonesque»**

Chaque langage de programmation ayant ses particularités, Python propose une syntaxe particulièrement agréable pour pouvoir faire l'échange de deux variables sans faire intervenir une variable temporaire :

```python
a = 2
b = 5

# on procède à l'échange
a,b = b,a
```
Ainsi,
```python
>>> a
5
>>> b
2
```

Les variables ont bien été échangées. 

*Remarque : Python ne fait que nous faciliter le travail. Il a dû lui-même créer une variable temporaire pour stocker la variable ```a``` avant de l'écraser : la simultanéité n'existe pas en informatique !*