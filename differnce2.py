def diff2(l):
    count=0
    k=sorted(l,reverse=True)
    for i in range(len(k)):
        for j in range(len(k)):
            if (l[i]-l[j])==2:
                count=count+1
    return count
print(diff2([1,5,3,4,2]))