from random import randint as rnd
from os import system

def randBool(chance):
    mxr = 100
    if rnd(1, mxr) <= chance:
        return True
    return False

def randCell(w, h):
    return rnd(0, h - 1), rnd(0, w - 1)

def checkBounds(x, y, w, h):
    if x >= 0 and y >= 0 and x < h and y < w:
        return True
    return False


def two_dim_obj_list_to_json(lst, m, n):
    res = []
    for i in range(n):
        res.append([])
        for j in range(m):
            if lst[i][j] is None:
                res[i].append("None")
            else:
                res[i].append(lst[i][j].serialize())
    
    return res

def two_dim_obj_list_from_json(lst, m, n):
    from objects import Field, Tree, River, Fire, \
                        Cloud, ThunderCloud, Hospital, Shop
    res = []
    for i in range(n):
        res.append([])
        for j in range(m):
            res[i].append(eval(lst[i][j]))
    
    return res


def gameOver(score):
    system("clear")
    print("💀" * 15)
    print("\tGAME OVER!")
    print(f"\tYOUR SCORE IS {score}")
    print("💀" * 15)