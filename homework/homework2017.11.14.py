s=[]
sn = 0
s.extend(input('give me a world'))
vowels=('a','e','i','o','u','A','E','I','O','U')
def vowelsNumber(sn):
        for x in vowels:
            sn = sn + s .count(x)
        return sn
print('you have ',vowelsNumber(sn),'vowels worlds')