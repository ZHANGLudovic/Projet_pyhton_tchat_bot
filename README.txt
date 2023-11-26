#README
Introduction
Ce projet comprend plusieurs programmes visant à analyser les discours présidentiels. Les programmes inclus fournissent des fonctionnalités telles que le nettoyage des discours, le calcul du score TF-IDF, et l'analyse de certains aspects spécifiques des discours.

# Groupe: ZHANG Ludovic

#Information
Il existe un fichier pour les fonctions on sont stocké toutes les fonctions nommée 'function' et un fichier 'main' contenant le programme principale.


##Liste des programmes
'list_of_files': Récupère la liste des fichiers dans un répertoire avec une extension donnée.
'extraire_les_noms': Extrait les noms des présidents à partir des noms de fichiers de discours.
'supprime_doublons': Supprime les doublons lorsqu'il y a plussieurs fois le même nom du présidents
'supprime_numero': Supprime les numéros des noms des présidents.
'associate_president_first_name': Associe les prénoms aux noms des présidents.
'cancel_char_and_majuscule': Réalise des transformations sur les caractères dans les discours.
'tf' : une fonction qui prend en paramètre une chaine de caractères et qui retourne un dictionnaire associant à chaque mot le nombre de fois qu’il apparait dans la chaine de caractères.
'recupere_les_termes': Fonction auxiliaire qui va récupérer tous les termes d'un dossier sans doublons pour IDF
'idf': une fonction qui prend en paramètre le répertoire où se trouve l’ensemble des fichiers du corpus et qui retourne un dictionnaire associant à chaque mot son score IDF
'tf-idf' : une fonction qui prend en paramètre le répertoire où se trouvent les fichiers à analyser et qui retourne au minimum la matrice TF-IDF.


##Partie pratique
On commence par récupéré les noms des fichiers avec 'list_of_file' dans une liste.
Par la suite, on récupère les Noms et associe les prénoms des présidents dans un dictionnaire avec les fonctions 'supprime_numero', 'supprime_doublons' et 'associate_president_first_name'
Ensuite, dans un dossier cleaned on ajoute les fichiers de 'speeches' en enlevant les mmajuscules en minuscules et en enlevant les toutes ponctuations avec cancel_char_and_majuscule

Pour crée le menu, on affiche les instructions mais également une valeurs à saisir pour intéragire avec le code avec les différents 'if'.

Pour obtenir la liste des mots avec le score tf-idf la plus faible, on leur demande de saisir la taille de la liste de mot, on cherche le plus petit score tf-idf, puis avec son indice on ajoute dans une liste le mot corespondant au score tf-idf et on répete ce schema en vérifiant que le mot suivant n'est pas deja dans la liste.

Pour obtenir le score tf-idf le plus élevé il nous suffit de faire un comparateur est si le score tf-idf est supèrieur au comparateur on associe au comparateur son score et on garde l'indice pour ajouter le mot avec le score le plus élevé/

Pour trouvé le mot dit le plus de fois par Chirac on a commencé par réunir en un discour les 2 fichiers du discour de Chirac d'ou le nouveau dossier 'chirac' où on utilise 'tf' pour connaitre le mot où le nombre d'occurence est le plus élevé.

Pour indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation », on commence par parcourir chaque fichier et pour chaque fichier on utilise tf afin d'obtenir tous les mots du fichier, on cherche si nation apparait dans les clés de 'doc' losqu'on applique tf et si elle apparait on ajoute le nom du président dans la liste en appliquant les fonctions 'extraire_les nom ...'
Enfin pour connaitre celui qui l’a répété le plus de fois on cherche l'indice du mot 'nation' dans all_words(varriable contenant tous les mots du dossier) pour connaitre son score tf-idf et on cherche simplement qu'elle fichier à le score tf-idf le plus élevé avec un simple comparateur.

Pour indiquer le premier président à parler du climat et/ou de l’écologie, on commence par parcourir chaque fichier et pour chaque fichier on utilise tf afin d'obtenir tous les mots du fichier, on cherche si 'climat' apparait dans les clés de 'doc', si elle apparait on arrète la fonction avec un booléen et on affiche le nom du président dans la liste en appliquant les fonctions 'extraire_les nom ...'

Pour le(s) mot(s) que tous les présidents ont évoqués, on parcours la matrice tf-idf et on affiche les mots toujours dans all_words où son score tf-idf n'a aucun zero.


#Lien Github: https://github.com/ZHANGLudovic/Projet_pyhton_tchat_bot
