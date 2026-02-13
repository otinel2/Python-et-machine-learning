# Importer un module qui est un fichier de notre projet
## import projet_1 as p1 ( Importe le module projet_1 et lui donne l'alias p1 pour faciliter son utilisation dans le code. Cela permet d'accéder aux fonctions, classes ou variables définies dans projet_1 en utilisant l'alias p1 (par exemple, p1.ma_fonction()).)
#liste = p1.ma_fonction() # Appelle la fonction ma_fonction du module projet_1 (ou p1) et stocke le résultat dans la variable liste. Après l'importation du module avec l'alias p1, vous pouvez accéder à ma_fonction() en utilisant p1.ma_fonction().
# importer une fonction spécifique d'un module
## from projet_1 import ma_fonction ( Importe uniquement la fonction ma_fonction du module projet_1, ce qui permet de l'utiliser directement dans le code sans avoir besoin de préfixer son nom avec le nom du module. Après cette importation, vous pouvez appeler ma_fonction() directement dans votre code.)
#liste= ma_fonction() # Appelle la fonction ma_fonction qui a été importée directement du module projet_1 et stocke le résultat dans la variable liste. Après l'importation de ma_fonction() avec from projet_1 import ma_fonction, vous pouvez l'appeler directement sans préfixer son nom avec le nom du module.

# importer toutes les fonctions d'un module
## from projet_1 import * ( Importe toutes les fonctions, classes et variables définies dans le module projet_1, ce qui permet de les utiliser directement dans le code sans avoir besoin de préfixer leur nom avec le nom du module. Cependant, cette méthode d'importation est généralement déconseillée car elle peut entraîner des conflits de noms si plusieurs modules contiennent des éléments avec les mêmes noms.)
#liste = ma_fonction() # Appelle la fonction ma_fonction qui a été importée directement du module projet_1 en utilisant from projet_1 import *, et stocke le résultat dans la variable liste. Après l'importation de toutes les fonctions avec from projet_1 import *, vous pouvez appeler ma_fonction() directement dans votre code, mais il est important de noter que cette méthode peut entraîner des conflits de noms si plusieurs modules contiennent des éléments avec les mêmes noms.

# les modules important pour faire du machine learning et de la data science
## module Math
import math # Importe le module math, qui fournit des fonctions mathématiques de base telles que les fonctions trigonométriques, les fonctions logarithmiques, les fonctions de puissance, etc. Après l'importation du module math, vous pouvez utiliser ses fonctions en préfixant leur nom avec math (par exemple, math.sqrt() pour calculer la racine carrée).
print(math.cos(2*math.pi)) # Affiche le résultat de la fonction cosinus appliquée à 2 fois pi, ce qui est égal à 1. La fonction math.cos() calcule le cosinus d'un angle donné en radians, et math.pi représente la valeur de pi (environ 3.14159). Donc, math.cos(2*math.pi) calcule le cosinus de 360 degrés (ou 2 pi radians), qui est égal à 1.

## module statistics
import statistics # Importe le module statistics, qui fournit des fonctions pour calculer des statistiques descript
list_0 = [1, 2, 3, 4, 5] # Crée une liste de nombres de 1 à 5 et l'assigne à la variable list_0.
print(statistics.mean(list_0)) # Affiche la moyenne de la liste list_0

## module random
import random # Importe le module random, qui fournit des fonctions pour générer des nombres al
print(random.choice(list_0)) # Affiche un élément aléatoire de la liste list_0 en utilisant la fonction random.choice(). Cette fonction sélectionne un élément au hasard parmi les éléments de la liste fournie en argument (dans ce cas, list_0) et le retourne. Chaque fois que vous exécutez cette ligne, vous obtiendrez potentiellement un résultat différent, car l'élément choisi est aléatoire.

# module os
## getcwd retourne le chemin du répertoire de travail actuel
import os # Importe le module os, qui fournit des fonctions pour interagir avec le système
print(os.getcwd()) # Affiche le chemin du répertoire de travail actuel en utilisant la fonction os.getcwd(). Cette fonction retourne une chaîne de caractères représentant le chemin absolu du répertoire dans lequel le script Python est actuellement exécuté. Cela peut être utile pour vérifier où se trouve votre script ou pour construire des chemins de fichiers relatifs à ce répertoire.

# module glob
## glob retourne une liste de chemins de fichiers correspondant à un motif spécifié
import glob # Importe le module glob, qui fournit des fonctions pour trouver des chemins de fichiers
print(glob.glob("*.txt")) # Affiche une liste de chemins de fichiers correspondant au motif "*.txt" en utilisant la fonction glob.glob(). Cette fonction recherche dans le répertoire de travail actuel tous les fichiers qui ont une extension .txt et retourne une liste de leurs chemins. Par exemple, si vous avez des fichiers nommés "fichier1.txt", "fichier2.txt" et "document.txt" dans le répertoire, glob.glob("*.txt") retournera ["fichier1.txt", "fichier2.txt", "document.txt"].

## exemeple d'utilisation de glob pour trouver tous les fichiers Python dans un répertoire

filenames = glob.glob("*.txt")
for file in filenames:
    with open(file, "r") as f: 
        print(f.read()) # Affiche le contenu de chaque fichier .txt trouvé dans le répertoire de travail actuel. La fonction glob.glob("*.txt") retourne une liste de chemins de fichiers correspondant au motif "*.txt", et la boucle for itère sur cette liste. Pour chaque fichier trouvé, le code ouvre le fichier en mode lecture ("r") à l'aide d'une instruction with (qui garantit que le fichier est correctement fermé après son utilisation), lit son contenu avec f.read() et l'affiche à l'écran.