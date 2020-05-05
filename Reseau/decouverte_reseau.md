### 0. Préambule

Dans ce chapitre, il fera appel de nombreuses fois au logiciel de simulation réseau Filius.  
Vous pouvez le télécharger :
- version Windows : [ici](https://www.lernsoftware-filius.de/downloads/Setup/Filius-Setup-1.9.0.exe)
- version Linux : [ici](https://www.lernsoftware-filius.de/downloads/Setup/filius_1.9.0_all.deb)
- version Mac : il n'y en a pas, désolé.

Ce n'est pas obligatoire de l'installer pour suivre ce cours, mais cela rendra le cours plus interactif d'avoir Filius à portée de main pour voir en direct les réactions du réseau.

Filius est très intuitif dans sa manipulation. Signalons juste la présence de deux modes : 
- le mode Conception, matérialisé par l'icone ![](data/conception.png) 
- le mode Simulation, matérialisé par l'icone ![](data/simulation.png) 

### 1. Un premier réseau local

Créons le réseau local ci-dessous :

![](data/f1.png)

Testons le ```ping``` de la machine ```192.168.0.1```  vers la machine ```192.168.0.3```.  
Il est nécessaire pour cela d'installer la «ligne de commande», en mode simulation.

**Résultat :**

![](data/ping1.png)

Le vocabulaire pour comprendre :

- **Adresse IP** : lorsque nous avons créé le réseau, nous avons attribué à chaque ordinateur une adresse, dite **adresse IP**, composée (pour l'IPv4)
de 4 nombres entre 0 et 255, séparés par un point. Exemple : 123.0.168.255 est une adresse IP valide, 156.286.3.16 n'est pas une adresse IP valide.
Ces adresses servent à identifier un ordinateur sur un réseau. Nous verrons plus tard qu'elles permettent aussi de savoir à quel sous-réseau l'ordinateur appartient, mais c'est une autre histoire. 

<br>

- **ping** : on appelle un **ping** l'action d'envoyer sur le réseau un tout petit message, dont l'utilité est juste de vérifier si la connexion entre deux ordinateurs est opérante. En réalité, on envoie un ping, on reçoit un pong, ce qui permet de voir que la connexion est ok. Dans la fenêtre ci-dessus, 4 «paquets» ont été envoyés, et bien ré-envoyés.  
Les ordinateurs ```192.168.0.1```  vers la machine ```192.168.0.3``` sont bien connectés et peuvent s'échanger des informations.

#### 1.1. La carte réseau et son adresse MAC
Chaque ordinateur sur le réseau dispose d'une adresse MAC, qui une valeur **unique** attribuée à sa carte réseau (Ethernet, Wifi, 4G, 5G, ...) lors de sa fabrication en usine.

Cette adresse est codée sur 48 bits, présentés sous la forme de 6 octets en hexadécimal. Exemple : ```fc:aa:14:75:45:a5```

Les trois premiers octets correspondent au code du fabricant.
Un site comme https://www.macvendorlookup.com/ vous permet de retrouver le fabricant d'une adresse MAC quelconque.

#### 1.2. Switch, hub, quelle différence ?

- Au sein d'un **hub Ethernet** (de moins en moins vendus), il n'y a **aucune analyse** des données qui transitent : il s'agit simplement d'un dédoublement des fils de cuivre (tout comme une multiprise électrique). L'intégralité des messages est donc envoyée à l'intégralité des ordinateurs du réseau, même s'ils ne sont pas concernés.

![](data/hub.png)

- Au sein d'un **switch Ethernet** , une analyse est effectuée sur la trame qui est à distribuer (voir [ici](https://github.com/glassus/nsi/blob/master/Premiere/Theme04_Architecture_materielle/04_Protocoles_de_communication.md)). Lors d'un branchement d'un nouvel ordinateur sur le switch, celui-ci récupère son adresse MAC, ce qui lui permet de **trier** les messages et de ne les distribuer qu'au bon destinataire.

![](data/switch.png)

----
