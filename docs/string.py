"""
    Déclaration de chaines
"""

# Chaines simples
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
# Avec + 
language = "Ukrainien"
number = "neuf"
word = "дев'ять"
sentence = word + " signifie " + number + " en " + language + "." # "дев'ять signifie neuf en Ukrainien."

# Avec .join() (Plus efficace)
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
separator.join(under_words) # 'under ⤴️ undercurrent ⤴️ undersea ⤴️ underpin ⤴️ underdog ⤴️ underlay'


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


"""
    Méthode endswith() / startswith()
"""
# Vérifie si une chaine fini par la chaine choisise
chaine = "bonjour"
chaine.endswith("r")                #True
chaine.endswith("t")                #False
print(chaine.endswith(("r", "t")))  # True → car "r" est dans la liste
"programmation".endswith("tion")    # True

# Vérifie si une chaîne commence par la chaîne choisie
chaine = "bonjour"
chaine.startswith("b")                # True
chaine.startswith("j")                # False
print(chaine.startswith(("b", "j")))  # True → car "b" est dans la liste
"programmation".startswith("pro")     # True


"""
    Méthode replace()
"""
texte = "Le ciel est bleu, le ciel est vaste."
nouveau_texte = texte.replace("ciel", "soleil") # "Le soleil est bleu, le soleil est vaste."

# Remplacement partiel (limité à 1 occurrence)
texte = "chat, chat, chat"
remplacement_limite = texte.replace("chat", "chien", 1) # "chien, chat, chat"


"""
    Méthode rstrip() / lstrip() / strip
"""
# rstrip nettoie la fin d'une chaine
# Suppression des espaces à droite
texte = "Bonjour     "
texte_nettoye = texte.rstrip()  # "Bonjour"

# Suppression d'un caractère spécifique à droite
texte = "Bonjour!!!"
texte_nettoye = texte.rstrip("!")  # "Bonjour"

# Suppression partielle (ne supprime que les caractères à droite)
texte = "!!!Bonjour!!!"
texte_nettoye = texte.rstrip("!")  # "!!!Bonjour"

# lstrip nettoie la fin d'une chaine
# Suppression des espaces à gauche
texte = "     Bonjour"
texte_nettoye = texte.lstrip()  # "Bonjour"

# Suppression d'un caractère spécifique à gauche
texte = "!!!Bonjour"
texte_nettoye = texte.lstrip("!")  # "Bonjour"

# Suppression partielle (ne supprime que les caractères à gauche)
texte = "!!!Bonjour!!!"
texte_nettoye = texte.lstrip("!")  # "Bonjour!!!"

texte = "   Bonjour   "
texte_nettoye = texte.strip()  # "Bonjour"

# Supprime les lettres 'd', 'n', 'u', 'e' et les espaces au début et à la fin
texte= "    unaddressed    "
texte_nettoye.strip('dnue ') # 'address'


"""
    Méthode .title()
"""
# Met en capital les premiers charactère de chaque mots 
man_in_hat = 'the man in the hat.'
man_in_hat.title() #The Man In The Hat.