# Activité 2 : Métadonnées EXIF

## 1. Découverte des métadonnées EXIF

1. Faire une recherche sur les différents renseignements que peuvent donner les métadonnées EXIF.
2. Grâce à l’outil en ligne [https://jimpl.com/](https://jimpl.com/){:target="_blank"} , explorer les métadonnées de l’image ci-dessous :
![image](data/riviere.jpg){: .center}
*(faire un clic-droit sur l'image, «copier le lien de l'image», et le coller dans le champ sous «upload from URL»)*
3. Avec quel matériel cette photo a-t-elle été prise ? Quel jour ?
4. Pouvez-vous localiser l’endroit où cette photo a été prise ?
5. Analysez l’image de la Statue de la Liberté ci-dessous. 
![image](data/liberty.jpg){: .center}


6. Où cette photo a-t-elle été prise ?
Vous pourrez utiliser le site [https://www.coordonnees-gps.fr/](https://www.coordonnees-gps.fr/){:target="_blank"}  

{{
correction(False,
"""
??? success \"Correction\" 
    1. [https://fr.wikipedia.org/wiki/Exchangeable_image_file_format](https://fr.wikipedia.org/wiki/Exchangeable_image_file_format){. target=\"_blank\"}
    2. -
    3. Samsung GT-i9195 Galaxy S4 Mini
    4. Pas de localisation possible.
    5. -
    6. Localisation : Place Picard à Bordeaux.   
"""
)
}}




## 2. La question de la confidentialité et de la fiabilité des données

1. Est-il possible d’effacer ou de modifier des données EXIF ?
Analysez la photo ci-contre :
![image](data/pont.jpg){: .center}
2. Est-il possible de paramétrer son téléphone pour que les coordonnées de géolocalisation ne figurent pas dans les EXIF ?
3. Les photos des réseaux sociaux Snapchat, Instagram ou Facebook contiennent-elles des données EXIF ? Faire l’expérience avec une photo de votre téléphone (avec par exemple l’application Metadata Viewer) avant envoi sur un réseau social, puis avec cette même photo téléchargée depuis ce réseau social.
4. Sait-on à quel endroit (sur votre appareil, ou sur les serveurs du réseau social) les données EXIF ont-elles été supprimées ? En quoi cela peut-il être problématique ?

{{
correction(False,
"""
??? success \"Correction\" 
    1. Le Pont de Pierre semble être au Groënland : les EXIF ont été modifiées.
    2. Oui, chaque téléphone permet de désactiver la localisation sur les photos.
    3. Non, les réseaux sociaux filtrent les EXIF.
    4. Par contre, on ne sait pas s'ils les filtrent en local ou sur leurs serveurs.    
"""
)
}}


