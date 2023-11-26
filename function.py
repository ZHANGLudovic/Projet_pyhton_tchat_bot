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

