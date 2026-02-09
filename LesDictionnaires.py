# Etablis un dictionnaire
traduction = {
    "chien": "dog",
    "chat": "cat",
    "oiseau": "bird",
    "souris": "mouse"
}

inventaire = {
    "pomme": 10,
    "banane": 5,
    "orange": 8
}

dictionnaire_melange = {
   "dict_1": traduction,
   "dict_2": inventaire,
}


# operations sur les dictionnaires
## afficher les valeurs
print(inventaire.values()) # Affiche les valeurs du dictionnaire d'inventaire (10, 5, 8)
## afficher les clés
print(inventaire.keys()) # Affiche les clés du dictionnaire d'inventaire ("pomme", "banane", "orange")
## ajouter un élément
inventaire["kiwi"] = 12 # Ajoute le fruit "kiwi" avec une quantité de 12 au dictionnaire d'inventaire

# les méthodes de dictionnaire
## get récupère la valeur associée à une clé spécifique dans le dictionnaire d'inventaire. Si la clé n'existe pas, elle retourne None ou une valeur par défaut spécifiée.
print(inventaire.get("pomme")) # Affiche la quantité de pommes dans le dictionnaire d'inventaire (10)
print(inventaire.get("fraise", "Non disponible")) # Affiche "Non disponible" car la clé "fraise" n'existe pas dans le dictionnaire d'inventaire 

## fromkeys crée un nouveau dictionnaire avec les clés spécifiées et une valeur par défaut. Ici, un nouveau dictionnaire est créé avec les clés "a", "b" et "c", et une valeur par défaut de 0 pour chacune de ces clés.
nouveau_dict = dict.fromkeys(["a", "b", "c"], 0) # Crée un nouveau dictionnaire avec les clés "a", "b" et "c", et une valeur par défaut de 0 pour chacune de ces clés
print(nouveau_dict) # Affiche le nouveau dictionnaire créé avec fromkeys ({"a": 0, "b": 0, "c": 0})

## pop supprime un élément du dictionnaire d'inventaire en utilisant la clé spécifiée. Ici, l'élément avec la clé "banane" est supprimé du dictionnaire d'inventaire, et la quantité associée à cette clé (5) est retournée.
quantite_banane = inventaire.pop("banane") # Supprime l'élément avec la clé "banane" du dictionnaire d'inventaire et retourne la quantité associée à cette clé (5)
print(quantite_banane) # Affiche la quantité de bananes qui a été supprimée du dictionnaire d'inventaire (5)
print(inventaire) # Affiche le dictionnaire d'inventaire mis à jour après la suppression de l'élément "banane" ({"pomme": 10, "orange": 8, "kiwi": 12}) 


# Utilisation des dictionnaires dans les structures de contrôle
## for avec dictionnaire (get les clés )
for i in inventaire.keys():
    print(i) # Affiche les quantités de chaque fruit dans le dictionnaire d'inventaire, un par ligne (10, 8, 12)

## for avec dictionnaire (get les valeurs )
for i in inventaire.values():
    print(i) # Affiche les quantités de chaque fruit dans le dictionnaire d'inventaire, un par ligne (10, 8, 12)

## for avec dictionnaire (get les clés et les valeurs )
for fruit, quantite in inventaire.items():
    print(fruit, quantite) # Affiche les fruits et leurs quantités dans le dictionnaire d'inventaire, un par ligne (pomme 10, orange 8, kiwi 12). La méthode items() retourne une vue des paires clé-valeur du dictionnaire, ce qui permet d'itérer à la fois sur les clés (fruit) et les valeurs (quantite) dans la boucle for.

# exo sur les dictionnaire (ecris une fonction qui trie les nombres positifs et négatifs dans un dictionnaire avec deux clés "positif" et "negatif")
classeurs = {
    "positif": [],
    "negatif": [],
}
def trier(classeur, nombre):
    if nombre > 0 :
        classeurs["positif"].append(nombre) # Ajoute le nombre à la liste "positif" du dictionnaire classeurs si le nombre est supérieur à 0
    else:        
        classeurs["negatif"].append(nombre) # Ajoute le nombre à la liste "negatif" du dictionnaire classeurs si le nombre est inférieur ou égal à 0
    return classeurs # Retourne le dictionnaire classeurs mis à jour avec le nombre trié dans la liste appropriée ("positif" ou "negatif")
trier(classeurs, 5) # Trie le nombre 5 dans le dictionnaire classeurs, en l'ajoutant à la liste "positif"
trier(classeurs, -3) # Trie le nombre -3 dans le dictionnaire classeurs, en l'ajoutant à la liste "negatif"
print(classeurs) # Affiche le dictionnaire classeurs mis à jour avec les nombres triés dans les listes "positif" et "negatif" ({"positif": [5], "negatif": [-3]})   