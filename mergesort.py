from math import *
def clone_arr(a):
    b = []
    for i in a:
        b += [None]
    return b
a=[8,8,9,2,1,0,0,7,6,11,4,9]
def mergesort(left, right):
    i = 0
    j = 0
    m = floor((right+left) / 2)
    b = clone_arr(a)
    print("-----")
    print("m     =   ", m)
    print("left  =   ", left)
    print("right =   ", right)
    print(a[left:right+1])
    if right > left:
        mergesort(left,m)
        mergesort(m+1,right)
        for i in range(left,m+1):  # 0 1 2 # 3 4 5
            b[i] = a[i]
        for j in range(m+1,right+1):
            b[m+right+1-j] = a[j]
        i = left
        j = right
        print("b = ", b)
        print("i = ", left)
        print("j = ", right)
        for k in range(left, right+1):
            if b[i] < b[j]:
                a[k] = b[i]
                i += 1
            else:
                a[k] = b[j]
                j -= 1
        print("a = ", a)
            
mergesort(0,len(a)-1)
print(a)
