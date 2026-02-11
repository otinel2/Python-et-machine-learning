# # fonction abs qui affiche la valeur absolue d'un nombre
# x = 3
# print(abs(x)) # Affiche la valeur absolue de x (3)

# # fonction round qui arrondit un nombre à un nombre de décimales spécifié
# y = 3.14159
# print(round(y, 2)) # Affiche y arrondi à 2 décimales (3.14)

# liste = [1, 2, 3, 4, 5]
# # fonction max qui retourne le plus grand élément d'une séquence ou de plusieurs arguments
# print(max(liste)) # Affiche le plus grand élément de la liste (5)
# # fonction min qui retourne le plus petit élément d'une séquence ou de plusieurs arguments
# print(min(liste)) # Affiche le plus petit élément de la liste (1)
# # fonction len qui retourne le nombre d'éléments dans une séquence ou un objet
# print(len(liste)) # Affiche le nombre d'éléments dans la liste (5)
# # fonction sum qui retourne la somme de tous les éléments d'une séquence ou de plusieurs arguments
# print(sum(liste)) # Affiche la somme de tous les éléments de la liste (15)

# liste_2 = [True, False, True, True]
# # fonction all qui retourne True si tous les éléments d'une séquence sont vrais, sinon elle retourne False
# print(all(liste_2)) # Affiche False car il y a un élément False dans la liste_2
# # fonction any qui retourne True si au moins un élément d'une séquence est vrai, sinon elle retourne False
# print(any(liste_2)) # Affiche True car il y a au moins un élément True dans la liste_2



# # foction type qui retourne le type d'un objet
# x = 5 
# print(type(x)) # Affiche le type de x (<class 'int'>)

# # fonction str qui convertit un objet en une chaîne de caractères
# y = 3.14
# print(str(y)) # Affiche la représentation en chaîne de caractères de y ("3.14")


# # fonction input qui lit une ligne de texte à partir de l'entrée standard (généralement le clavier) et retourne une chaîne de caractères

# x = int(input("Entrez un nombre: ")) # Affiche le message "Entrez un nombre: " et attend que l'utilisateur saisisse une entrée. La fonction input() lit la ligne de texte saisie par l'utilisateur et la retourne sous forme de chaîne de caractères, qui est ensuite convertie en entier avec int() et assignée à la variable x.
# print(x) # Affiche la valeur de x, qui est maintenant un entier

# # fonction format
# x = 25
# ville = "Paris"
# message = "la température à {} est de {} degrés".format(ville, x) # Crée une chaîne de caractères formatée en utilisant la méthode format(). La syntaxe "la température à {} est de {} degrés".format(ville, x) remplace les accolades {} par les valeurs des variables ville et x respectivement, pour créer un message complet.
# print(message) # Affiche le message formaté ("la température à Paris est de 25

# ## format bien ecrit 
# x = 25
# ville = "Paris"
# message = f"la température à {ville} est de {x} degrés" # Crée une chaîne de caractères formatée en utilisant une f-string. La syntaxe f"la température à {ville} est de {x} degrés" permet d'insérer directement les valeurs des variables ville et x dans la chaîne de caractères en utilisant des accolades {}.
# print(message) # Affiche le message formaté ("la température à Paris est de 25 degrés")

# # fonction Open, read et write pour manipuler les fichiers
# ## ouvrir un fichier en mode écriture et écrire du texte dedans 
# f = open("exemple.txt", "w") # Ouvre un fichier nommé "exemple.txt" en mode écriture ("w"). Si le fichier n'existe pas, il sera créé. Si le fichier existe déjà, son contenu sera écrasé.
# f.write("Ceci est un exemple de texte écrit dans le fichier.") # Écrit la chaîne de caractères "Ceci est un exemple de texte écrit dans le fichier." dans le fichier ouvert.
# f.close() # Ferme le fichier après l'écriture pour s'assurer que les données sont correctement enregistrées et que les ressources sont libérées.
# ## ouvrir un fichier en mode lecture et lire son contenu
# f = open("exemple.txt", "r") # Ouvre le fichier "exemple.txt" en mode lecture ("r"). Le fichier doit exister pour que cette opération réussisse.
# contenu = f.read() # Lit le contenu du fichier et le stocke dans la variable contenu.
# f.close() # Ferme le fichier après la lecture pour libérer les ressources.
# print(contenu) # Affiche le contenu du fichier, qui est "Ceci est un exemple de texte écrit dans le fichier."

# # Ecrire plus simplement avec with open
# with open("exemple.txt", "w") as f: # Ouvre le fichier "exemple.txt" en mode
#     f.write("Ceci est un exemple de texte écrit dans le fichier.") # Écrit la chaîne de caractères "Ceci est un exemple de texte écrit dans le fichier." dans le fichier ouvert. Le bloc with garantit que le fichier sera automatiquement fermé après l'exécution du bloc, même en cas d'erreur.
# with open("exemple.txt", "r") as f: # Ouvre le fichier "    exemple.txt" en mode lecture ("r"). Le fichier doit exister pour que cette opération réussisse. Le bloc with garantit que le fichier sera automatiquement fermé après l'exécution du bloc, même en cas d'erreur.
#     contenu = f.read() # Lit le contenu du fichier et le stocke dans la variable contenu.  

# print(contenu) # Affiche le contenu du fichier, qui est "Ceci est un exemple de texte écrit dans le fichier."

# pratique 
with open('fichier.txt', 'w') as f:
    for i in range(10):
        f.write("{}^2 = {}\n".format(i, i**2)) # Écrit une ligne dans le fichier pour chaque nombre de 0 à 9, où la ligne contient le nombre suivi de son carré (par exemple, "0^2 = 0", "1^2 = 1", etc.). La syntaxe "{}^2 = {}\n".format(i, i**2) formate la chaîne de caractères en remplaçant les accolades {} par les valeurs de i et i**2 respectivement, et ajoute un saut de ligne à la fin de chaque ligne écrite dans le fichier.


# exo ecrit une fonction qui lit le fichier "fichier.txt" et affiche les lignes qui contiennent dans une liste
with open('fichier.txt', 'r') as f:
    liste = []
    for ligne in f:
        liste.append(ligne.strip()) # Ajoute chaque ligne du fichier à la liste après avoir supprimé les espaces blancs en début et en fin de ligne avec strip().
print(liste) # Affiche la liste des lignes lues à partir du fichier "fichier.txt", où chaque élément de la liste est une ligne du fichier sans les espaces blancs (par exemple, ["0^2 = 0", "1^2 = 1", ..., "9^2 = 81"]).