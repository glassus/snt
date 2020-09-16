# Variables et affectation

La mémoire d'un ordinateur peut-être perçue comme un ensemble de tiroirs.

Écrire  l'instruction :
```python
a = 2
```

va provoquer chez l'ordinateur (le processeur) le comportement suivant :
- Est-ce que je possède **déjà** un tiroir appelé ```a``` ? 
    - si oui, je me positionne devant.
    - si non, je crée un tiroir appelé ```a```.


<p align="center">
<img src="data/tiroir.gif" width='20%'/> 

<img src="data/tir_var.png" width='20%'/> 


<img src="data/tir_var2.png" width='20%'/> 
</p>

- J'ouvre le tiroir et j'y dépose la valeur numérique 2. Si le tiroir contenait déjà une valeur, celle-ci disparaît. On dit souvent qu'elle est **écrasée**.

> Le sens du signe = n'est donc **pas du tout le même** qu'en mathématiques. On dit que c'est un signe d'**affectation**. 
L'écriture a = 2 signifie donc a ← 2