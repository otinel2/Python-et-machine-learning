# # list comprehension
# ## créer une liste de carrés de nombres de 0 à 9
# carrés = [x**2 for x in range(10)] # Crée une liste de carrés de nombres de 0 à 9 en utilisant une compréhension de liste. La syntaxe [x**2 for x in range(10)] génère une nouvelle liste en itérant sur les nombres de 0 à 9 (générés par range(10)) et en calculant le carré de chaque nombre (x**2) pour l'ajouter à la liste carrés.
# print(carrés) # Affiche la liste de carrés de nombres de 0 à

# ## Nested list comprehension
# ## créer une matrice 3x3 avec des zéros
# matrice = [[i for i in range(3)] for j in range(3)] # Crée une matrice 3x3 remplie de zéros en utilisant une compréhension de liste imbriquée. La syntaxe [[0 for j in range(3)] for i in range(3)] génère une nouvelle liste qui contient trois sous-listes (une pour chaque ligne de la matrice), et chaque sous-liste contient trois éléments (des zéros) générés par la compréhension de liste interne [0 for j in range(3)].
# print(matrice) # Affiche la matrice 3x3 remplie de zéros ([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

# # dictionnaire comprehension
# prenoms = ["Alice", "Bob", "Charlie"]
# dico = {k:v for k, v in enumerate(prenoms)} # Crée un dictionnaire en utilisant une compréhension de dictionnaire. La syntaxe {k:v for k, v in enumerate(prenoms)} génère une nouvelle paire clé-valeur pour chaque élément de la liste prenoms, où la clé (k) est l'index de l'élément dans la liste (généré par enumerate(prenoms)) et la valeur (v) est l'élément lui-même (le prénom).
# print(dico) # Affiche le dictionnaire créé à partir de la liste de prénoms ({0: "Alice", 1: "Bob", 2: "Charlie"})

# ## zip et dict comprehension
# ages = [25, 30, 35]
# dict_zip = {prenom:age for prenom, age in zip(prenoms, ages)} # Crée un dictionnaire en utilisant une compréhension de dictionnaire et la fonction zip. La syntaxe {prénom:age for prenom, age in zip(prenoms, ages)} génère une nouvelle paire clé-valeur pour chaque élément combiné des listes prenoms et ages, où la clé (k) est le prénom (généré par zip(prenoms, ages)) et la valeur (v) est l'âge correspondant.
# print(dict_zip) # Affiche le dictionnaire créé à partir des listes de prénoms et d'âges ({"Alice": 25, "Bob": 30, "Charlie": 35})

# ## dictionnaire comprehension avec condition
# dict_condition = {prenom:age for prenom, age in zip(prenoms, ages) if age > 28} # Crée un dictionnaire en utilisant une compréhension de dictionnaire avec une condition. La syntaxe {prenom:age for prenom, age in zip(prenoms, ages) if age > 28} génère une nouvelle paire clé-valeur pour chaque élément combiné des listes prenoms et ages, mais seulement si l'âge est supérieur à 28 (condition if age > 28).
# print(dict_condition) # Affiche le dictionnaire créé à partir des listes de prénoms et d'âges, mais uniquement pour les âges supérieurs à 28 ({"Bob": 30, "Charlie": 35})

# # tuple comprehension
# ## créer une liste de tuples (nombre, carré) pour les nombres de 0 à 9
# tuples_1 = tuple((x, x**2) for x in range(10)) # Crée une liste de tuples (nombre, carré) pour les nombres de 0 à 9 en utilisant une compréhension de générateur. La syntaxe tuple((x, x**2) for x in range(10)) génère une nouvelle séquence de tuples en itérant sur les nombres de 0 à 9 (générés par range(10)) et en créant un tuple (x, x**2) pour chaque nombre, où x est le nombre lui-même et x**2 est son carré.
# print(tuples_1) # Affiche la liste de tuples (nombre, carré) pour les nombres de 0 à 9 ((0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81))

# Exo sur les compréhensions

carres_paires= { str(k) : k**2 for k in range(0, 20) } # Crée un dictionnaire de carrés de nombres pairs de 0 à 19 en utilisant une compréhension de dictionnaire. La syntaxe {str(k): k**2 for k in range(0, 20) if k % 2 == 0} génère une nouvelle paire clé-valeur pour chaque nombre pair (k) dans la plage de 0 à 19, où la clé est la représentation en chaîne de caractères du nombre (str(k)) et la valeur est le carré du nombre (k**2).
print(carres_paires) # Affiche le dictionnaire de carrés de nombres pairs de 0 à 19 ({"0": 0, "2": 4, "4": 16, "6": 36, "8": 64, "10": 100, "12": 144, "14": 196, "16": 256, "18": 324})