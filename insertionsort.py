def insertionsort(a):
    print("start")
    print("1    --> ",a)
    for i in range(1,len(a)):
        v = a[i]
        j = i
        while a[j-1] > v:
            a[j] = a[j-1]
            j -= 1
            if j <= 0:
                break
        a[j] = v
        print(i, "  --> ", a)
    print("end")
    return a

arr=[30,4,43,4,34,97,56,2,34,5,40,23,5,52,34,3,2,6,434,2,1,5,34,5,4323,443,5,7,9,6]
insertionsort(arr)