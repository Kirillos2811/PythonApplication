def print_list(index, lst):
    print(lst[index], end=" ")
    if index == len(lst) - 1:
        print("Конец списка")
    else:
        print_list(index + 1, lst)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print_list(0, my_list)