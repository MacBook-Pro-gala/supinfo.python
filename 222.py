def hour(x):
    sn1=x//3600
    return sn1
def min(x):
    sn2=(x-hour(x)*3600)/60
    return sn2
x=int(input('give me seconds'))
y=x
y=y-hour(x)*3600-min(x)*60
print('hour=',hour(x),'min=',min(x),'seconds=',y)