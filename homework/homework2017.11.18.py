x =int(input("give me a number x"))
y =int(input("give me a number y"))
def Karatsuba(x,y):
    if x <10 or y<10:
        return x*y
    m =max([len(str(x)),len(str(y))])
    n = (m+1)//2
    z=10**n
    a,b=x//z,x%z
    c,d=y//z,y%z
    u = Karatsuba(a,c)
    t = Karatsuba(a,d)
    s = Karatsuba(b,c)
    w = Karatsuba(b,d)
    return u*(10**(2*n))+(t+s)*(10**n)+w
print(Karatsuba(x,y))