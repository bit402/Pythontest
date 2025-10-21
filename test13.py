import random
# username="世龙"
# account=0
# coupon=0
# total=float(input("请输入购买总金额："))
# if 0<total<500:
#     coupon+=random.randint(1,10)+random.randint(1,10)+random.randint(1,10)
# elif 500<total<2000:
#     coupon=50*2
#     print("请问您还需要充值吗？lv2充值送充值金额的%10")
#     flag=input("充值请输入：“Y”，不充值请输入：“N”")
#     match flag:
#         case "Y":
#             account=float(input("请输入您要充值的金额数："))
#             account+=account*0.1
#             print("您的总金额为："+str(account))
#         case "N":
#             pass
#         case _:
#             print("输入不合法，请重新输入Y或者N")
# elif total>2000:
#     coupon=200
#     print("请问您还需要充值吗？lv3充值送充值金额的%15")
#     flag = input("充值请输入：“Y”，不充值请输入：“N”")
#     match flag:
#         case "Y":
#             account=float(input("请输入您要充值的金额数："))
#             account+=account*0.15
#             print("您的总金额为"+str(account))
#         case "N":
#             pass
#         case _:
#             print("输入不合法，请重新输入Y或者N")
# username=input("请输入用户名：")
# password=input("请输入密码：")
# is_remember=True
# if username == "admin" and password == "1234":
#     if is_remember:
#         print("已经记住用户名admin的密码了")
#     else:
#         print("没记住密码，下次继续输入")
# else:
#     print("用户名或者密码有误！")
unitPrice=float(input("请输入商品的单价："))
quantity=int(input("请输入要购买的商品数量"))
totalAmount=unitPrice*quantity
print("您总共需要支付"+str(totalAmount)+"元，我们为您提供了四种付款方式，不同的付款方式有不同的折扣")
print("1.现金支付（没有折扣）")
print("2.微信（0.95折）")
print("3.支付宝（鼓励金付款金额的10%，且鼓励金可以直接折算到付款金额中）")
print("4.刷卡（满100-20）")
choice=int(input('请选择你的付款方式：'))
if choice==1:
    print("现金支付...")
    print("应付金额为："+str(totalAmount)+"元")
elif choice==2:
    print("微信支付...")
    print("应付金额为："+str(totalAmount*0.95)+"元")
elif choice==3:
    print("支付宝支付...")
    print("鼓励金为"+str(totalAmount*0.1)+"元")
    print("应付金额为"+str(totalAmount-totalAmount*0.1)+"元")
elif choice==4:
    print("刷卡支付...")
    if(totalAmount>100):
        print("应付金额为：" + str(totalAmount-20)+"元")
    else:
        print("应付金额为：" + str(totalAmount)+"元")
