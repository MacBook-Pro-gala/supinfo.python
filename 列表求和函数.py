import random
number=int(input('give me a number'))
list1=[]
list2=[]
y=0
s=0
for x in range (number):
    z1=random.randint(1,100)
    list1.append(z1)
    z2=random.randint(1,100)
    list2.append(z2)
def sum (y,s,list1):
    if y<number-1:
        s=list1[y]+list1[y+1]+s
        y=y+1
        return sum(y,s,list1)
    else:
        return s
print(sum(0,0,list1)+sum(0,0,list2))
print(list1,list2)