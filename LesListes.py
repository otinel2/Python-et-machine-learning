#Définir une liste de nombres
nombres = [1, 2, 3, 4, 5]
print(nombres) # Affiche la liste de nombres

#définir une liste de chaînes de caractères
fruits = ["pomme", "banane", "orange"]
print(fruits) # Affiche la liste de fruits

# liste dans une liste
liste_melangee = [nombres, fruits]
print(liste_melangee) # Affiche la liste mélangée contenant les listes de nombres et de fruits

liste_vide = [] # Affiche une liste vide
print(liste_vide) # Affiche la liste vide

# tuple
mon_tuple = (1, 2, 3) # Affiche un tuple de nombres

# String
mon_string = "otinel" # Affiche une chaîne de caractères

#  Indexation
print(nombres[0]) # Affiche le premier élément de la liste de nombres (1)
print(fruits[-1]) # Affiche le dernier élément de la liste de fruits ("orange")
print(liste_melangee[0][2]) # Affiche le troisième élément de la première liste dans la liste mélangée (3)

# Slicing
print(nombres[1:4]) # Affiche les éléments de la liste de nombres de l'index 1 à 3 (2, 3, 4)
print(fruits[:2]) # Affiche les deux premiers éléments de la liste de fruits ("pomme", "banane")
print(nombres[2:]) # Affiche les éléments de la liste de nombres à partir de l'index 2 jusqu'à la fin (3, 4, 5)
print(nombres[::2]) # Affiche les éléments de la liste de nombres en sautant un élément (1, 3, 5)

# les méthodes de liste
## Ajouter un élément à la fin de la liste
nombres.append(6) # Ajoute le nombre 6 à la fin de la liste de nombres
print(nombres) # Affiche la liste de nombres mise à jour avec le nombre 6

## Insérer un élément à une position spécifique
fruits.insert(1, "kiwi") # Insère le fruit "kiwi" à l'index 1 de la liste de fruits
print(fruits) # Affiche la liste de fruits mise à jour avec "kiwi"

## extendre une liste avec une autre liste
nombres.extend([7, 8, 9]) # Ajoute les nombres 7, 8 et 9 à la fin de la liste de nombres
print(nombres) # Affiche la liste de nombres mise à jour avec les nombres 7

## len Affiche la longueur de la liste de nombres
print(len(nombres)) # Affiche la longueur de la liste de nombres (9)


## Sort trie la liste de fruits par ordre alphabétique
fruits.sort() # Trie la liste de fruits par ordre alphabétique
print(fruits) # Affiche la liste de fruits triée par ordre alphabétique

## sort reverse trie la liste de fruits par ordre alphabétique inverse
fruits.sort(reverse=True) # Trie la liste de fruits par ordre alphabétique inverse

print(fruits) # Affiche la liste de fruits triée par ordre alphabétique inverse


## count compte le nombre d'occurrences d'un élément dans la liste de fruits
print(fruits.count("kiwi")) # Affiche le nombre d'occurrences du fruit "kiwi" dans la liste de fruits (1)

# liste dans les sturctures de contrôle
## liste avec if et else
if "kiwi" in fruits: 
    print('oui')
else:    print('non') # Affiche "oui" si le fruit "kiwi" est présent dans la liste de fruits, sinon affiche "non"

## liste avec for
for fruit in fruits: 
    print(fruit) # Affiche chaque fruit de la liste de fruits, un par ligne


## enumerate avec for
for index, fruit in enumerate(fruits):
    print(index, fruit) # Affiche l'index et le fruit de la liste de fruits, un par ligne. La fonction enumerate() permet d'obtenir à la fois l'index et la valeur de chaque élément de la liste lors de l'itération avec la boucle for.    

## liste avec zip
nombres2 = [10, 20, 30]
for nombre, fruit in zip(nombres2, fruits):
    print(nombre, fruit) # Affiche le nombre et le fruit de deux listes différentes, un par ligne. La fonction zip() permet de combiner les éléments de deux listes en une seule séquence de tuples, où chaque tuple contient un élément de chaque liste. Lors de l'itération avec la boucle for, chaque tuple est décomposé en ses éléments respectifs (nombre et fruit) pour être affiché.


# exo sur les listes (ecris la fonction de fibonacci qui retourne les 10 premiers nombres de la séquence de Fibonacci dans une list)
def fibonacci(n):
    liste_fibonacci = []
    x = 0
    y =1
    for i in range(n):
        liste_fibonacci.append(x) # Ajoute le nombre actuel de la séquence de Fibonacci à la liste
        x, y = y, x + y # Met à jour les valeurs de x et y pour le prochain nombre de la séquence de Fibonacci
    return liste_fibonacci # Retourne la liste contenant les nombres de la séquence de Fibonacci
print(fibonacci(10)) # Affiche les 10 premiers nombres de la séquence de Fibonacci dans une liste