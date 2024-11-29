import random

computer = random.randint(1, 100)
count = 0
while True:
    player = int(input("Veuillez entrer un nombre: "))
    count = count + 1
    if count == 6:
        print("Game over, vous avez échoué!")
        break
    if player > computer:
        print("Plus petit.")
    elif player < computer:
        print("Plus grand.")
    else:
        print("Vous avez bien deviné " + str(count) + " fois au total.")
        break