# my_list=[1,2,3,4,5,6,7,8,9,10]
# my_list2=[]
# my_list3=[]
# index=0
# while index<len(my_list):
#     if my_list[index]%2==0:
#         my_list2.append(my_list[index])
#     index+=1
# print(f"{my_list2}")
#
# for i in my_list:
#     if i%2==0:
#         my_list3.append(i)
# print(f"{my_list3}")

# list=('周杰伦',11,['football','music'])
# num=list.index(11)
# print(f"{num}")
#
# print(list[0])
# del list[2][0]
# print(f"{list}")
# list[2].append("coding")
# print(f"{list}")
#
# str="itheima itcast boxuegu"
# num=str.count("it")
# print(f"{num}个it字符")
# str2=str.replace(" ","|")
# print(f"{str2}")
# str3=str2.split("|")
# print(f"{str3}")


# str="万过月薪，员序程马黑来，nohtyP学"
# str2=str[::-1]
# print(f"{str2}")
# str3=str2[8:14]
# print(f"{str3}")



# my_list=['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
# list=set()
# for i in my_list:
#     list.add(i)
# print(f"{list}")

# dict={"王力宏":{
#         "部门":"科技部",
#         "工资":3000,
#         "级别":1
#       },
#       "周杰伦":{
#         "部门":"市场部",
#         "工资":5000,
#         "级别":2
#       },
#       "林俊杰": {
#         "部门": "市场部",
#         "工资": 7000,
#         "级别": 3
#       },
#       "张学友": {
#         "部门": "科技部",
#         "工资": 4000,
#         "级别": 1
#       },
#       "刘德华": {
#         "部门": "市场部",
#         "工资": 6000,
#         "级别": 2
#       }
# }
# for i in dict:
#     if dict[i]["级别"]==1:
#          # dict_new=dict[i]
#          # dict_new["级别"]+=1
#          # dict_new["工资"]+=1000
#          # dict[i]=dict_new
#
#          dict[i]["级别"] += 1
#          dict[i]["工资"] += 1000
#
# print(f"{dict}")

# count=0
# f=open("D:\新建 文本文档.txt","r",encoding="UTF-8")
# # print(f"{f.read()}")
# for line in f:
#     list(line)
#     if "itheima":
#         count+=1
# print(f"{count}")
# f.close

# fr=open("D:/bili.txt","r",encoding="UTF-8")
#
# fw=open("D:/bili.tex.bac","w",encoding="UTF-8")
# for line in fr:
#     line=line.strip()
#     if line.split(",")[-1] == "测试":
#         continue
#
#     fw.write(line)
#     fw.write("\n")
#
#
# fr.close()
# fw.close()

