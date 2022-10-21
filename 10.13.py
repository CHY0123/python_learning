mylist=[21,25,21,23,22,20]
mylist.append(31)
print(f"{mylist}")
mylist2=[29,33,30]
mylist.extend(mylist2)
print(f"{mylist}")
del mylist[0]
print(f"{mylist}")
del mylist[-1]
print(f"{mylist}")
num=mylist.index(31)
print(f"{num}")