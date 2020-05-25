def missing(l):
    l1=[]
    for i in range(1,26):
        if i not in l:
            l1.append(i)
    return l1

list1 = [1,2,6,8,9,10,11,12]

print(missing(list1))