# definir une fonction
f = lambda x: x * 2  # la fonction avec une expression lambda permet de créer des fonctions mathématiques simples en une seule ligne. Ici, la fonction prend un argument x et retourne le double de x.
# utiliser la fonction
print(f(5)) # Affiche 10


# fonction et arguments
def e_potentielle(masse, hauteur, g=9.81): # la fonction e_potentielle calcule l'énergie potentielle d'un objet en fonction de sa masse, de sa hauteur et de l'accélération due à la gravité. La fonction prend trois arguments : masse, hauteur et g (avec une valeur par défaut de 9.81 m/s²).
    E = masse * hauteur * g
    return (E, "Joules") # la fonction retourne une valeur et une unité de mesure. La fonction calcule l'énergie potentielle en utilisant la formule E = m * h * g, où m est la masse, h est la hauteur et g est l'accélération due à la gravité.
# utiliser la fonction
e_potentielle(masse=10, hauteur=5) # Affiche 490.5
print(e_potentielle(masse=10,hauteur= 5)) # Affiche 490.5

