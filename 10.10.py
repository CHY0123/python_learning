import random
num = random.randint(1,10)
guess_number=int(input("请输入你猜测的数字："))

if guess_number == num:
    print("第一次就猜对了")
else:
     if guess_number < num:
         print("猜的小了")
     else:
         print("猜的大了")

guess_number=int(input("请输入你猜测的数字："))
if guess_number == num:
    print("第二次就猜对了")
else:
    if guess_number < num:
         print("猜的小了")
    else:
         print("猜的大了")

guess_number=int(input("请输入你猜测的数字："))
if guess_number == num:
    print("最后一次猜对了")
else:print("没有猜对")