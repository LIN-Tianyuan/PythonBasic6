a = 1
while a < 10:
    b = 1
    while b < a + 1:
        print("%d * %d = %d" % (b, a, b * a), end="\t")
        b = b + 1
    print()
    a = a + 1

