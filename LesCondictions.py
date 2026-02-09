# Condictions if
X = 10
if X > 5: # La condition if vérifie si la variable X est supérieure à 5. Si la condition est vraie, le code à l'intérieur du bloc if sera exécuté.
    print("X est supérieur à 5") # Affiche "X est supérieur à 5" si la condition est vraie.

# Condictions if-else
y = 3
if y > 5: # La condition if vérifie si la variable Y est supérieure à 5. Si la condition est vraie, le code à l'intérieur du bloc if sera exécuté. Sinon, le code à l'intérieur du bloc else sera exécuté.
    print("Y est supérieur à 5") # Affiche "Y est supérieur à 5" si la condition est vraie.
else:
    print("Y est inférieur ou égal à 5") # Affiche "Y est inférieur ou égal à 5" si la condition est fausse.

# Condictions if-elif-else
z = 7
if z > 10: # La condition if vérifie si la variable Z est supérieure à 10. Si la condition est vraie, le code à l'intérieur du bloc if sera exécuté. Sinon, la condition elif sera vérifiée.
    print("Z est supérieur à 10") # Affiche "Z est supérieur à 10" si la condition est vraie.
elif z > 5: # La condition elif vérifie si la variable Z est supérieure à 5. Si la condition est vraie, le code à l'intérieur du bloc elif sera exécuté. Sinon, le code à l'intérieur du bloc else sera exécuté.
    print("Z est supérieur à 5 mais inférieur ou égal à 10") # Affiche "Z est supérieur à 5 mais inférieur ou égal à 10" si la condition est vraie.
else:
    print("Z est inférieur ou égal à 5") # Affiche "Z est inférieur ou égal à 5" si la condition est fausse.

# fonction et condition
def signe (x) :
    if x > 0:
        print(x, 'positif') # Affiche "x positif" si la condition est vraie.
    elif x == 0:
        print(x, 'nul') # Affiche "x nul" si la condition est vraie.
    else:
        print(x, 'negatif') # Affiche "x negatif" si la condition est fausse.

signe(5) # Affiche "5 positif"
signe(0) # Affiche "0 nul"
signe(-3) # Affiche "-3 negatif"


# boucle for

for i in range(10) :
    print(i) # Affiche les nombres de 0 à 9, un par ligne. La fonction range(10) génère une séquence de nombres de 0 à 9, et la boucle for itère sur cette séquence, assignant chaque nombre à la variable i et exécutant le bloc de code à l'intérieur de la boucle pour chaque valeur de i.

# boucle for argument debut et pas

for element in range(1, 10, 2) :
    print(element) # Affiche les nombres impairs de 1 à 9, un par ligne. La fonction range(1, 10, 2) génère une séquence de nombres commençant à 1, s'arrêtant avant 10, et incrémentant de 2 à chaque étape. Ainsi, la boucle for itère sur cette séquence, assignant chaque nombre impair à la variable i et exécutant le bloc de code à l'intérieur de la boucle pour chaque valeur de i.

# boucle while
j = 0
while j < 5: # La condition while vérifie si la variable j est inférieure à 5. Tant que la condition est vraie, le code à l'intérieur du bloc while sera exécuté.
    print(j) # Affiche les nombres de 0 à 4, un par ligne. La variable j est incrémentée de 1 à chaque itération de la boucle, ce qui permet d'afficher les nombres de 0 à 4.
    j += 1


# exo sur les conditions
def fibonacci(n):
    X, Y = 0, 1
    for i in range(n):
        print(X)  # Affiche le nombre actuel de la séquence de Fibonacci
        X, Y = Y, X + Y  # Calcule le prochain nombre et décale les valeurs pour la prochaine itération
fibonacci(10)  # Affiche les 10 premiers nombres de la séquence de Fibonacci

 