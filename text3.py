list=[6,5,3,1,8,7,2,4]
count=len(list)
for n in range(0,len(list),2):
    if list[n]>list[n+1]:
        list[n],list[n+1]=list[n+1],list[n]
    else:
        list[n], list[n + 1] = list[n], list[n+1]
for z in range(0,len(list),4):
    if list[n]>list[n+2]:
        list[n], list[n + 2] = list[n + 2], list[n]
        if list[n+2]>list[n+3]:
            list[n+3],list[n+1]=list[n+1],list[n+3]
        else:
            list[n+2],list[n+1]=list[n+1],list[n+2]
    else:
        list[n], list[n + 2] = list[n], list[n+2]
        if list[n + 2] > list[n + 3]:
            list[n + 3], list[n + 1] = list[n + 1], list[n + 3]
        else:
            list[n + 2], list[n + 1] = list[n + 1], list[n + 2]
list=list[0:y]