def factorial(a):
    res = 1
    for i in range(1, a + 1):
        res *= i
    return res

a = int(input())
lst = []
for i in reversed(range(1, factorial(a) + 1)):
    lst.append(factorial(i))

print(lst)