from function import *

# Récupération des noms de fichiers et nettoyage des noms
if __name__ == '__main__':
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    lst_des_noms = []
    for idx in range(len(files_names)):
        lst_des_noms.append(extraire_les_noms(files_names[idx]))
    for idx in range(len(lst_des_noms)):
        lst_des_noms[idx] = supprime_numero(lst_des_noms[idx])
    supprime_doublon(lst_des_noms)
    dict_nom_prenom = associate_president_first_name(lst_des_noms)
    for i in range(len(files_names)):
        with open("Cleaned/"+str(files_names[i]), 'w') as f1, open("speeches/"+str(files_names[i]),'r') as f2:
            lst = f2.read()
            for j in range(len(lst)):
                f1.write(str(cancel_char_and_majuscule(lst[j],lst[j-1])))


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




    tfidf_lst = tf_IDF("Cleaned")
    all_words = recupere_les_termes("Cleaned")
    #Affiche la liste de mot avec le score tf-idf le moins eleve
    if valeurs_numerique == 1:
        n = int(input("Saisissez la taille de la liste souhaité: "))
        lst_tfidf_non_important = [0,0,0,0,0,0,0,0]
        lst_tfidf_moins_important = []
        for i in range(n):
            comparateur = tfidf_lst[0]
            idx = 0
            for j in range (1,len(all_words)):
                if tfidf_lst[j] < comparateur and all_words[j] not in lst_tfidf_moins_important and tfidf_lst[j]!= lst_tfidf_non_important :
                    comparateur = tfidf_lst[j]
                    idx = j
            lst_tfidf_moins_important.append(all_words[idx])
        print("La liste des mots de taille {0} avec le score tf-idf les moins élevés sont: {1} ".format(n,lst_tfidf_moins_important))

    #Affiche le mot avec le score tf-idf le plus eleve
    if valeurs_numerique == 2:
        lst_eleve = []
        comparateur = tfidf_lst[0]
        for i in range(1,len(tfidf_lst)):
            if tfidf_lst[i] > comparateur and all_words[i] != '':
                comparateur = tfidf_lst[i]
        for idx in range(len(tfidf_lst)):
            if tfidf_lst[idx] == comparateur:
                lst_eleve.append(all_words[idx])
        print("Le mot avec le score tf-idf le plus eleve est : {0}".format(lst_eleve))

    #Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac

    if valeurs_numerique == 3:
        text = ""
        for i in range (0,2):
            with open ("Cleaned/"+str(files_names[i]), 'r') as f1:
                f_text = f1.readline()
                text += f_text + ' '
        with open("chirac/"+"Nominated.chirac", 'w') as f2:
            f2.write(f_text)
        with open("chirac/"+"Nominated.chirac", 'r') as f3:
            dico = tf(f3.readline())
            comp = 0
            word = ""
            for key,value in dico.items():
                if comp < value:
                    comp = value
                    word = key
        print("Le mot le plus répété par Chirac est: {0}".format(word))

#Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois

    if valeurs_numerique == 4:
        lst = []
        mot = "nation"
        lst_presidents = []
        for i in range(len(files_names)):
            with open("Cleaned/"+str(files_names[i]), 'r') as f1:
                f_text = f1.readline()
            dico = tf(f_text)
            if mot in dico.keys():
                lst_presidents.append((str(supprime_numero(extraire_les_noms(str(files_names[i]))))))
        print("Le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation est : {0}»".format(supprime_doublon(lst_presidents)))
        for i in range(len( all_words)):
            if all_words[i] == "nation":
                lst = tfidf_lst[i]
        comp = lst[0]
        indice = 0
        for i in range(1,len(lst)):
            if lst[i]> comp:
                comp = lst[i]
                indice = i
        print("Et celui qui la répété le plus de fois est : {0}".format(supprime_numero(extraire_les_noms(files_names[indice]))))

#Indiquer le premier président à parler du climat et/ou de l’écologie

    if valeurs_numerique == 5:
        verificateur = True
        president_climat = ""
        mot = "climat"
        for i in range(len(files_names)):
            with open("Cleaned/"+str(files_names[i]), 'r') as f1:
                f_text = f1.readline()
                dico = tf(f_text)
                if mot in dico.keys() and verificateur:
                    print("Le premier président à parler du climat et/ou de l’écologie est : {0}".format(str(supprime_numero(extraire_les_noms(str(files_names[i]))))))
                    verificateur = False

#Hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqués.

    if valeurs_numerique == 6:
        lst_mot_commun = []
        for i in range(len(all_words)):
            if 0 not in tfidf_lst[i]:
                lst_mot_commun.append(all_words[i])
        print ("les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqués sont : {0}".format(lst_mot_commun))

