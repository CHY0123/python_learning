num=4
if int(input("请输入第一次猜想的数字:"))== num:
    print("猜对了")
elif int(input("不对，再猜一次:"))== num:
    print("猜对了")
elif int(input("还是不对，再猜一次:"))== num:
    print("猜对了")
else:
    print(f"sorry 我想的数字是{num}")