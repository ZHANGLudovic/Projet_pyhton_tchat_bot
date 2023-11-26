# README
Introduction
Ce projet comprend plusieurs programmes visant à analyser les discours présidentiels. Les programmes inclus fournissent des fonctionnalités telles que le nettoyage des discours, le calcul du score TF-IDF, et l'analyse de certains aspects spécifiques des discours.

Liste des programmes
'list_of_files': Récupère la liste des fichiers dans un répertoire avec une extension donnée.
'extraire_les_noms': Extrait les noms des présidents à partir des noms de fichiers de discours.
'supprime_numero': Supprime les numéros des noms des présidents.
'associate_president_first_name': Associe les prénoms aux noms des présidents.
'cancel_char_and_majuscule': Réalise des transformations sur les caractères dans les discours.
'tf' : une fonction qui prend en paramètre une chaine de caractères et qui retourne un dictionnaire associant à chaque mot le nombre de fois qu’il apparait dans la chaine de caractères.
'recupere_les_termes': Fonction auxiliaire qui va récupérer tous les termes d'un dossier sans doublons pour IDF
'idf': une fonction qui prend en paramètre le répertoire où se trouve l’ensemble des fichiers du corpus et qui retourne un dictionnaire associant à chaque mot son score IDF
'tf-idf' : une fonction qui prend en paramètre le répertoire où se trouvent les fichiers à analyser et qui retourne au minimum la matrice TF-IDF.
##Partie pratique

On commence par récupéré les noms des fichiers avec 'list_of_file' dans une liste:
