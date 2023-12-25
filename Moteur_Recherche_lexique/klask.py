# coding=utf-8
#Le commentaire précédent permet d'éviter les erreurs d'affichage.

#Pour convertir le fichier CSV en dictionnaire
import csv 

#Défini le chemin où se trouve le fichier CSV (fonctionne seulement s'il est dans le même dossier que ce script.
from inspect import getsourcefile
  
import os

def to_raw(string):
    return fr"{string}"
    
#initialisation du dictionnaire et création à partir du fichier CSV
dico = {}

path_CSV = to_raw(os.path.dirname(getsourcefile(lambda:0))+ r"\Geriaoueg_Jean_Marot_source.csv")

with open(path_CSV, mode="r", encoding="ANSI") as entrée:
    lecture = csv.reader(entrée)
    dico = {colonne[0]: colonne[1] for colonne in lecture}

#Recherche dans le lexique
print("Ne pas écrire de majuscules et respecter les accents, le ñ, lire les commentaires au début de ce script.")

continuer = "1"
while (continuer == "1"):
    j = 0
    print("Entrez un terme à chercher : ") 
    terme = input()
    print(f"Voici la liste des entrées dans lesquelles ont été trouvé \"{terme}\" : ")
    for i in dico :
        if (list(dico.keys())[j].__contains__(terme)):
            print("· "+ i + " : " + dico[i])
        elif (dico[i].__contains__(terme)) :
            print("· "+ dico[i] + " : " + i)
        j = j+1
    continuer = input("Voulez-vous faire une nouvelle recherche ? 0 : Non ; 1 : Oui ")