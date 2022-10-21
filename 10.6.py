import random
num = random.randint(1,100)

a = True
b = 0
while a:
    gnum = int(input("输入猜测的数："))
    if gnum == num:
       a = False
       print("你猜对了")
    else:
        if gnum >num:
           print("大了")
        else:print("小了")
    b+= 1

print(f"一共猜了{b}次")
