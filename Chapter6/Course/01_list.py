# Création d'une liste
leisure = ['swim', 'dance', 'sing']
print(leisure)
# Longueur d'une liste
print(len(leisure))
# Test de présence d'un élément
print('basketball' in leisure)
print('DANCE' in leisure)
print('dance' in leisure)
# Index d'un élément
print(leisure.index('sing'))
# Accéder aux éléments d'une liste
print(leisure[1])
# Modifier la valeur d'un élément de liste
leisure[0] = 'ski'
print(leisure)
# Ajouter un élément à une liste
leisure.append('game')
print(leisure)
# Insérer un élément ailleurs qu'à la fin
leisure.insert(3, 'climb')
print(leisure)
# Enlever un élément de liste
leisure.remove('climb')
print(leisure)
# Enlever un élément ailleurs avec son index
leisure.pop(1)
print(leisure)
# Vider une liste
leisure.clear()
print(leisure)

print('--------------------')
# Concaténer deux listes
month = ['Janvier', 'Février', 'Mars']
season = ['Automne', 'Hiver', 'Printemps', 'Eté']
various_time = month + season
print(various_time)
# Étendre une liste
month.extend(season)
print(month)
print('--------------------')

rainbow = ['rouge', 'orange', 'jaune', 'vert', 'bleu', 'indigo', 'violet']
print(rainbow[1:4])
print(rainbow[2:])  # print(rainbow[2:7])
print(rainbow[:5])
print(rainbow[-5:-2])

