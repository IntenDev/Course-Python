# put your python code here
num = input().split(' ')
n = int(num[0])
m = int(num[1])
matrix = [['']*m for _ in range(n)]
b, c, d, e, f = 0, 0, n, 0, m

while b < (n * m):
    d -= 1
    f -= 1
# Верхняя строка +1
    for i in range(e, n-d):
        for j in range(e, f):
            if b != n*m:
                matrix[i][j] = str(b + 1)
                b += 1
# Правый вертикальный столбец
    for x in range(f, f+1):
        for y in range(c, n-e):
            if b != n*m:
                matrix[y][x] = str(b + 1)
                b += 1

# Нижняя горизонтальная строка
    for w in range(d, n-e):
        for z in range(f-1, e, -1):
            if b != n*m:
                matrix[w][z] = str(b + 1)
                b += 1

# Левый вертикальный столбец
    for h in range(d, c, -1):
        for g in range(e, e + 1):
            if b != n*m:
                matrix[h][g] = str(b + 1)
                b += 1
    e += 1
    c += 1
for row in range(n):
    for col in range(m):
        print(matrix[row][col].ljust(3), end=' ')
    print()