# a=[8,8,9,2,1,0,0,7,6,11,4,9]
# a=[3,4,5,2,1]
# a=[30,32,1,2,3,54,56,0,9]
# a=[30,4,43,4,34,97,56,2,34,5,40,23,5,52,34,3,2,6,434,2,1,5,34,5,4323,443,5,7,9,6]
a=['e','a','s','y','q','u','e','s','t','i','o','n']
# a = [3,2,2,4,1]
# a = [51, 87, 17, 21, 20, 48, 49, 23, 80, 60, 34, 36, 50, 56, 93, 59, 17, 59, 95, 3, 78, 1, 65, 19, 63, 56, 27, 54, 1, 19, 31, 21, 43, 40, 95, 80, 27, 40, 44, 77, 70, 3, 57, 59, 25, 27, 24, 99, 96, 71,
#      92, 19, 62, 80, 11, 49, 5, 27, 54, 73, 2, 21, 24, 49, 36, 20, 51, 4, 41, 50, 55, 31, 25, 22, 42, 62, 88, 48, 13, 84, 56, 93, 36, 20, 29, 75, 65, 12, 37, 94, 42, 33, 97, 60, 62, 47, 25, 13, 51, 5]


def quicksort(left, right):
    global a
    # j = 0
    # k = 0
    j = left + 1
    k = right
    if right - left == 1:
        if a[left] > a[right]:
            a[left], a[right] = a[right], a[left]
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
            while a[j] < a[left]:
                j += 1
                if j > k:
                    break
            while a[k] > a[left]:
                k -= 1
                if j > k:
                    break
            if j < k:
                print("++++")
                print("j:           ", j, a[j])
                print("k:           ", k, a[k])
                a[j], a[k] = a[k], a[j]
                if a[j] == a[k]:
                    j += 1
                # j += 1
                # k -= 1
                print("next array:  ", a)
        print("-+-+")
        print("pivot:   ", a[left])
        print("j:       ", j)
        print("k:       ", k, a[k])
        a[left], a[k] = a[k], a[left]
        print("array:   ", a)
        print("quick sort: ", left, k-1)
        quicksort(left, k-1)
        print("quick sort: ", k+1, right)
        quicksort(k+1, right)


quicksort(0, len(a)-1)
print(a)
