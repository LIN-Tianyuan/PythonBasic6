list_number = [32, 5, 12, 8, 3, 75, 2, 15, 82983, 23547, 2221, 2, 2458, 2, 3]
# print(max(list_number))
i = 1
max_number = list_number[0]
while i < len(list_number):
    if list_number[i] > max_number:
        max_number = list_number[i]
    i = i + 1

print("Le plus grand élément de cette liste a la valeur est " + str(max_number) + ".")
