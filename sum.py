def fun(n):
    a=[]
    sum=0
    for i in range(1,n+1):
        while i>0:
            m=int(i%10)
            i=int(i/10)
            a.append(m)
        a.reverse()
        print(a)
        for j in range(1,len(a)+1):
            sum=sum+a[j-1]**j
        #print(sum)
        if sum==i:
            print(i)

fun(123)