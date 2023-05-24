n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

arr.reverse()
print(*arr)