import random
# d={'hello':10,'world':20,'python':30}
# print(d['hello'])
# print(d.get('hello'))
# #print(d['java'])#报错
# print(d.get('java'))
# print(d.get('java','不存在'))
# for item in d.items():
#     print(item)
# for key,value in d.items():
#     print(key,value)
# d={1001:'李梅',1002:'王华',1003:'张锋'}
# print(d)
# d[1004]='张丽丽'
# print(d)
# k=d.keys()
# print(k)
# print(list(k))
# print(tuple(k))
# va=d.values()
# print(va)
# print(list(va))
# print(tuple(va))
# print(d.items())
# lst=list(d.items())
# print(lst)
# tp=tuple(d.items())
# print(tp)
# d=dict(tp)
# print(d)
# print(dict(lst))
# print(d.pop(1001))
# print(d)
# print(d.pop(1008,'不存在'))
# print(d.popitem())
# print(d)
# d.clear()
# print(d)
# print(bool(d))
d={item:random.randint(1,100) for item in range(3)}
print(d)
lst=[1001,1002,1003]
lst2=['陈美美','王一一','李莉莉']
d={key:value for key,value in zip(lst,lst2)}
print(d)