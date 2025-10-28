"""
    Déclaration de chaines
"""
single_quoted = 'Permet d\'utiliser des "guillemets doubles" sans caractère d\'échappement.'
double_quoted = "Permet d'utiliser des 'guillemets simples' sans caractère d'échappement."
escapes = 'Si nécessaire, un \\ peut être utilisé comme caractère d\'échappement.'

# Chaines multi-lignes
triple_quoted = '''Chaîne sur plusieurs lignes.
Les sauts de ligne, tabulations et espaces sont pris en charge.

Souvent utilisée pour les docstrings ou les tests de documentation.
'''


"""
    Concaténation
"""
# Avec + (pas très performant)
language = "Ukrainien"
number = "neuf"
word = "дев'ять"

sentence = word + " signifie " + number + " en " + language + "." # "дев'ять signifie neuf en Ukrainien."

# Avec str.join() (Plus efficace)
# Array
chickens = ["poule", "œuf", "coq"]
' '.join(chickens)  # 'poule œuf coq'
' :: '.join(chickens)  # 'poule :: œuf :: coq'
' 🌿 '.join(chickens)  # 'poule 🌿 œuf 🌿 coq'

# Tuples
flowers = ("rose", "marguerite", "œillet")
'*-*'.join(flowers)  # 'rose*-*marguerite*-*œillet'

# Set
flowers_set = {"rose", "marguerite", "œillet"}
'*-*'.join(flowers_set)  # L’ordre n’est pas garanti

# Attention avec les chaines
phrase = "Ceci est ma chaîne"
'..'.join(phrase)  # C..e..c..i.. ..e..s..t.. ..m..a.. ..c..h..a..î..n..e

#Effet créatifs
under_words = ['under', 'current', 'sea', 'pin', 'dog', 'lay']
separator = ' ⤴️ under'
separator.join(under_words)
# 'under ⤴️ undercurrent ⤴️ undersea ⤴️ underpin ⤴️ underdog ⤴️ underlay'


"""
    Indexation
"""
creative = '창의적인'
creative[0]  # '창'
creative[2]  # '적'
creative[-1] # '인'

# Il n'existe pas de type 'caractère' en python: chaque élément indexé est une str de longueur 1
website = "exercism"
type(website[0])  # <class 'str'>
len(website[0])   # 1
website[0] == website[0:1] == 'e'  # True


"""
    Slicing
"""
# On peu extraire des sous-chaine avec la notation [start:stop:step]
# Tout les paramètre ne sont pas nécessaire
moon_and_stars = '🌟🌟🌙🌟🌟⭐'
moon_and_stars[1:4]  # '🌟🌙🌟'
moon_and_stars[:3]   # '🌟🌟🌙'
moon_and_stars[3:]   # '🌟🌟⭐'
moon_and_stars[:-1]  # '🌟🌟🌙🌟🌟'

sun_and_moon = '🌞🌙🌞🌙🌞🌙🌞🌙🌞'
sun_and_moon[::2]     # '🌞🌞🌞🌞🌞'
sun_and_moon[:-2:2]   # '🌞🌞🌞🌞'
sun_and_moon[1:-1:2]  # '🌙🌙🌙🌙'


"""
    Découpage split()
"""
cat_ipsum = "Détruire la maison en 5 secondes, se moquer de l'humain."
cat_ipsum.split()  # ['Détruire', 'la', 'maison', 'en', '5', 'secondes,', 'se', 'moquer', 'de', "l'humain."]
cat_ipsum.split()[-1]  # "l'humain.

# Avec un séparateur personnalisé
cat_words = "félin, quadrupède, féroce, poilu"
cat_words.split(', ')  # ['félin', 'quadrupède', 'féroce', 'poilu']

# Fonctionne sur du multi-caractères
colors = """rouge,
orange,
vert,
violet,
jaune"""

colors.split(',\n')  # ['rouge', 'orange', 'vert', 'violet', 'jaune']


"""
    Itération sur caractère
"""
exercise = 'bonjour'

for code_point in exercise:
    print(code_point)
# Affiche chaque caractère individuellement

for index, code_point in enumerate(exercise):
    print(index, ": ", code_point)
# Affiche l’index et le caractère

