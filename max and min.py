def fun(n):
    #print(sorted(n))
    min=0
    max=0
    for i in range(len(n)):
        if i<int(len(n)/2):
            min=min+n[i]
        else:
            max=max+n[i]
    print(min)
    print(max)
fun([21,13,16,18,24,67,32,54,89,76])