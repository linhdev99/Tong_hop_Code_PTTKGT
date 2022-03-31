def isFibonacci(k):
    a = [1,1]
    i = 2
    if k == 1: 
        return True
    while True:
        a.append(a[i-1]+a[i-2])
        print(a)
        if a[i] == k:
            return True
        elif a[i] > k:
            return False
        i += 1

print(isFibonacci(56))