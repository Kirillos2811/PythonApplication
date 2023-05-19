n = int(input("n = "))

count = 0
for i in range(n):
    if int(input()) == 0:
        count += 1

print("count =", count)