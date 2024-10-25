# 0 + 1 + 2 + 3 + ... + 100
a = 0
b = 0
while a < 101:
    b = a + b
    a = a + 1
print("La somme des nombres compris entre 0 et 100 donne " + str(b) + ".")