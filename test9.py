# i=0
# while i<3:
#     name=input("请输入您的用户名：")
#     pwd=input("请输入您的密码：")
#     if(name=="ysj" and pwd=="88888888"):
#         print("登陆成功，请稍后...")
#         break
#     elif i<2:
#         print("用户名或密码错误，您还有",2-i,"次机会")
#     i+=1
# else:
#     print("三次机会均错误，账户已冻结！！！")
# i="hello"
# for i in "hello":
#     if i=="e":
#         break
#     print(i)
# for i in range(3):
#     name=input("请输入您的用户名：")
#     pwd=input("请输入您的密码：")
#     if(name=="ysj" and pwd=="88888888"):
#         print("登陆成功，请稍后...")
#         break
#     elif(i<2):
#         print("用户名或密码错误，您还有",2-i,"次机会")
# else:
#     print("三次机会均错误，您的账户已冻结！！！")
# s=0
# i=1
# while i<=100:
#     if i%2==1:
#         i+=1
#         continue
#     else:
#         s+=i
#         i+=1
# print(s)
# s=0
# for i in range(1,101):
#     if(i%2==1):
#         continue
#     else:
#         s+=i
# print("1-100之间的偶数和为：",s)
# if True:
#     pass
# while True:
#     pass
# for i in range(10):
#     pass
# year=eval(input("请输入年份："))
# if(year%4==0 and year%100!=0 or year%400==0):
#     print(year,"是闰年")
# else:
#     print(year,"是平年")
# answer="y"
# while answer=="y":
#     print('-'*10,"欢迎使用10086查询功能",'-'*10)
#     print("1.查询当前余额")
#     print("2.查询当前剩余流量,单位GB")
#     print("3.查询当前剩余通话时长")
#     print("0.退出系统")
#     choice=input("请输入您的选择：")
#     if choice=='1':
#         print("当前余额剩余888元")
#     elif choice=='2':
#         print("当前流量还有888G")
#     elif choice=='3':
#         print("当前剩余通话时长还有：888分钟")
#     elif choice=='0':
#         break
#     else:
#         print("对不起，您的输入有误，请重新操作：")
#         answer=input("还继续操作吗？y/n:")
# else:
#     print("程序退出感谢您的使用。")
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,'*',i ,'=',i*j,end=" "*5)
#     print()
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(str(j)+'*'+str(i)+'='+str(j*i),end="\t")
#     print()
import random
count=1
rand=random.randint(1,100)
num=0
while num!=rand:
    if count>10:
        print("很遗憾您十次均没有猜对，挑战失败。")
        break
    else:
        num = eval(input("在我心中有个数请你猜一猜："))
    if num>rand:
        print("猜的偏大。")
    elif num<rand:
        print("猜的偏小")
    elif num==rand:
        print("恭喜你，猜对了！！！")
        print("您一共猜了",count,"次")
        break
    count+=1