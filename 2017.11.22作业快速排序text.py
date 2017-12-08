list1=[2,10,3,6,5]
list2=[]
def quick(list1,list2):
    count = len(list1)
    x1 = list1[count // 2]
    for y in range(0,count-1):
        if list1[y]<x1:
            list1.insert(0,list[y])
            list1.remove(y+1)
        elif list1[y]==x1:
            if y==count//2+1 or y==count//2-1:
                continue
            elif y==count//2:
                continue
            else:
                a = list1[y]
                list1.remove(list1[y])
                list1.insert(count // 2 - 1, a)
        else:
            b=list1[y]
            list1.remove(list1[y])
            list1.append(b)


    count = len(list2)
    x2 = list2[count // 2]
    for z in range(0, count - 1):
        if list1[z] < x2:
                    list1.insert(0, list[z])
                    list1.remove(z + 1)
        elif list1[z] == x2:
            if z == count // 2 + 1 or z == count // 2 - 1:
                    continue
            elif z == count // 2:
                    continue
            else:
                    c = list1[z]
                    list1.remove(list1[z])
                    list1.insert(count // 2 - 1, c)
        else:
            d = list1[y]
            list1.remove(list1[y])
            list1.append(d)
    return quick(list1[0:x1],list2[0:x2])
print(quick(list1,list2))

