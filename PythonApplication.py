number = int(input("number = "))

if number != 0:
    if number > 0:
        print("положительное", end = " ")
    else:
        print("отрицательное", end = " ")

    if number % 2 == 0:
        print("четное", end = " ")
    else:
        print("нечетное", end = " ")
else:
    print("нулевое", end = " ")

print("число")