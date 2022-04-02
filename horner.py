def horner1(P, x):
    res = P[0]
    for i in range(1, len(P)):
        res = x*res+P[i]
        print(i, res)
    print(res)


def horner2(P, x):
    res = P[-1]
    for i in range(len(P)-2, -1, -1):
        res = x*res+P[i]
    print(res)


arr1 = [1,0,0,-2,0,1,-6]
arr2 = [3, -1, 0, 2, 5]

horner1(arr1, 3)
horner1(arr2, -2)

horner2(arr1[::-1], 3)
horner2(arr2[::-1], -2)
