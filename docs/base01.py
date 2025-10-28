# Import pour utiliser les méthode "math"
import math

# Variables immutables / mutables
MA_CONSTANTE = "Je ne peux pas changer"
ma_variable = "Je peux changer"

# Fonctions & utilisation de méthodes
def addition(a: int, b: int) -> int :
    """Additionne deux nombres.

    Args:
        a (int): Premier nombre.
        b (int): Second nombre.
    
    Returns:
        int: Résultat de l'addition
    
    """
    return a + b 


def puissance(a: int, b: int) -> float:
    """Élève le premier nombre à la puissance du second.

    Args:
        a (int): Base.
        b (int): Exposant.

    Returns:
        float: Résultat de la puissance.
    """
    return math.pow(a, b)

