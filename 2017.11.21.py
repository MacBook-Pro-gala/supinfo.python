#方法1
list=[3,4,8,2,6]
listnew=[]
x=0
def solution (x):
    for z in range(0,5):
        x=min(list)
        listnew.insert(z,x)
        list.remove(x)
    return listnew
print(solution(x))



#方法2
list=[3,4,8,2,6]
listnew=list[:]
x=True
while x==True:
    a=0
    for n in range(0,4):
        if list[n]>list[n+1]:
            list[n],list[n+1]=list[n+1],list[n]
            a=1
        else:
            list[n],list[n + 1] = list[n],list[n+1]
    if a==0:
       x=False
    else:
        x=True
print(list)


#插入排序
list=[5,3,1,4,2]
count=len(list)
for n in range(0,count-1):
    while n>=0:
        if list[n] > list[n + 1]:
            list[n],list[n+1]=list[n+1],list[n]
        n=n-1
print(list)