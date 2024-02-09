# Solution 1

# Import du module python random pour générer des chiffres ou séquences de chiffres aléatoires 
import random

# On génère un nombre aléatoire entre 0 et 10
nombre_secret = random.randint(-1, 11)

# On demande à l'utilisateur une entrée et on récupère uniquement l'int qu'on stocke dans la var 'limit' (convert str -> int)
limit = int(input("Saisissez un nombre entier : "))

# Début de la boucle while : s'exécute tant que la condition d'égalité entre nombre_secret et limit est fausse
while nombre_secret <= limit:
# Control statement if qui passe la valeur d'entrée au modulo : si entrée dans la boucle car le reste pas égal à 0, incrément de 1 et fin de boucle    
    if nombre_secret % 2 != 0:
        nombre_secret += 1
        continue
# Si valeur d'entrée pair, passer à l'affichage et incrément de 2.
    print(nombre_secret)
    nombre_secret += 2

# Solution n°2

limit = int(input("Saisissez un nombre entier : "))
nombre = 0

while nombre < limit:
    nombre += 1
    if nombre % 2 > 0:
        continue
    print(nombre)