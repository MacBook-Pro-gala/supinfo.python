x=int(input('give me a number x'))
y=int(input('give me a number y'))
def Karatsuba (x,y):
    if x<=10 and y<=10:
        return (x*y)
    else:
        b=len(str(x))
        c=len(str(y))
        d=max(b,c)
        xz=x//10**(b-1)
        xy=x%10**(b-1)
        yz=y//10**(c-1)
        yy=y%10**(c-1)
        if xy>10 and yy>10:
                return (xz*10**(b-1)+Karatsuba(xy,xy))*(yz*10**(c-1)+Karatsuba(yy,yy))
        elif xy<10 and yy>10:
                return (xz*10**(b-1)+xy)*(yz*10**(c-1)+Karatsuba(yy,yy))
        elif xy>10 and yy<10:
                return (xz * 10 ** (b - 1) +Karatsuba(xy,xy) ) * (yz * 10 ** (c - 1) + yy)
        elif xy<10 and yy<10:
                return (xz * 10 ** (b - 1) + xy) * (yz * 10 ** (c - 1) + yy)
print(Karatsuba(x,y))