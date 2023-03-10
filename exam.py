def fun(n,a):
    x=[[a[i],a[j]]
       for i in range(len(a))
       for j in range(len(a))
       if a[i]<a[j]
       if (a[i]+a[j])%n==0]
    print(x)
fun(5,[1,2,3,4,5])