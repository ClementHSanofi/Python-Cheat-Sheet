"""
    Boolean
"""
# Opérateurs logiques : AND
true_variable = True and True
false_variable = True and False

# Opérateurs logiques : OR
true_variable = False or True
false_variable = False or False

# Opérateur logique : NOT
true_variable = not False
false_variable = not True

"""
    Comparaisons
"""
# Comparaisons classiques
a = 10
b = 5

print(a > b)     # True
print(a < b)     # False
print(a == b)    # False
print(a != b)    # True
print(a >= b)    # True
print(a <= b)    # False

# Comparaison d'identité
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)        # True (même objet)
print(x is z)        # False (contenu identique, objets différents)
print(x == z)        # True (valeurs identiques)

# Comparaison entre types différents
print(17 == '17')            # False
print(17 == 17.0)            # True
print(6/3 == 0b10)           # True
print(17 == complex(17))     # True
print(0.4 == 2/5)            # True

# Comparaison avec NaN
nan = float('NaN')
print(nan == nan)            # False
print(nan < 3)               # False
print(3 < nan)               # False

# Comparaison de chaînes (lexicographique)
print('Python' > 'Rust')         # False
print('Python' > 'JavaScript')   # True
print('你好' < '再见')             # True
print(ord('你'), ord('再'))       # 20320, 20877

# Chaînage de comparaisons
x = 2
y = 5
z = 10

print(x < y < z)     # True
print(x < y > z)     # False
print(x > y < z)     # False

"""
    Test d'appartenance
"""

fruits = ["pomme", "banane", "orange"]
print("pomme" in fruits)         # True
print("kiwi" not in fruits)      # True

# Test d'appartenance dans un dictionnaire
employee = {
    "name": "John Doe",
    "id": 67826,
    "age": 33,
    "title": "CEO"
}

print("age" in employee)                # True
print(33 in employee)                   # False
print(33 in employee.values())          # True
print(("age", 33) in employee.items())  # True
print("lastname" not in employee)       # True

# Test d'appartenance dans une chaîne
name = "Super Batman"
print("Bat" in name)             # True
print("Batwoman" in name)        # False

