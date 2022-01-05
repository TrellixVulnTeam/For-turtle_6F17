def create_matrix_zero(x, y):
    aux = []
    for i in range(x):
        aux.append([0] * y)
    return aux


def print_matrix(matrix):
    for _ in matrix:
        print(*_)


def col_down(matrix, col_number, n=0):
    x = len(matrix)
    for i in range(x):
        n += 1
        matrix[i][col_number] = n
    return matrix, n


def col_up(matrix, col_number, n):
    x = len(matrix)
    for i in range(x - 1, -1, -1):
        n += 1
        matrix[i][col_number] = n
    return matrix, n


col = 5
row = 4
m = create_matrix_zero(row, col)
num = 0
for _ in range(col):
    if _ % 2 == 0:
        m, num = col_down(m, _, num)
    else:
        m, num = col_up(m, _, num)
print_matrix(m)
