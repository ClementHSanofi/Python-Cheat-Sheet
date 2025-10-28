
"""
    Les listes
"""

# Une liste est une collection ordonnée et modifiable d'éléments.
# Elle peut contenir différents types de données, y compris d'autres listes.

# Déclaration avec des crochets []
vide = []
print(vide)  # []

un_element = ["Guava"]
print(un_element)  # ['Guava']

plusieurs_elements = ["Parrot", "Bird", 334782]
print(plusieurs_elements)  # ['Parrot', 'Bird', 334782]

# Mise en forme sur plusieurs lignes pour plus de lisibilité
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
print(fleurs) # ['Rose', 'Sunflower', 'Poppy', 'Pansy', 'Tulip', 'Fuchsia', 'Cyclamen', 'Lavender']

"""
    Structures imbriquées
"""
donnees_complexes = [
    {"fish": "gold", "monkey": "brown", "parrot": "grey"},
    ("fish", "mammal", "bird"),
    ['water', 'jungle', 'sky']
]
print(donnees_complexes) # [{'fish': 'gold', 'monkey': 'brown', 'parrot': 'grey'}, ('fish', 'mammal', 'bird'), ['water', 'jungle', 'sky']]

"""
    Utilisation du constructeur list()
"""
vide = list()
print(vide)  # []

# À partir d'un tuple
depuis_tuple = list(("Parrot", "Bird", 334782))
print(depuis_tuple) # ['Parrot', 'Bird', 334782]

# À partir d'un set
depuis_set = list({2, 3, 5, 7, 11})
print(depuis_set) # [2, 3, 5, 7, 11]

# À partir d'une chaîne
depuis_chaine = list("Timbuktu")
print(depuis_chaine)  # ['T', 'i', 'm', 'b', 'u', 'k', 't', 'u']

# À partir d'un dictionnaire (seules les clés sont prises)
donnees = {"fish": "gold", "monkey": "brown"}
cles = list(donnees)
print(cles)  # ['fish', 'monkey']

# Attention : les objets non itérables provoquent une erreur
# list(16)  # TypeError: 'int' object is not iterable

"""
    Accès aux éléments par index
"""
aliments = ["Oatmeal", "Fruit Salad", "Eggs", "Toast"]
print(aliments[0])   # 'Oatmeal'
print(aliments[-1])  # 'Toast'
print(aliments[2])   # 'Eggs'

"""
    Slicing (tranches)
"""
couleurs = ["Red", "Purple", "Green", "Yellow", "Orange", "Pink", "Blue", "Grey"]
print(couleurs[2:6])     # ['Green', 'Yellow', 'Orange', 'Pink']
print(couleurs[::3])     # ['Red', 'Yellow', 'Blue']


"""
    Combinaison de listes
"""
concatenee = ["George", 5] + ["cat", "Tabby"]
print(concatenee)        # ['George', 5, 'cat', 'Tabby']

replication = ["cat", "dog", "elephant"] * 3
print(replication)       # ['cat', 'dog', 'elephant', 'cat', 'dog', 'elephant', 'cat', 'dog', 'elephant']

"""
    Boucle sur une liste
"""
couleurs = ["Orange", "Green", "Grey", "Blue"]
for item in couleurs:
    print(item) # Orange Green Grey Blue

# Boucle avec index
for index, item in enumerate(couleurs):
    print(f"{index} → {item}") # 0 → Orange 1 → Green 2 → Grey 3 → Blue


"""
    Méthode sum() 
"""
# Additionne les nombres d'une liste entre eux
nombres = [1, 2, 3, 4]
print(sum(nombres)) # 10

"""
    Méthode len()
"""
# Donne le nombre d'item de la liste
print(len(nombres)) # 4

"""
    Méthode append()
"""
# Ajoute un élément à la fin de la liste
animaux = ["chat", "chien"]
animaux.append("lapin")
print(animaux)  # ['chat', 'chien', 'lapin']

"""
    Méthode extend()
"""
# Ajoute plusieurs éléments à la fin de la liste
animaux.extend(["lion", "tigre"])
print(animaux)  # ['chat', 'chien', 'lapin', 'lion', 'tigre']

"""
    Méthode pop()
"""
# Supprime et retourne le dernier élément
dernier = animaux.pop()
print(dernier)   # 'tigre'
print(animaux)   # ['chat', 'chien', 'lapin', 'lion']

# Supprime un élément à un index précis
animal_retire = animaux.pop(1)
print(animal_retire)  # 'chien'
print(animaux)        # ['chat', 'lapin', 'lion']

"""
    Méthode reverse()
"""
# Inverse l'ordre des éléments dans la liste
animaux.reverse()
print(animaux)  # ['lion', 'lapin', 'chat']

"""
    Méthode sort()
"""
# Trie les éléments par ordre croissant (alphabétique ici)
animaux.sort()
print(animaux)  # ['chat', 'lapin', 'lion']

# Trie en ordre décroissant
animaux.sort(reverse=True)
print(animaux)  # ['lion', 'lapin', 'chat']