"""
a = "*"
while a:
    if a == "**********":
        break
    print(a)
    a = a + "*"
"""

a = 0
while a < 9:
    b = 0
    while b < a + 1:
        print("*", end="")
        b = b + 1
    print()
    a = a + 1


# print("*", end="")
# print("*")

