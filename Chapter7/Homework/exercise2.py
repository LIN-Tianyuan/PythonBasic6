def my_max(n1, n2, n3):
    max_number = n1
    if max_number < n2:
        max_number = n2
        if max_number < n3:
            max_number = n3
    return max_number

print(my_max(2, 5, 4))