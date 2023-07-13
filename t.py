# import os  
import glob

path = input("Quel est le chemin d'accès du dossier: ")
regex = input("Quel type de fichier cherchez vous ? Ex: \*.py :")
response = "n"
tab= []
tab.append(regex)
while response is "false":
    response = input("Un autre type fichier à ajouter ? o/n")
    if response is "n":
        regex = input("Quel type de fichier cherchez vous ? Ex: \*.py :")
        tab.append(regex)


# chercher par extensions ? ensuite renommer ?
targetPattern = r"{}{}".format(path,regex)
print(glob.glob(targetPattern))




