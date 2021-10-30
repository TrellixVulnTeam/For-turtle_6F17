def f(w, x, y, z):
    return not(not y or (x == w)) and (not z or x)


def g(scope, m, prefix = None):
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return prefix
    for element in scope:
        if element in prefix:
            continue
        prefix.append(element)
        g(scope, m - 1, prefix)
        prefix.pop()

q = (0, 1)

col1 = [q, 0, q]
col2 = [1, q, 0]
col3 = [1, q, 1]
col4 = [q, 0, 0]
result = [1, 1, 1]

aux = ['w', 'x', 'y', 'z']
g(aux, len(aux))

f(0, y=1,x=2, z=5)