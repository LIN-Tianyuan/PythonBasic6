year = int(input("Veuillez entrer une année: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("%d est une année bissextile." % year)
else:
    print("%d n'est pas une année bissextile." % year)
