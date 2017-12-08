#***************************
#猜数游戏
#作者：刘宇涵
#最近更新日期：2017.11.9
#***************************
run = True
import random
answer = random.randint(1, 25)
chance = 3
while run == True:        #只要run等于true就一直循环
    x = int(input("guess  a number which is from 1-25.""(And You have only three chances)"))

    if x < answer:
     print("too small")
     chance = chance - 1
     if chance > 0:
       run = True
     else:
         b = int(input("\033[4;31;0myou are Defeated.""Want to try again?{1=yes,2=no}\033[0m"))
         if b == 1:

          run = True
          chance = 3
          answer = random.randint(1, 25)
         else:
          run =False


    elif x > answer:
     print("too big")
     chance = chance - 1
     if chance > 0:
       run = True
     else:
         b = int(input("\033[4;31;0myou are Defeated.""Want to try again?{1=yes,2=no}\033[0m"))
         if b == 1:
          run = True
          chance = 3
          answer = random.randint(1, 25)
         else:
          run =False

    else:
     print("Congratulations")
     c = int(input("\033[4;34;0myou are Finshed.""Want to try again?{1=yes,2=no}\033[0m"))
     if c == 1:
       run = True
       chance = 3
       answer = random.randint(1, 25)
     else:
       run = False
