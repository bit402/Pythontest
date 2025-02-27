# name="张三"
# age=18
# a=b=c=d=100
# print(name,age,a,b,c,d)
# a,b,c,d=100,200,300,400
# print(a,b,c,d)
# a,b,c,d="room"
# print(a,b,c,d)
# print("-----输入/输出语句也是典型的顺序结构------")
# name=input("请输入您的名字：")
# age=eval(input("请输入您的年龄："))
# luck_number=eval(input("请输入您的幸运数字："))
# print("姓名：",name)
# print("年龄：",age)
# print("幸运数字：",luck_number)
# number=eval(input("请输入6位中奖号码："))
# if number==987654:
#     print("恭喜您中奖了！")
# if number != 987654:
#     print("您未中本期大奖")
# print("----以上if判断的表达式，是通过比较运算符计算出来的结果是布尔类型")
# n=98
# if(n%2):
#     print(n,"是奇数。")
# if(not n%2):
#     print(n,"为偶数")
# if(n%2==0):
#     print(n, "为偶数")
# print("-----判断一个字符串是否为空字符串：------")
# x=input("请输入一个字符串：")
# if x:
#     print("x不是空字符串。")
# if not x:
#     print("x是一个空字符串。")
# print("-----表达式也可以是一个单纯的布尔型变量-----")
# flag=eval(input("请输入一个布尔型变量True或False："))
# if flag:
#     print("flage的值为：True")
# if not flag:
#     print("flag的值为：False")
# print("----使用if语句时，如果语句块中只有一句代码，可以将语句块直接写在冒号的后面-----")
# a=10
# b=5
# if a>b:max=a
# print("a和b的最大值为：",max)
number=eval(input("请输入您的6位中奖号码："))
if number==987654:
    print("恭喜您中奖了！")
else:
    print("您未中本期大奖。")
result="恭喜您中奖了！"if number==987654 else"您未中大奖"
print(result)
print("恭喜您中奖了！"if number==987654 else"您未中大奖")