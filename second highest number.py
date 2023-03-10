def second_highest(l):
    p=sorted(set(l),reverse=True)
    return p[1]
print(second_highest([15,12,10,53,69,49,95]))




