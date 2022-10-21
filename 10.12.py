# cont = 0
# money = 5000000
# name = input("请输入你的姓名：")
#
# def search():
#     print(f"账户余额{money}")
#     input("选择退出或继续{exit}或{cont}：")
#     if "cont":
#         search()
#     else:
#         menu()
#
# def save():
#     add = int(input("请输入你要存入的余额："))
#     global money
#     money = add + money
#     print(f"余额剩余{money}")
#     input("选择退出或继续{exit}或{cont}：")
#     if not "cont":
#         save()
#     else:
#         menu()
#
# def put():
#     s = int(input("请输入你要拿走的金额："))
#     global money
#     money -= s
#     print(f"余额剩余{money}")
#     input("选择退出或继续{exit}或{cont}：")
#     if "cont":
#        put()
#     else:
#         menu()
#
# def menu():
#     print(f"{name}欢迎你使用ATM系统，请选择你的操作：")
#     print("查询余额 1\t")
#     print("存款 2\t")
#     print("取款 3\t")
#     print("退出 4\t")
#
#     choose = int(input("请输入你的选择："))
#
#     if choose == 1:
#         search()
#     elif choose == 2:
#         save()
#     elif choose == 3:
#         put()
#     else:
#         print("欢迎你下次使用")
#
#
# menu()
