# Activité 1 : Coordonnées GPS


## 1. Se repérer à la surface de la Terre

### Rappels sur le vocabulaire

Latitude, longitude, méridiens, parallèles... rendez-vous sur 
[ce document GeoGebra](https://www.geogebra.org/m/vdpwxyrj){:target="_blank"}.

!!! example "Exercice 1"

    Rendez-vous sur [ce document GeoGebra](https://www.geogebra.org/m/rxx7psvs){:target="_blank"}


    Sur l'animation GeoGebra apparaissent des villes (en noir) et un point bleu que vous pouvez déplacer.  
    Dans le tableau ci-dessous sont données des coordonnées de villes.  
    Associer à chaque numéro la ville qui lui correspond.

    Quel est la ville qui n'est associée à aucun numéro ?

    | numéro de la ville | Latitude | Longitude |
    |:---:|---|---|
    | 1 | 51° N | 0° E|
    | 2 | 49° N | 2° E|
    | 3 | 40° N | 4° E|
    | 4 | 41° N | 116° O|
    | 5 | 57° N | 38° E|
    | 6 | 0° N | 79° O|
    | 7 | 34° S | 18° E|
    | 8 | 34° S | 71° O|
    | 9 | 34° S | 151° O|
    | 10 | 41° S | 175° O|
    | 11 | 60° N | 11° E|
    | 12 | 37° N | 10° E|

    {{
    correction(True,
    """
    ??? success \"Correction\" 
        | numéro de la ville | Ville |
        |:---:|---|
        | 1 | Londres|
        | 2 | Paris|
        | 3 | Madrid|
        | 4 | New-York|
        | 5 | Moscou|
        | 6 | Quito|
        | 7 | Le Cap|
        | 8 | Santiago|
        | 9 | Sydney|
        | 10 | Wellington|
        | 11 | Oslo|
        | 12 | Tunis|

        La ville manquante est donc Pékin       
    """
    )
    }}


[https://www.partir.com/carte/des-cartes-pour-comprendre-le-monde.html](https://www.partir.com/carte/des-cartes-pour-comprendre-le-monde.html){. target="_blank"}   

## 2. Les différentes conventions d'écriture d'angles


![](data/bordeaux.png){align=right}

Numériquement parlant, le format décimal (DD) des coordonnées géographiques est le plus pratique.

Sur le web (ou ailleurs), il arrive fréquemment que ces coordonnées ne soient pas données au format décimal, mais plutôt au format DMS (degré, minutes, secondes)

Il faut donc les [convertir](https://fr.wikipedia.org/wiki/Syst%C3%A8me_sexag%C3%A9simal#Conversion_de_minutes_et_secondes_en_fraction_d%C3%A9cimale_de_degr%C3%A9){:target="_blank"}.

Par exemple, les coordonnées des villes sur Wikipedia sont données au format DMS (ci-contre celles de Bordeaux).

!!! info "Conversion"
    Comme pour la mesure du temps, une minute (d'arc) correspond à 1/60 de degré et une seconde (d'arc) à 1/60 de minute, soit 1/3600 de degré.

    La latitude de Bordeaux, en décimal, est donc obtenue par le calcul:
    
    44 + 50/60 + 16/3600 = 44,837777

    Enfin, cette latitude est positive car sa position par rapport à l'équateur est Nord. Une latitude 44°50'16'' S serait donc convertie -44,837777 en décimal.

!!! warning "Point ou virgule"
    Il ne faut pas confondre notre séparateur décimal, **la virgule**, avec celui des anglo-saxons, **le point**, qui est la norme sur tout système informatique.





## 3. Utilisation du site ```coordonnnees-gps.fr```

Il existe des sites en ligne qui proposent de manipuler très facilement des coordonnées GPS, comme [https://www.coordonnees-gps.fr/](https://www.coordonnees-gps.fr/){:target="_blank"}  par exemple.


!!! example "Exercice 2"
    
    1. Que trouve-t-on aux coordonnées : 44.83887 / -0.55537 ?
        {{
        correction(False,
        """
        ??? success \"Correction\" 
            La salle 1308 du Lycée François Mauriac.
        """
        )
        }}

    2. Que peut-on observer aux coordonnées  : 40° 41' 21.296'' N / 74° 2' 40.199'' O ?
        {{
        correction(False,
        """
        ??? success \"Correction\" 
            La statue de la Liberté.
        """
        )
        }}
