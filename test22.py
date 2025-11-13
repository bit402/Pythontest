# lis1=[]
# lis2=["面包"]
# lis1.append("火腿肠")
# lis1.append("酸奶")
# lis1.append("辣条")
# print(lis1)
# lis2.append("薯条")
# print(lis2)
# lis=lis1+lis2
# print(lis)
# lis=lis2+lis1
# print(lis)
# lis1.extend(lis2)
# print(lis1)
# count=[]
# flag=True
# while flag:
#     name=input("请输入您要添加的商品名称：")
#     price=float(input("请输入商品的价格："))
#     number=int(input("请输入商品的数量："))
#     goods=[name,price,number]
#     count.append(goods)
#     answer=input("请选择是否继续添加商品？（按Q或q退出）")
#     if answer.lower()=="q":
#         flag=False
# for i in count:
#     print(i)
# lis=["面包","牛奶","牛奶","辣条","薯片","雪糕","糖果","瓜子","牛奶"]
# for i in lis:
#     if i=="牛奶":
#         lis.remove(i)
# print(lis)
# lis=["面包","牛奶","辣条","薯片","雪糕","糖果","瓜子"]
# lis.pop()
# print(lis)
# lis.pop()
# print(lis)
# lis.remove("辣条")
# print(lis)
# if("辣条" in lis):
#     print("存在")
# else:
#     print("不存在")
# lis = ["面包", "牛奶", "牛奶", "辣条", "薯片", "雪糕", "糖果", "瓜子", "牛奶"]
# print("初始列表:", lis)
#
# for i in list(lis):  # 用副本遍历，避免索引混乱
#     if i == "牛奶":
#         lis.remove(i)
#         print(f"删除了'{i}'，当前列表: {lis}")
#     else:
#         print(f"当前元素'{i}'，列表不变: {lis}")
lis = ["面包", "牛奶", "牛奶", "辣条", "薯片", "雪糕", "糖果", "瓜子", "牛奶"]
print("初始列表:", lis)
for li in lis:
    print("当前元素为："+li)
    if li=="牛奶":
        lis.remove(li)
        print("删除了"+li+",当前列表：",lis)
    else:
        print("列表不变，当前列表为：",lis)