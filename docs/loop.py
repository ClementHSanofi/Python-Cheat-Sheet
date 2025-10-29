"""
    Les boucles en Python
"""
 
# Boucle while

# La boucle while s'exécute tant que l'expression est évaluée à True.
# Elle s'arrête dès que l'expression devient False.
placeholders = ["spam", "ham", "eggs", "green_spam", "green_ham", "green_eggs"]

while placeholders:
    print(placeholders.pop(0))
# Affiche chaque élément jusqu'à ce que la liste soit vide.


# Boucle for

# La boucle for parcourt les éléments d’un objet itérable.
word_list = ["bird", "chicken", "barrel", "bongo"]

for word in word_list:
    if word.startswith("b"):
        print(f"{word.title()} starts with a B.")
    else:
        print(f"{word.title()} doesn't start with a B.")

"""
    Séquence range()
"""

# range() génère une séquence de nombres sans créer une liste en mémoire.
# Syntaxe : range(start, stop, step)

for number in range(1, 7):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# Avec un pas personnalisé
for number in range(3, 15, 2):
    print(f"{number} is odd.")  # Tous les nombres ici sont impairs

"""
    Indexation avec enumerate()
"""

# enumerate() permet d'accéder à la fois à l'index et à la valeur
word_list = ["bird", "chicken", "barrel", "apple"]

for index, word in enumerate(word_list):
    if word.startswith("b"):
        print(f"{word.title()} (at index {index}) starts with a B.")
    else:
        print(f"{word.title()} (at index {index}) doesn't start with a B.")

# Exemple d'association entre deux listes
word_list = ["cat", "chicken", "barrel", "apple", "spinach"]
category_list = ["mammal", "bird", "thing", "fruit", "vegetable"]

for index, word in enumerate(word_list):
    print(f"{word.title()} is in category: {category_list[index]}.")

"""
    Personnalisation du comportement
"""

# continue : saute à l’itération suivante
word_list = ["bird", "chicken", "barrel", "bongo", "sliver", "apple", "bear"]

for index, word in enumerate(word_list):
    if index == 0:
        continue
    if word.startswith("b"):
        print(f"{word.title()} (at index {index}) starts with a b.")

# break : interrompt la boucle
word_list = ["bird", "chicken", "barrel", "bongo", "sliver", "apple"]

for index, word in enumerate(word_list):
    if word.startswith("b"):
        print(f"{word.title()} (at index {index}) starts with a B.")
    elif word == "sliver":
        break
    else:
        print(f"{word.title()} doesn't start with a B.")
print("loop broken.")



"""
    Boucles Pythonic
"""

# List comprehension : pour transformer ou filtrer des données
scores = [45, 72.00, 88.50, 39, 60]
threshold = 60
boolean_list = [score >= threshold for score in scores]  # [False, True, True, False, True]
binary_list = [int(score >= threshold) for score in scores]  # [0, 1, 1, 0, 1]
rounded_list = [round(score) for score in scores]  # [45, 72, 88, 39, 60]
valid_scores = [score for score in scores if score >= threshold]  # [72, 88, 60]

# Boucle avec zip() pour parcourir plusieurs listes
names = ["Alice", "Bob", "Charlie"]
grades = [85, 92, 78]

for name, grade in zip(names, grades):
    print(f"{name} a obtenu {grade} points.")

# Boucle avec next() retourne le premier élément trouvé 
student_info = [["Charles", 90], ["Tony", 80], ["Alex", 100]]
perfect_score = next((student for student in student_info if student[1] == 100), [])