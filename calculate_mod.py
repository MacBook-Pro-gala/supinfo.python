def c_to_f(celsius):#摄氏度转华氏度
   return celsius*9.0/5+32

def dcsum(a1,n,d):#等差数列求和
   return a1*n+n*(n-1)*d/2

def dbsum(a1,n,q):#等比数列求和
   return a1*(1-q**n)/(1-q)

def plus(x,y):#x+y
   return x + y

def substract(x, y):#x-y
   sn = x - y

   return sn
def multiplicate(x,y):#x*y
   sn = x * y

   return sn
def divide(x,y):#x/y
   sn = x / y

   return sn

def quick(list):#快速排序（比大小)
    if list == [] or len(list) == 1:
        return list
    base = list[0]
    left_l, right_l = [], []
    for i in list[1:]:
        if i >= base:
            right_l.append(i)
        else:
            left_l.append(i)
    left_l = quick(left_l)
    right_l = quick(right_l)
    return left_l + [base] + right_l

def merge_sort(x):#归并排序（比大小）

    if len(x) < 2:return x

    result,mid = [],int(len(x)/2)

    y = merge_sort(x[:mid])
    z = merge_sort(x[mid:])

    while (len(y) > 0) and (len(z) > 0):
            if y[0] > z[0]:result.append(z.pop(0))
            else:result.append(y.pop(0))

    result.extend(y+z)
    return result