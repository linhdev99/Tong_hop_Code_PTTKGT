from math import *


def clone_arr(a):
    b = []
    for i in a:
        b += [i]
    return b


def mergesort(left, right, a):
    m = floor((right+left) / 2)
    b = clone_arr(a)
    if right > left:
        mergesort(left, m, a)
        mergesort(m+1, right, a)
        for i in range(left, m+1):
            b[i] = a[i]
        for j in range(m+1, right+1):
            b[m+right+1-j] = a[j]
        i = left
        j = right
        for k in range(left, right+1):  # 0 1 2 # 5 4 3
            if b[i] < b[j]:
                a[k] = b[i]
                i += 1
            else:
                a[k] = b[j]
                j -= 1
    return a


def MergeSort(arr):
    global a
    a = clone_arr(arr)
    return mergesort(0, len(a)-1, a)


def Split(arr):
    if arr[0] == arr[1] or arr[1] == arr[2] or arr[2] == arr[3]:
        return 1
    newArr = [0, 0, 0, 0]
    for id, ele in enumerate(arr):
        if ele > 0:
            temp = clone_arr(arr)
            temp[id] = temp[id] - 1
            # print("temp = ", temp)
            newArr[id] = -1 * Split(temp)
        # print("newArr = ", newArr)
    if 1 in newArr:
        return 1
    return -1


def SplitChocolate(arr):
    arr = MergeSort(arr)
    print("[a, b, c, d] =", arr)
    if arr[0] == arr[1] and arr[2] == arr[3]:
        return -1
    return Split(arr)


def CreateChocolate(x, y, w, h):
    mat = []
    print("\nChocolate:\n")
    # in dong dau
    print("\t", end="")
    for j in range(h):
        print(" ",j,"",end="")
    print("\n")
    #in phan duoi
    for i in range(w):
        temp = []
        print(i, "\t|", end="")
        for j in range(h):
            temp += ["O"]
            if x == i and y == j:
                print(" X |", end="")
            else:
                print(" O |", end="")
        print("\n")
        mat += [temp]
    mat[x][y] = ["X"]


def StartGame():
    print("Width: ")
    w = int(input())
    print("Height: ")
    h = int(input())
    print("X: ")
    x = int(input())
    print("Y: ")
    y = int(input())
    if x > w or y > h:
        print("Can't create chocolate!")
        StartGame()
    CreateChocolate(y, x, h, w)
    win = SplitChocolate([x, y, w-x-1, h-y-1])
    print("Player ", 2 if win == -1 else win, " Win!")
    print("-------------------------")
    print("1: Start Game\n2: Exit\nEnter number:")
    state = int(input())
    if state == 1:
        StartGame()


if __name__ == "__main__":
    StartGame()
