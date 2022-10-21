# for i in range(1,10):
#
#     for j in range(1,i+1):
#         print(f"{j}*{i}={i*j}\t",end='')
#
#     print()

# money=10000
# for i in range(1,21):
#     a=0
#     import random
#     num = random.randint(1, 10)
#     if num <5:
#         print(f"员工{i}，绩效分{num}，低于5，不发工资")
#         continue
#     elif num>=5:
#         money-=1000
#         print(f"员工{i}，绩效{num}，向员工{i}发放工资1000，账户余额还剩{money}")
#         if money == 0:
#              print("没钱了")
#              break
#         continue

# money=10000
# for i in range(1,21):
#     import random
#     num = random.randint(1, 10)
#
#     if num<5:
#         print(f"员工{i}，绩效分{num}，低于5，不发工资")
#         continue
#
#     if money>=1000:
#         money-=1000
#         print(f"员工{i}，绩效{num}，向员工{i}发放工资1000，账户余额还剩{money}")
#     else:
#         print("没钱了")
#         break

# def cewen(x):
#     print(""
#           ""
#           "你的体温：{x}")
#     if x >= 37.3:
#         print(f"体温{x},体温过高不给进入")
#     else: print("体温正常")
#
#
# cewen(float(input("输入体温：")))

# def add(x,y):
#     """
#
#     :param x:
#     :param y:
#     :return:
#     """
#     result=x+y
#     return result
cont=0
money=5000000
name=input("请输入你的姓名：")
def search():
    print(f"账户余额{money}")
    answer = input("选择退出或继续{exit}或{cont}：")
    if answer != cont:
        return menu()

def save():
    add=int(input("请输入你要存入的余额："))
    global money
    money=add+money
    print(f"余额剩余{money}")
    answer=input("选择退出或继续{exit}或{cont}：")
    if answer!=cont:
        return menu()

def put():
    s=int(input("请输入你要拿走的金额："))
    global money
    money-=s
    print(f"余额剩余{money}")
    answer = input("选择退出或继续{exit}或{cont}：")
    if answer != cont:
         return menu()

def menu():
    print(f"{name}欢迎你使用ATM系统，请选择你的操作：")
    print("查询余额 1\t")
    print("存款 2\t")
    print("取款 3\t")
    print("退出 4\t")

    choose=int(input("请输入你的选择："))
    
    if choose == 1:
        search()
    elif choose==2:
        save()
    elif choose==3:
        put()
    else:
        print("欢迎你下次使用")


menu()