def percentage(n,p):
    sum=0

    for keys in n.keys():
        if keys==p:
            for i in n.get(keys):
                sum=sum+i
    print("{:.2f}".format(sum/3))
percentage({'alpha':[20,30,40],'beta':[30,50,70]},'beta')

