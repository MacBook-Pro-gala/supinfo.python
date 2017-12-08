n=int(input())
x=int(input())
def c (x,n):
    if n>0:
        return x * c(x,n-1)
    else:
        return 1
print(c(x,n))