from random import choice
from random import randint


def qsort(a):
    if len(a) <= 1:
        return a
    aux = choice(a)
    b1 = [temp for temp in a if temp < aux]
    bx = [temp for temp in a if temp == aux]
    b2 = [temp for temp in a if temp > aux]
    return qsort(b1) + bx + qsort(b2)


def sum_digit_in_number(i): # Сумма цифр в числе
    return sum(int(a) for a in str(i))

n = 10
x = [randint(10, 20) for i in range(n)]
print(x)
b = qsort(x[:len(x) // 2]) + qsort(x[len(x) // 2:])
print(b)

print(sorted(x, key=sum_digit_in_number))

X = [0] * 6
for k in range(6):
    X[k] = 11 - 3 * k
print(X)