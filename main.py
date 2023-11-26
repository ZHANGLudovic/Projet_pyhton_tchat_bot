from function import *


if __name__ == '__main__':
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")     # Liste des noms de fichiers avec l'extension "txt"
    lst_des_noms = [] 
    for idx in range(len(files_names)): # Extraction des noms de chaque fichier
        lst_des_noms.append(extraire_les_noms(files_names[idx]))
    for idx in range(len(lst_des_noms)):  # Suppression des numéros des noms extraits
        lst_des_noms[idx] = supprime_numero(lst_des_noms[idx])
    supprime_doublon(lst_des_noms)
    dict_nom_prenom = associate_president_first_name(lst_des_noms)     # Création d'un dictionnaire associant les noms et prénoms
    for i in range(len(files_names)): # Nettoyage des discours et sauvegarde dans des fichiers Cleaned
        with open("Cleaned/"+str(files_names[i]), 'w') as f1, open("speeches/"+str(files_names[i]),'r') as f2:
            lst = f2.read()             # Lecture du discours original
            for j in range(len(lst)):               # Écriture du discours nettoyé dans le fichier Cleaned
                f1.write(str(cancel_char_and_majuscule(lst[j],lst[j-1])))

    # Affichage des instructions pour le chatbot

    
    print("                   Bienvenu dans le tchatbot: Partie 1")
    print("Veuillez respecter les règles suivantes pour une meilleurs expèrience.")
    print("-Taper 1: Afficher la liste des mots avec le score tf-idf le moins eleve")
    print("-Taper 2: Afficher la liste de mot avec le score tf-idf le plus eleve")
    print("-Taper 3: Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac")
    print("-Taper 4: Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois")
    print("-Taper 5: Indiquer le premier président à parler du climat et/ou de l’écologie")
    print("-Taper 6: Afficher quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqués")
    print(("Le chargement peut-être un peu long merci de prendre cela en considération"))
    valeurs_numerique = int(input("Saisissez des chiffre entre 1 à 6  pour accéder au diverse fonctionnalité du tchatbot: "))




    tfidf_lst = tf_IDF("Cleaned") # Calcul du TF-IDF et récupération des termes du discours nettoyé
    all_words = recupere_les_termes("Cleaned") 
    #Affiche la liste de mot avec le score tf-idf le moins eleve
    if valeurs_numerique == 1:
        n = int(input("Saisissez la taille de la liste souhaité: "))
        lst_tfidf_non_important = [0,0,0,0,0,0,0,0]     # Initialisation des listes pour stocker les résultats
        lst_tfidf_moins_important = []
        for i in range(n): # Boucle pour sélectionner les mots avec les scores TF-IDF les moins élevés
            comparateur = tfidf_lst[0]
            idx = 0
            for j in range (1,len(all_words)):
                if tfidf_lst[j] < comparateur and all_words[j] not in lst_tfidf_moins_important and tfidf_lst[j]!= lst_tfidf_non_important : # Vérification des conditions pour sélectionner le mot
                    comparateur = tfidf_lst[j]
                    idx = j
            lst_tfidf_moins_important.append(all_words[idx])
        print("La liste des mots de taille {0} avec le score tf-idf les moins élevés sont: {1} ".format(n,lst_tfidf_moins_important)) # Affichage de la liste des mots avec les scores TF-IDF les moins élevés

    #Affiche le mot avec le score tf-idf le plus eleve
    if valeurs_numerique == 2:
        lst_eleve = []     # Initialisation de la liste pour stocker le mot avec le score TF-IDF le plus élevé
        comparateur = tfidf_lst[0] # Initialisation du comparateur
        for i in range(1,len(tfidf_lst)): # Boucle pour trouver le mot avec le score TF-IDF le plus élevé
            if tfidf_lst[i] > comparateur and all_words[i] != '':
                comparateur = tfidf_lst[i]
        for idx in range(len(tfidf_lst)): # Boucle pour ajouter les mots avec le score TF-IDF le plus élevé à la liste
            if tfidf_lst[idx] == comparateur:
                lst_eleve.append(all_words[idx])
        print("Le mot avec le score tf-idf le plus eleve est : {0}".format(lst_eleve))

    #Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac

    if valeurs_numerique == 3:
        text = ""   # Initialisation de la variable texte
        for i in range (0,2): # Boucle pour lire les deux premiers fichiers Cleaned de Chirac
            with open ("Cleaned/"+str(files_names[i]), 'r') as f1:
                f_text = f1.readline()
                text += f_text + ' ' 
        with open("chirac/"+"Nominated.chirac", 'w') as f2: # Sauvegarde du texte dans un fichier Nominated.chirac
            f2.write(f_text)
        with open("chirac/"+"Nominated.chirac", 'r') as f3: # Lecture du fichier Nominated.chirac et création d'un dictionnaire de fréquence
            dico = tf(f3.readline())
            comp = 0
            word = ""
            for key,value in dico.items():  # Boucle pour trouver le mot le plus répété par Chirac
                if comp < value:
                    comp = value
                    word = key
        print("Le mot le plus répété par Chirac est: {0}".format(word))

#Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois

    if valeurs_numerique == 4:
        lst = [] 
        mot = "nation"
        lst_presidents = []
        for i in range(len(files_names)): # Boucle pour parcourir tous les fichiers Cleaned
            with open("Cleaned/"+str(files_names[i]), 'r') as f1:
                f_text = f1.readline()
            dico = tf(f_text) # Création d'un dictionnaire de fréquence pour le mot "nation"
            if mot in dico.keys():  # Vérification de la présence du mot "nation" dans le discours
                lst_presidents.append((str(supprime_numero(extraire_les_noms(str(files_names[i])))))) # Ajout du nom du président à la liste
        print("Le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation est : {0}»".format(supprime_doublon(lst_presidents)))
        for i in range(len( all_words)): # Recherche du président qui a répété le plus de fois le mot "nation"
            if all_words[i] == "nation":
                lst = tfidf_lst[i]
        comp = lst[0]
        indice = 0
        for i in range(1,len(lst)): # Boucle pour trouver le président qui a répété le plus de fois le mot "nation"
            if lst[i]> comp:
                comp = lst[i]
                indice = i
        print("Et celui qui la répété le plus de fois est : {0}".format(supprime_numero(extraire_les_noms(files_names[indice])))) 

#Indiquer le premier président à parler du climat et/ou de l’écologiecsdsdfsdfsdffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff

    if valeurs_numerique == 5:
        verificateur = True # Initialisation du vérificateur et de la variable président_climat
        president_climat = ""
        mot = "climat"
        for i in range(len(files_names)): # Boucle pour parcourir tous les fichiers Cleaned
            with open("Cleaned/"+str(files_names[i]), 'r') as f1:
                f_text = f1.readline()
                dico = tf(f_text)
                if mot in dico.keys() and verificateur: # Vérification de la présence du mot "climat" dans le discours et du vérificateur
                    print("Le premier président à parler du climat et/ou de l’écologie est : {0}".format(str(supprime_numero(extraire_les_noms(str(files_names[i]))))))
                    verificateur = False

#Hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqués.

    if valeurs_numerique == 6:
        lst_mot_commun = []  # Initialisation de la liste pour stocker les mots communs
        for i in range(len(all_words)): # Vérification si le terme a un score TF-IDF non nul
            if 0 not in tfidf_lst[i]:
                lst_mot_commun.append(all_words[i])# Ajout du terme à la liste des mots communs
        print ("les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqués sont : {0}".format(lst_mot_commun))

