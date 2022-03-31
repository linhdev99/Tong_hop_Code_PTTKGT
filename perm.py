def perm(a):
    Ps = [str(a[0])]
    for i in a[1:]:
        newPs = []
        for p in Ps:
            for x in range(len(p),-1,-1):
                temp = p
                temp = temp[:x] + str(i) + temp[x:]
                newPs += [temp]
        Ps = newPs
    print("So hoan vi: ", len(Ps))
    print("Cac hoan vi")
    print(Ps)
perm([1,2,3,4])
