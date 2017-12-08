def produit(y,c,v,b):
    p = 1
    for x in [2,-4,5,3]:
        p *= x
    return p

print(produit(2,-4,5,3))

sn=0
s=[]
s.append(input())
vowels=('a','e','i','o','u')
def vowelsNumber(x):
    for x in vowels:
        sn=sn+s.count(x)
print(sn)