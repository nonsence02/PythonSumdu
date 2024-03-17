n = 7
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][j] = j + 1

for i in range(n):
    k = n - i - 1
    for j in range(k):
        matrix[i][j] = 0
        k -= 1

for row in matrix:
    print(*row)
