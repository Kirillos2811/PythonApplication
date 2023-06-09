import random as rnd

def print_list(lst):
    for item  in lst:
        print(*item)

n = int(input("Rows number = "))
m = int(input("Columns number = "))

matrix1 = [[0 for i in range(m)] for i in range(n)]
matrix2 = [[0 for i in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        matrix1[i][j] = rnd.randint(1, 100)
        matrix2[i][j] = rnd.randint(1, 100)

res_matrix = [[0 for i in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        res_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

print("Matrix 1:")
print_list(matrix1)
print("Matrix 2:")
print_list(matrix2)
print("Resulting matrix:")
print_list(res_matrix)
