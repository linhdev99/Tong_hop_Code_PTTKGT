# a=[8,8,9,2,1,0,0,7,6,11,4,9]
# a=[3,4,5,2,1]
# a=[30,32,1,2,3,54,56,0,9]
a=[30,4,43,4,34,97,56,2,34,5,40,23,5,52,34,3,2,6,434,2,1,5,34,5,4323,443,5,7,9,6]
# a = [3,2,2,4,1]
def quicksort(left, right):
    global a
    # j = 0
    # k = 0
    j = left + 1
    k = right
    if right - left == 1:
        if a[left] > a[right]:
            a[left], a[right] = a[right],a[left]
        return
    if k > j:
        # j = left + 1
        # k = right
        print("------------------")
        print("array:   ", a)
        print("pivot:   ", a[left])
        print("cut a:   ", a[left+1:k+1])
        print("j:       ", j, a[j])
        print("k:       ", k, a[k])
        while j < k:
            while a[j] <= a[left]:
                j += 1
                if j > k:
                    break
            while a[k] >= a[left]:
                k -= 1
                if j > k:
                    break
            if j < k:
                print("++++")
                print("j:           ", j, a[j])
                print("k:           ", k, a[k])
                a[j],a[k] = a[k],a[j]
                # j += 1
                # k -= 1
                print("next array:  ", a)
        print("-+-+")
        print("pivot:   ", a[left])
        print("j:       ", j)
        print("k:       ", k, a[k])
        a[left],a[k] = a[k], a[left]
        print("array:   ", a)
        print("quick sort: ",left,k-1)
        quicksort(left,k-1)
        print("quick sort: ",k+1, right)
        quicksort(k+1,right)

quicksort(0,len(a)-1)
print(a)