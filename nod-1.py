def nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

print (nod(75,30))