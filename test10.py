import random
#s="Hello World"
#print("e在s中存在吗？",("e" in s))
#print("v在s中存在吗？",("v" in s))
#print("e在s不中存在吗？",("e" not in s))
#print("v在s中不存在吗？",("v" not in s))
# lst=["hello","world",98,100.5]
# print(lst)
# lst2=list("helloworld")
# print(lst2)
# lst3=list(range(1,10,2))
# print(lst3)
# print(lst+lst2+lst3)
# print(type(lst3),type(lst3[0]))
# print(len(lst3),len(lst))
# print(lst*5)
# print(max(lst3))
# print(min(lst3))
# lst4=[10,20,30]
# print(lst4)
# del lst4[0]
# print(lst4)
# del lst4
# #print(lst4)
# print(lst2.index('o'))
# print(lst2.count('o'))
# lst=["hello","world","python"]
# print(lst)
# for i in lst:
#     print(i)
# for i in range(0,len(lst)):
#     print(i,"-->",lst[i])
# for index,item in enumerate(lst):
#     print(index,"-->",item)
# for index,item in enumerate(lst,start=1):
#     print(index,"-->",item)
# for index,item in enumerate(lst,1):
#     print(index,"-->",item)
# lst=["hello","world","python"]
# print("原列表为：", lst, id(lst) )
# lst2=lst.append("sql")
# print("增加一个元素之后的列表为：",lst,id(lst))
# print(lst is lst2)
# print(id(lst2))
# lst.insert(1,100)
# print(lst)
# lst.remove("world")
# print("删除之后的列表是：",lst,id(lst))
# print(lst.pop(1))
# print(lst)
# # lst.clear()
# # print(lst, id(lst))
# lst.reverse()
# print(lst)
# new_lst=lst.copy()
# print(new_lst,id(new_lst))
# print(lst,id(lst))
# lst[1]="mysql"
# print(lst)
# lst=[4,56,3,78,40,58,89,56]
# print("原序列：",lst)
# lst.sort();
# print("升序：",lst)
# lst.sort(reverse=True)
# print("降序:",lst)
# lst=["banana","apple","Cat","Orange"]
# print(lst)
# lst.sort()
# print("升序（先排大写，后排小写）:",lst)
# lst.sort(reverse=True)
# print("降序（先排小写，后排大写）：",lst)
# lst.sort(key=str.lower)
# print(lst)
# lst=[4,56,78,89,40,3,56]
# print("原列表：",lst)
# arc_lst=sorted(lst)
# print("升序排列：",arc_lst)
# desc_lst=sorted(lst,reverse=True)
# print('降序：：',desc_lst)
# print("原序列：",lst)
# lst=["banana","apple","Cat","Orange"]
# print("原列表：",lst)
# new_lst=sorted(lst,key=str.lower)
# print("忽略大小写升序排列：",new_lst)
lst=[item for item in range(1,11)]
print(lst)
print(type(lst))
print(len(lst))
lst=[item*item for item in range(1,11)]
print(lst)
lst=[random.randint(1,100) for item in range(1,11)]
print(lst)
lst=[i for i in range(10) if i%2==0]
print(lst)