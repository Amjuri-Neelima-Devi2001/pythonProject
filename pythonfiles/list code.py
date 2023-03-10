def fun(list1,list2):
    list1.sort()
    list2.sort()
    list1idx=0
    list2idx=0
    current=0
    smallest=float("inf")
    result=[]
    while list1idx<len(list1) and list2idx<len(list2):
        first=list1[list1idx]
        second=list2[list2idx]
        if first>second:
            current=first-second
            list2idx+=1
        elif first<second:
            curren=second-first
            list1idx+=1
        else:
            return [first,second]
        if smallest>current:
            smallest=current
            result=[first,second]
    return result
m=fun([2,20],[21,9])
print(m)