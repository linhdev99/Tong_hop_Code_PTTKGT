import enum
from hashlib import new


def clone_arr(a):
    newa = []
    for i in a:
        temp = []
        for j in i:
            temp += [j]
        newa += [temp]
    return newa


def gaussianElimination(L, R):
    A = []
    for id, ele in enumerate(L):
        A += [L[id] + [R[id]]]
    newA = clone_arr(A)
    print("0\t:", A)
    n = len(A)
    for i in range(0, n-1):
        for j in range(i+1, n):
            for k in range(i, n+1):
                res = newA[j][k] - newA[i][k] * newA[j][i]/newA[i][i]
                # print("%d - %d * (%d - %d) = %d" %
                #       (A[j][k], A[i][k], A[j][i], A[i][i], res))
                A[j][k] = res
        newA = clone_arr(A)
        print(i+1, "\t:", newA)
    # print(A)
    print("-------------------------------")


def main():
    L = [
        [2, -1, 1],
        [4, 1, -1],
        [1, 1, 1]
    ]
    R = [1, 5, 0]
    gaussianElimination(L, R)
    L = [
        [4, 1, -1],
        [0, 1, 1],
        [2, -1, 1]
    ]
    R = [5, -1, 1]
    gaussianElimination(L, R)


if __name__ == "__main__":
    main()
