def fib(n):
    global d
    if n in d:
        return d[n]
    else:
        aux = 1 if n < 3 else fib(n-1) + fib(n-2)
        d[n] = aux
        return aux


d = {}
for i in range(1, 51):
    print(f'FIB({i}) = {fib(i)}')
