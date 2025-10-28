"""
    Condition 
"""
x = 10

if x > 5:
    print("x est supérieur à 5")
elif x == 5:
    print("x est égal à 5")
else:
    print("x est inférieur à 5")

"""
    Bonnes pratiques Pythonic
"""

# Expression ternaire (condition courte en une ligne)
age = 20
status = "majeur" if age >= 18 else "mineur"
print("Statut :", status)

# Comparaison explicite (à éviter)
is_active = True
if is_active == True:
    print("Pas pythonic")

# Comparaison implicite (plus pythonic)
if is_active:
    print("Pythonic")

# Tester l'appartenance avec `in`
fruit = "pomme"
salade = ["pomme", "banane", "orange"]

if fruit in salade:
    print("Fruit présent")

# Walrus operator
# Permet d'affecter une valeur tout en la testant
if (longueur := len(salade)) > 2:
    print(f"La salade contient {longueur} fruits.")

# Fonction utilitaire
def is_supperior_at_five(number: int) -> bool:
    return number > 5
print(is_supperior_at_five(3))  # False
print(is_supperior_at_five(6))  # True 