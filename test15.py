import random
# for i in range(10):
#     print(i)
# print('*'*20)
# for i in range(0,10):
#     print(i)
# print('*'*20)
# for i in range(0,10,2):
#     print(i)
# print('*'*20)
# for i in range(1,10,2):
#     print(i)
# sum=0
# for i in range(1,51):
#     sum+=i
# print(sum)
# username="bit402"
# password="88888888"
# for i in range(3):
#     u=input("请输入账号：")
#     p=input("请输入密码：")
#     if u==username and p==password:
#         print("ok")
#         break
#     else:
#         print("用户名或密码错误，请重新输入：")
#     # if(i==2):
#     #     print("error,三次均输入错误")
# else:print("三次均输入错误，账户已冻结！")
# i=0
# while i<10:
#     print(i,sep=' ,',end=' ')
#     i+=1
# else:
#     print("over")
gold=0
dice1=0
dice2=0
if gold>=5:
    while True:
        print("是否消耗5金币开始掷骰子游戏？")
        result=input("请输入‘Y’（开始游戏）或者‘N’（离开游戏）")
