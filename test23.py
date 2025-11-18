import random
# n=0
# lis = ["面包", "牛奶", "牛奶", "辣条", "薯片", "雪糕", "牛奶","牛奶","糖果", "瓜子", "牛奶"]
# # while n<len(lis):
# #     if(lis[n]=="牛奶"):
# #         lis.remove(lis[n])
# #     else:
# #         n+=1
# # print(lis)
# #for i in lis[::-1]:
# #     if(i=="牛奶"):
# #         lis.remove(i)
# # print(lis)
# # for i in range(lis.count("牛奶")):
# #     lis.remove("牛奶")
# # print(lis)
# lis.clear()
# print(lis)
# lis=[1,1,5,6,7,9,2,8,3,1,0]
# print(lis.count(10))
# print(lis.count(3))
# print(lis.count(1))
# del lis[6]
# print(lis)
# lis.clear()
# print(lis)
# lis.append(2)
# print(lis)
# del lis
# print(lis)
# lis1=[1,2,3,4,5]
# print(id(lis1))
# lis2=lis1
# lis2.append(6)
# print(id(lis2))
# print(lis2)
# print(lis1)
# lis1.clear()
# print(lis2)
# del lis1
# print(lis2)
# a="hello"
# b=a
# c=a
# del a
# print(b,c)
# lis=[]
# for i in range(8):
#     n=random.randint(1,20)
#     lis.append(n)
# print(lis)
# # lis.sort()
# # print(lis)
# lis.sort(reverse=True)
# print(lis)
lis=[]
for i in range(8):
    n=random.randint(1,100)
    lis.append(n)
print(lis)
lis.sort()
print(lis)
a=int(input("请输入一个整数："))
lis.append(a)
print(lis)
lis.sort()
print(lis)