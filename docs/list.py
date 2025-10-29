
"""
    Les listes
"""

# Une liste est une collection ordonnée et modifiable d'éléments.
# Elle peut contenir différents types de données, y compris d'autres listes.

# Déclaration avec des crochets []
vide = []
un_element = ["Guava"]
plusieurs_elements = ["Parrot", "Bird", 334782]

# Mise en forme sur plusieurs lignes
fleurs = [
    "Rose",
    "Sunflower",
    "Poppy",
    "Pansy",
    "Tulip",
    "Fuchsia",
    "Cyclamen",
    "Lavender"
]

# Structures imbriquées
donnees_complexes = [
    {"fish": "gold", "monkey": "brown", "parrot": "grey"},
    ("fish", "mammal", "bird"),
    ['water', 'jungle', 'sky']
]

# Utilisation du constructeur list()
vide = list() # []
depuis_tuple = list(("Parrot", "Bird", 334782)) # ['Parrot', 'Bird', 334782]
depuis_set = list({2, 3, 5, 7, 11}) # [2, 3, 5, 7, 11]
depuis_chaine = list("Timbuktu") # ['T', 'i', 'm', 'b', 'u', 'k', 't', 'u']
donnees = {"fish": "gold", "monkey": "brown"}
cles = list(donnees)# ['fish', 'monkey'] (seules les clés sont prises)

# Attention : les objets non itérables provoquent une erreur
# list(16)  # TypeError: 'int' object is not iterable

"""
    Accès aux éléments par index
"""
aliments = ["Oatmeal", "Fruit Salad", "Eggs", "Toast"]
print(aliments[0])   # 'Oatmeal'
print(aliments[-1])  # 'Toast'
print(aliments[2])   # 'Eggs'

# Slicing
couleurs = ["Red", "Purple", "Green", "Yellow", "Orange", "Pink", "Blue", "Grey"]
print(couleurs[2:6])     # ['Green', 'Yellow', 'Orange', 'Pink']
print(couleurs[::3])     # ['Red', 'Yellow', 'Blue']

# Utilisation de slice()
s = slice(1, 4)
print(couleurs[s])       # ['Purple', 'Green', 'Yellow']

"""
    Combinaison et duplication
"""
concatenee = ["George", 5] + ["cat", "Tabby"] # ['George', 5, 'cat', 'Tabby']

replication = ["cat", "dog", "elephant"] * 3 # ['cat', 'dog', 'elephant', 'cat', 'dog', 'elephant', 'cat', 'dog', 'elephant']

"""
    Boucle
"""
couleurs = ["Orange", "Green", "Grey", "Blue"]
for item in couleurs:
    print(item) # Orange Green Grey Blue

# Boucle avec index
for index, item in enumerate(couleurs):
    print(f"{index} → {item}") # 0 → Orange 1 → Green 2 → Grey 3 → Blue

# List comprehension
carres = [x**2 for x in range(5)]
print(carres)  # [0, 1, 4, 9, 16]


"""
    Fonctions utiles
"""
nombres = [1, 2, 3, 4]
print(sum(nombres))       # 10
print(len(nombres))       # 4
print(min(nombres))       # 1
print(max(nombres))       # 4
print(any([False, True])) # True
print(all([True, True]))  # True


"""
    Méthode de modification
"""
# Ajout
animaux = ["chat", "chien"]
animaux.append("lapin")           # ['chat', 'chien', 'lapin']
animaux.extend(["lion", "tigre"]) # ['chat', 'chien', 'lapin', 'lion', 'tigre']
animaux.insert(0, "souris")       # ['souris', 'chat', 'chien', 'lapin', 'lion', 'tigre'] (2 args place le deuxième à l'emplacement défini par le premier)

# Suppression
dernier = animaux.pop()           # ['souris', 'chat', 'chien', 'lapin', 'lion'] et stocke 'tigre' dans dernier
animal_retire = animaux.pop(1)    # ['souris', 'chien', 'lapin', 'lion'] et stocke 'chat' dans dernier
del animaux[0]                    # ['chien', 'lapin', 'lion']
animaux.remove("chien")           # ['lapin', 'lion'] (Supprime le premier élément si sa valeur est égale à celle de selectionnée avec remove())
animaux.clear()                   # []


"""
    Méthodes de tri et d'ordre
"""
animaux = ["chat", "chien", "lion", "tigre"]
animaux.reverse()             # ['tigre', 'lion', 'chien', 'chat'] Inverse l'ordre
animaux.sort()                # ['chat', 'chien', 'lion', 'tigre'] Alphabétique croissant
animaux.sort(reverse=True)    # ['tigre', 'lion', 'chien', 'chat'] Alphabétique décroissant
animaux.sort(key=len)         # ['chat', 'lion', 'chien', 'tigre'] Longueur de chaine
copie_triee = sorted(animaux) # ['chat', 'chien', 'lion', 'tigre'] Copie Alphabétique croissant


"""
    Méthode d'information
"""
items = [1, 7, 4, 1, 0, 2, 5, 1]
print(items.index(4))          # 0
items.count(1)                 # 3 Nombre de fois que l'on trouve l'élément dans la liste

names = ["Tina", "Leo", "Thomas", "Tina", "Emily", "Justin"]
print(names.index("Tina"))        # 0
print(names.index("Tina", 2, 5))  # 3 Cherche de l'indice 2 à 5

"""
    Copie de liste
"""
original = [1, 2, 3]
copie = original.copy() # Crée une copie de la liste originale
