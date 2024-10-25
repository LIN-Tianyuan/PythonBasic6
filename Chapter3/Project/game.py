"""
player = int(input("Que voulez-vous jouer? Pierre(1) / Ciseaux(2) / Papier(3)."))
computer = 1
if player == computer:
    print("Les deux côtés sont à égalité.")
elif player == 2:
    print("L'ordinateur gagne.")
else:
    print("Le joueur gagne.")
"""

import random

computer = random.randint(1, 3)
player = int(input("Que voulez-vous jouer? Pierre(1) / Ciseau(2) / Papier(3)"))
print(computer)
"""
if computer == 1:
    if player == 1:
        print("Les deux côtés sont à égalité.")
    elif player == 2:
        print("L'ordinateur gagne.")
    else:
        print("Le joueur gagne.")
elif computer == 2:
    if player == 1:
        print("Le joueur gagne.")
    elif player == 2:
        print("Les deux côtés sont à égalité.")
    else:
        print("L'ordinateur gagne.")
else:
    if player == 1:
        print("L'ordinateur gagne.")
    elif player == 2:
        print("Le joueur gagne.")
    else:
        print("Les deux côtés sont à égalité.")
"""

if computer == player:
    print("Les deux côtés sont à égalité.")
elif (computer == 1 and player == 2) or (computer == 2 and player == 3) or (computer == 3 and player == 1):
    print("L'ordinateur gagne.")
else:
    print("Le joueur gagne.")


