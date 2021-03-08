import random


def bool19_1(a, b, c):
    x = True if a == -b or a == -c or b == -c else False
    return x


def bool19_2(a, b, c):
    x = True if (a + b + c) in (a, b, c) else False
    return x


k = 0
for i in range(10000000):
    a = random.randint(-1000, 1000)
    b = random.randint(-1000, 1000)
    c = random.randint(-1000, 1000)
    if bool19_1(a, b, c) == bool19_2(a, b, c):
        k += 1

print("Ok" if k == 10000000 else "Faile")
