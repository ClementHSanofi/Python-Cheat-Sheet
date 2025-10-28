
"""
Ce fichier __init__.py marque le dossier 'docs' comme un package Python.

Il permet :
- D'organiser les modules Python dans un espace de noms commun.
- De définir les éléments accessibles lors d'un import global (`from docs import *`).
- De centraliser les importations utiles à l'extérieur du package.

En exposant certaines fonctions et constantes via __all__, ce fichier facilite
l'importation contrôlée et propre des composants principaux du package.
"""

from .base01 import MA_CONSTANTE
from .base01 import addition
from .base01 import puissance

__all__ = ["MA_CONSTANTE", "addition", puissance]