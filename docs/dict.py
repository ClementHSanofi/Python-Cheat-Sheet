"""
    Les dictionnaires
"""

# Un dictionnaire est une structure de données qui associe des clés (hashables et uniques) à des valeurs.
# - Les clés peuvent être : str, int, float, ou tuple (immuable).
# - Les clés ne peuvent pas être des types mutables (list, dict, set).

# Constuction d'un dictionnaire

# Avec le constucteur dict()
wombat = dict([('name', 'Wombat'), ('speed', 23), ('land_animal', True)])
bear = dict(name="Black Bear", speed=40, land_animal=True)

# Avec une déclaration littérale
whale = {
    "name": "Blue Whale",
    "speed": 35,
    "land_animal": False
}

"""
    Accès au valeurs
"""

# Accès direct avec []
bear["speed"] # 40
bear["color"] # KeyError si la clé n'existe pas

# Accès sécurisé avec .get()
bear.get("speed") # 40
bear.get("color", "not found") # Affiche 'not found' si la clé est absente

"""
    Modification ou ajout de valeur
"""

# Modification d'une valeur existante
bear["name"] = "Grizzly Bear"
whale["speed"] = 25

# Ajout une nouvelle paire clé/valeur
bear["color"] = "tawney"
whale["blowholes"] = 1

"""
    Suppression avec .pop()
"""
bear.pop("name")  # Supprime et retourne la valeur associée à "name"
bear.pop("name")  # KeyError si la clé n'existe plus
bear.pop("name", "Unknown")  # Retourne "Unknown" si la clé est absente


"""
    Boucle sur un dictionnaire
"""
# Parcours des clés
for key in bear:
    print((key, bear[key]))  # Affiche (clé, valeur)

# Parcours des paires clé/valeurs avec .items()
for key, value in whale.items():
    print(f"{key} : {value}")

# Accès uniquement aux clés ou aux valeurs
whale.keys()    # retourne toutes les clés
whale.values()  # retourne toutes les valeurs

inventory = {'wood': 3, 'stone': 2, 'gold': 1}

# Conversion (Liste de tuple ici)
new_inventory = [(key, value) for key, value in inventory.items() if value > 0]

"""
    collection.Counter
"""
# Counter est une classe du module collections qui permet de compter les occurrences de chaque élément dans une séquence (liste, chaîne, etc.).
from collections import Counter

def create_inventory(items):
    return dict(Counter(items))

create_inventory(["wood", "stone", "wood", "gold", "stone", "wood"]) # {'wood': 3, 'stone': 2, 'gold': 1}

# Accéder aux éléments les plus fréquents
Counter("abracadabra").most_common(2) # [('a', 5), ('b', 2)]

# Ajouter ou soustraire des compteurs
c1 = Counter("abc")
c2 = Counter("bcd")

c1 + c2  # Counter({'b': 2, 'c': 2, 'a': 1, 'd': 1})
c1 - c2  # Counter({'a': 1})
