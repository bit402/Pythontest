import random
# a=1
# b=2
# # if(a<b):
# #     c=a
# # else:
# #     c=b
# # print(a,b,c)
# c=a if a<b else b
# print(a,b,c)
# print('a'*5 ) if a<b else print("b*5")
# i=1
# while i<=50:
#     if i%3==0:
#         print(i)
#     i+=1
# i=1
# sum=0
# while i<=10:
#     sum+=i
#     i+=1
# print(sum)
# count=5
# numbers=0
# result=random.randint(1,100)
# for i in range(5):
#     numbers=int(input("请猜数字1-100之间的一个数字："))
#     count-=1
#     if numbers==result:
#         print("恭喜你猜对了！！！")
#         print("共用了"+str(5-count)+"次机会")
#         break
#     elif numbers<result:
#         print("猜小了")
#         print("您还有"+str(count)+"次机会")
#     elif numbers>result:
#         print("猜大了")
#         print("您还有" + str(count) + "次机会")
#     if count==0:
#         print("对不起，次数用完了")
#         break
n=0
cwin=0
nwin=0
draw=0
for i in range(3):
    print("欢迎来到猜拳游戏以下为对应的规则：")
    print("0:拳头，1：剪刀，2：布")
    n=int(input("请开始选择对应的编号："))
    while n not in [0,1,2]:
        print("输入不合法，请重新输入：")
        n = int(input("请开始选择对应的编号："))
    if n == 0:
        print("玩家出石头")
    elif n == 1:
        print("玩家出剪刀")
    elif n == 2:
        print("玩家出布")
    computer = random.randint(0,2)
    if computer == 0:
        print("电脑出石头")
    elif computer == 1:
        print("电脑出剪刀")
    elif computer == 2:
        print("电脑出布")
    if (n==0 and computer==0) or (n==1 and computer==1) or (n==2 and computer==2):
        print("平局一次")
        draw+=1
    elif(n==0 and computer==1) or(n==1 and computer==2) or (n==2 and computer==0):
        print("玩家获胜一次")
        nwin+=1
    elif(n==0 and computer==2) or(n==1 and computer==0) or (n==2 and computer==1):
        print("电脑获胜一次")
        cwin+=1
    if(draw>=2):
        print("最终为平局！")
        break
    elif(nwin>=2):
        print("最终玩家获胜！")
        break
    elif(cwin>=2):
        print("最终电脑获胜！")
        break
    elif(cwin==nwin==draw):
        print("最终平局！")