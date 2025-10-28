"""
    Arithmetique
    
    En python, l'opérateur `/` retourne toujours un float, même avec deux entiers.
    Les autres opérations retournent un float si au moins un opérande est un float.

"""

# Addition
addition = 3 + 4.0        # Résultat : 7.0 (float)

# Multiplication
multiplication = 3 * 4.0  # Résultat : 12.0 (float)

# Soustraction
soustraction = 3 - 2      # Résultat : 1 (int)

# Division
division = 6 / 2          # Résultat : 3.0 (float)

# Division si int nécessaire
division = 7 // 4         # Résultat : 1 (int)
division = 6 // 2         # Résultat : 3 (int)

# Modulo
modulo = 7 % 4            # Résultat : 3 (reste de la division entière)

# Conversion int / float
int(6 / 2)                # Résultat : 3 (int)
float(1 + 2)              # Résultat : 3.0 (float)
