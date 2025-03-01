# answer=input("请问您喝酒了吗？请回答y或n：")
# if answer=="y":
#     proof=eval(input("请输入酒精含量："))
#     if proof<20:
#         print("未构成酒驾，祝您一路平安！")
#     elif proof<80:
#         print("构成酒驾，不能开车！")
#     else:
#         print("已达到了醉驾的标准，千万不要开车！")
# else:
#     print("继续通行！")
# user_name=input("请输入您的用户名：")
# pwd=input("请输入您的密码：")
# if user_name=="ysj" and pwd=="88888888":
#     print("登陆成功！")
# else:
#     print("用户名或密码错误！")
# score=eval(input("请输入您的成绩："))
# if score>100 or score<0:
#     print("成绩无效！")
# else:
#     print("您的成绩为：",score)
# grade=input("请输入您的成绩等级：")
# match grade:
#     case "A":
#         print("优秀！")
#     case "B":
#         print("良好！")
#     case "C":
#         print("中等！")
#     case "D":
#         print("及格")
#     case "E":
#         print("不及格！")
# for i in "helloworld":
#     print(i)
# for i in range(1,11):
#     #print(i)
#     if i%2==0:
#         print(i,"是偶数")
# s=0
# for i in range(1,11):
#     s+=i
# print("1-10之间的累加和为：",s)
# for i in range(100,1000):
#     if((i%10)**3+(i//10%10)**3+(i//100%10)**3==i):
#         print(i,"为水仙花数!")
# s=0
# for i in range(1,11):
#     s+=i
# else:
#     print("1-10之间的整数和为：",s)
# answer=input("今天要上课吗？y/n:")
# while(answer=="y"):
#     print("好好学习天天向上")
#     answer=input("今天要上课吗？y/n:")
# sum=0
# i=1
# while(i<=100):
#     sum+=i
#     i+=1
# print("1-100的数累加和为：",sum)
# sum=0
# i=1
# while(i<=100):
#     sum+=i
#     i+=1
# else:
#     print("1-100的数累加和为：",sum)
# i=0
# while(i<3):
#     user = input("请输入您的用户名：")
#     pwd = input("请输入您的密码：")
#     if(user=="ysj" and pwd=="88888888"):
#         print("登陆成功，请稍后......")
#         break
#     else:
#         print("用户名或密码错误。您还有",2-i,"次机会")
#         i+=1
# if(i==3):
#     print("对不起三次均输入错误，账户已冻结！")
# i=0
# while(i<3):
#     j=0
#     while(j<4):
#         print('*',end="")
#         j+=1
#     print()
#     i+=1
# print("------------方法2-----------------")
# for i in range(1,4):
#     for j in range(1,5):
#         print('*',end="")
#     print()
# for i in range(1,6):
#     j=0
#     while(j<i):
#         print('*',end="")
#         j=j+1
#     print("")
# print("------------方法2-----------------")
# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end="")
#     print("")
# for i in range(1,6):
#     for j in range(1,7-i):
#         print("*",end="")
#     print()
for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end="")
    for k in range(2 * i -1):
        print('*', end="")
    print()