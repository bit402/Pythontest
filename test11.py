# lst=(['城市','环比','同比'],['北京',120,103],['上海',104,504],['深圳',100,39])
# print(lst)
# for row in lst:
#     for item in row:
#         print(item,end='\t')
#     print()
# lst2=[[j for j in range(5)] for i in range(4)]
# print(lst2)
#s="helloworld"
# print(s[::-1])
# print(s[::2])
# print(s[5:-11:-1])
# t=('hello',[10,20,30],'python','world')
# print(t)
# t=tuple([10,20,30])
# print(t)
# t=tuple("helloworld")
# print(t)
# print("元组长度：",len(t))
# print("元组的最大值：",max(t))
# print("元组的最小值：",min(t))
# print("元组10第一次出现在：",t.index(10))
# print("元组中10一共出现了：",t.count(10))
# print("10在元组中存在吗？",10 in t)
# print("10在元组中不存在吗？",10 not in t)
# print(type(t))
# t=(10)
# print(type(t))
# y=(10,)
# print(type(y))
# # del t
# print(t)
t=('hello','world',"python")
print(t)
print(t[0])
t2=t[0:3:2]
print(t2)
print('-'*50)
for i in t:
    print(i)
for i in range(len(t)):
    print(i,t[i])
for index,item in enumerate(t):
    print(index,item)
for index, item in enumerate(t,start=11):
    print(index, item)

