"""
    Tuples
"""

# Un tuple est une collection immuable d'élément ordonnés

# Construction d'un tuple (Doit être dans une liste ou une autre tuple)
# Avec tuple()
no_element = tuple() # ()
one_element = tuple([16]) # (16,)
multiple_elements_string = tuple("Timbuktu") # ('T', 'i', 'm', 'b', 'u', 'k', 't', 'u')
multiple_elements_list = tuple(["Parrot", "Bird", 334782]) # ('Parrot', 'Bird', 334782)
multiple_elements_set = tuple({2, 3, 5, 7, 11}) # (2, 3, 5, 7, 11)

# Déclaration littérale
no_elements = ()
one_element = ("Guava",) # La virgule est obligatoire pour un seul élément
# Tupless imbriqués
nested_data_structures = (
    {"fish": "gold", "monkey": "brown", "parrot": "grey"},
    ("fish", "mammal", "bird")
) # ({'fish': 'gold', 'monkey': 'brown', 'parrot': 'grey'}, ('fish', 'mammal', 'bird'))
nested_data_structures_1 = (
    ["fish", "gold", "monkey", "brown", "parrot", "grey"],
    ("fish", "mammal", "bird")
) # (['fish', 'gold', 'monkey', 'brown', 'parrot', 'grey'], ('fish', 'mammal', 'bird'))


"""
    Concaténation et répétition
"""
# Concaténation avec +
new_via_concatenate = ("George", 5) + ("cat", "Tabby") # ("George", 5, "cat", "Tabby")

# Répétition avec *
first_group = ("cat", "dog", "elephant")
multiplied_group = first_group * 3 # ('cat', 'dog', 'elephant', 'cat', 'dog', 'elephant', 'cat', 'dog', 'elephant')


"""
    Accès aux éléments
"""
student_info = ("Alyssa", "grade 3", "female", 8)

student_gender = student_info[2]     # 'female'
student_gender = student_info[-2]    # 'female'
student_name = student_info[0]       # 'Alyssa'
student_name = student_info[-4]      # 'Alyssa'

"""
    Itération sur les éléments
"""

# Simple boucle for
for item in student_info:
    print(item)

# Avec récupération d'index + valeur
for index, item in enumerate(student_info):
    print(f"Index is: {index}, value is0: {item}.")

"""
    Vérification d'appartenance
"""
multiple_elements_list = tuple(["Parrot", "Bird", 334782])
"Parrot" in multiple_elements_list  #True