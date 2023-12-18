import math
import random
from importlib.metadata import files
import os

def list_of_files(directory, extension): # Fonction pour obtenir la liste des fichiers dans un répertoire avec une certaine extension
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def extraire_les_noms(fichier_txt): # Fonction pour extraire le nom du président à partir du nom de fichier
    nom_du_president = ""
    verificateur = True
    i = 0
    while verificateur:
        if fichier_txt[i] == '_':
            while verificateur:
                i += 1
                if fichier_txt[i] != '.':
                    nom_du_president += fichier_txt[i]
                else:
                    verificateur = False
        i += 1
    return nom_du_president

def supprime_numero(chaine): # Fonction pour supprimer les numéros d'une chaîne de caractères
    lst = ['0','1','2','3','4','5','6','7','8','9']
    new_chaine = ''
    for i in range(len(chaine)):
        if chaine[i] not in lst:
            new_chaine += chaine[i]
    return new_chaine

def supprime_doublon(lst): # Fonction pour supprimer les doublons d'une liste
   i = 0
   while i <= len(lst):
       for j in range(i+1,len(lst)-1):
           if lst[i] == lst[j]:
               lst.remove(lst[j])
       i+=1
   return lst

def associate_president_first_name(president_names): # Fonction pour associer le prénom au nom du président
    president_first_names = {}
    for president in president_names:  # Association des prénoms en fonction des noms de président
        if president=="Chirac":
            president_first_names[president]="Jack"
        elif president=="Hollande":
            president_first_names[president]="Francçois"
        elif president=="Macron":
            president_first_names[president]="Emanuel"
        elif president=="Mitterrand":
            president_first_names[president]="François"
        elif president=="Giscard dEstaing":
            president_first_names[president]="Valery"
        elif president == "Sarkozy":
            president_first_names[president]="Nicolas"

    return president_first_names

def cancel_char_and_majuscule(chaine, indice):
    if ord(chaine) >= 65 and ord(chaine) <= 90 or 97 >= ord(chaine) and 122 <= ord(chaine):
        if ord(chaine) >= 65 and ord(chaine) <= 90:
            return chr(ord(chaine)+32) # Convertit une majuscule en minuscule
        return chaine
    else:
        lst_char = ['.', '!', '?', ';', ':', ',']
        lst_aux = ['d','s','c','n','j','u','t','T','D','S','C','N','J']
        if chaine == '-' and indice == "\n":
            return ''
        elif chaine == '-':
            return ' '    
        elif chaine == '\'' and indice in lst_aux:
            return 'e '
        elif chaine == '\'' and (indice == 'l' or indice == 'L'):
            return random.choice("ae") + ' '
        elif chaine == "\n":
            return ''
        elif chaine not in lst_char:
            return chaine
        else:
            return ' '
def tf(texte): #Cette fonction prend en entrée un texte et renvoie un dictionnaire des fréquences de chaque mot dans le texte.
    texte1 = texte
    dico = {}
    i = 0
    while i < len(texte1):
        if texte1[i] == " ":
            if texte1[0:i] in dico:
                dico[texte1[0:i]] += 1
            else:
                dico[texte1[0:i]] = 1
            texte1 = texte1[i+1:]
            i = 0
        else:
            i+= 1
    return dico

def recupere_les_termes(repertoire): #Cette fonction prend en entrée le chemin d'un répertoire et renvoie une liste de tous les termes uniques dans les fichiers texte de ce répertoire.
    tous_les_termes = []
    lst = list_of_files(repertoire, ".txt") # Liste des noms de fichiers texte dans le répertoire
    texte = ""
    for i in range(len(lst)):
        with open(repertoire + "/" + str(lst[i]), 'r') as f1:
            f_text = f1.readline()  # Lecture de la première ligne du fichier texte
            texte += f_text + ' '
    doc = tf(texte) # Création d'un dictionnaire des fréquences de chaque mot dans le texte
    for key in doc.keys():
        tous_les_termes.append(key) # Ajout de chaque terme unique à la liste 'tous_les_termes'
    return tous_les_termes
    
def IDF(repertoire): # Cette fonction prend en entrée le chemin d'un répertoire et renvoie un dictionnaire des valeurs d'IDF (Inverse Document Frequency) pour chaque terme dans les fichiers du répertoire.
    dic_idf = {}
    frequence_doc = {}# Dictionnaire pour stocker la fréquence de chaque terme dans les documents
    lst = list_of_files(repertoire, ".txt")
    texte = ""
    lst_termes = recupere_les_termes(repertoire) # Liste des termes uniques dans les documents
    for el in lst_termes:   # Initialisation de la fréquence de chaque terme à 0
        frequence_doc[el] = 0
    for i in range(len(lst)):  # Parcours de chaque fichier dans le répertoire
        with open(repertoire + "/" + str(lst[i]), 'r') as f1: 
            f_text = f1.readline()
        texte += f_text + " " # Concaténation du texte du fichier au texte global
        doc = tf(texte)  # Calcul des fréquences des termes dans le texte global
        for el in doc.keys():
            if el in frequence_doc.keys():
                frequence_doc[el] += 1 # Mise à jour de la fréquence de chaque terme
    for key, values in frequence_doc.items():     # Calcul des valeurs d'IDF pour chaque terme
        dic_idf[key] = math.log10((len(lst) / values)+1)
    return dic_idf



def tf_IDF(directory):
    idf_dico = IDF(directory)  # Calcul des valeurs IDF pour chaque terme dans le répertoire
    tfidf_matrix = []
    lst_aux = []  # Liste auxiliaire pour stocker les valeurs TF-IDF pour chaque document
    lst = list_of_files(directory, ".txt")  # Liste des noms de fichiers dans le répertoire
    all_words = recupere_les_termes(directory) 
    for mot in all_words:
        for j in range(len(lst)):
            with open(directory + "/" + str(lst[j]), 'r') as f1:
                f_text = f1.readline()
            doc = tf(f_text)  # Calcul des fréquences de chaque terme dans le document
            if mot in doc.keys():
                lst_aux.append(doc[mot] * idf_dico[mot])  # Calcul de la valeur TF-IDF pour le terme dans le document
            else:
                lst_aux.append(0)  # Si le terme n'est pas présent dans le document, la valeur TF-IDF est 0
        tfidf_matrix.append(lst_aux) 
        lst_aux = []  # Réinitialisation de la liste auxiliaire pour le prochain terme
    return tfidf_matrix 

# Fonction de tokenisation pour diviser un texte en liste de mots
def tokenisation(txt):
    nex_txt = ""  # Chaîne de caractères pour stocker le texte traité
    aux_txt = ""  # Chaîne de caractères auxiliaire pour construire chaque mot
    lst = []      # Liste pour stocker les mots extraits du texte

    # Parcours du texte pour créer une version modifiée avec suppression de certains caractères
    for i in range(len(txt)):
        nex_txt += cancel_char_and_majuscule(txt[i], txt[i-1])

    # Parcours de la version modifiée pour extraire les mots
    for i in range(len(nex_txt)):
        if nex_txt[i] != " ":
            aux_txt += nex_txt[i]
        elif aux_txt:
            lst.append(aux_txt)
            aux_txt = ""

    return lst


# Fonction pour obtenir l'intersection de deux listes
def intersection(lst, repertoire):
    all_words = recupere_les_termes(repertoire)
    new_lst = []

    # Parcours de la liste fournie en paramètre
    for i in range(len(lst)):
        if lst[i] in all_words:
            new_lst.append(lst[i])

    return new_lst


# Fonction pour calculer le vecteur TF-IDF d'un texte dans un répertoire donné
def vecteur_tf_idf(txt, repertoire):
    vecteur_tf_idf = []  # Liste pour stocker les valeurs TF-IDF
    all_words = recupere_les_termes(repertoire)
    dic = {}             # Dictionnaire pour stocker les fréquences des termes
    lst_intersection = intersection(tokenisation(txt), repertoire)
    dico_tf = tf(txt)
    dic_idf = IDF(repertoire)
    var_aux = 0

    # Initialisation du dictionnaire avec les termes présents dans le texte
    for i in range(len(all_words)):
        if all_words[i] not in lst_intersection:
            dic[all_words[i]] = 0
        else:
            dic[all_words[i]] = dico_tf[all_words[i]] / len(tokenisation(txt))

    # Calcul du vecteur TF-IDF pour chaque terme
    for i in range(len(all_words)):
        var_aux = dic[all_words[i]] * dic_idf[all_words[i]]
        vecteur_tf_idf.append((var_aux))

    return vecteur_tf_idf


# Fonction pour calculer la norme d'un vecteur
def norme(vecteur):
    sum = 0

    # Parcours des éléments du vecteur et calcul de la somme des carrés
    for el in vecteur:
        sum += el ** 2

    return sqrt(sum)


# Fonction pour calculer le produit scalaire entre deux vecteurs
def produit_scalaire(lst, lst_1):
    produit_scalaire_result = 0

    # Parcours des éléments des deux listes et calcul du produit scalaire
    for i in range(len(lst)):
        produit_scalaire_result += lst[i] * lst_1[i]

    return produit_scalaire_result


# Fonction pour calculer la similarité cosinus entre deux vecteurs
def similarite_cosinus(lst, lst_1):
    produit = produit_scalaire(lst, lst_1)
    norme_1 = norme(lst)
    norme_2 = norme(lst_1)

    # Vérification pour éviter une division par zéro
    if norme_2 != 0 and norme_1 != 0:
        return produit / (norme_1 * norme_2)

    return 0


# Fonction pour trouver le document le plus pertinent par rapport à une question
def plus_pertinent(matrice_tf_idf, lst_question, directory):
    lst = list_of_files(directory, ".txt")
    lst_aux = []
    lst_aux_2 = []
    comparateur = 0
    idx = 0

    # Parcours des colonnes de la matrice TF-IDF pour chaque document
    for i in range(8):
        for j in range(len(matrice_tf_idf)):
            lst_aux.append(matrice_tf_idf[j][i])
        lst_aux_2.append(lst_aux)
        lst_aux = []

    # Comparaison de la similarité cosinus pour trouver le document le plus pertinent
    for i in range(len(lst_aux_2)):
        if comparateur < similarite_cosinus(lst_aux_2[i], lst_question):
            comparateur = similarite_cosinus(lst_aux_2[i], lst_question)
            idx = i

    return lst[idx]


# Fonction pour trouver le terme avec le plus grand TF-IDF dans un vecteur
def plus_grand_tf_idf(lst, directory):
    all_words = recupere_les_termes(directory)
    comparateur = lst[0]
    idx = 0

    # Parcours de la liste pour trouver le terme avec le plus grand TF-IDF
    for i in range(len(lst)):
        if lst[i] > comparateur:
            comparateur = lst[i]
            idx = i

    return all_words[idx]


# Fonction pour trouver la première chaîne qui contient un mot spécifié
def chaine_contient_mot(mot, lst):
    for i in range(len(lst)):
        if mot in lst[i]:
            return lst[i]


# Fonction pour fournir une réponse à une question à partir de deux répertoires et d'une liste de noms de fichiers
def reponse(directory_1, directory_2, question, tfidf_lst, files_names):
    lst = list_of_files(directory_1, ".txt")
    fichier = plus_pertient(tfidf_lst, vecteur_tf_idf(question, directory_1), directory_1)
    mot = plus_grand_tf_idf(vecteur_tf_idf(question, directory_1), directory_1)

    # Recherche du fichier correspondant au document le plus pertinent
    for el in lst:
        if el == fichier:
            with open(directory_2 + str(el), 'r', encoding="utf-8") as f1:
                lst = f1.readlines()
                return chaine_contient_mot(mot, lst)


# Fonction pour mettre en page la réponse en fonction du type de question
def mise_en_page(question):
    question_starters = {
        "Comment": "Après analyse, ",   # Mise en page pour les questions commençant par "Comment"
        "Pourquoi": "Car, ",            # Mise en page pour les questions commençant par "Pourquoi"
        "Peux-tu": "Oui, bien sûr! "     # Mise en page pour les questions commençant par "Peux-tu"
    }

    # Parcours des déclencheurs de question et ajout de la mise en page correspondante
    for key, values in question_starters.items():
        if key in question:
            return values

    return "On peut dire"   # Mise en page par défaut
