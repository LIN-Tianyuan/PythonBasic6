"""
age = int(input("Veuillez entre votre âge: "))

'''
if age >= 0:
    if age < 120:
        print("correct.")
    else:
        print("Incorrect.")
else:
    print("Incorrect.")
'''

if age >= 0 and age < 120:
    print("Age correct.")
else:
    print("Age incorrect.")
"""

python_score = int(input("Veuillez entrer votre score Python: "))
c_score = int(input("Veuillez entrer votre score C: "))
if python_score > 60 or c_score > 60:
    print("Reussir l'examen.")
else:
    print("Continuez.")

