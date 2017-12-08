import time
i = 5
for i in range(5,-1,-1):
    print ("\t"u"系统将在%d秒后关机"% i,)
    time.sleep(1)
    if i == 0:
        print("finshed")


