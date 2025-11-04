import random
# fileName=""
# s="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789"
# for i in range(4):
#     index=random.randint(0,len(s)-1)
#     fileName+=s[index]
# print(fileName)
#
# name=input("请输入要上传的文件名，需要把后缀名也写上(目前只支持jpg,jif,png)并且文件名要大于6位以上：")
# if (not(name.endswith("jpg"))) and (not(name.endswith("jif"))) and (not(name.endswith("png"))):
#     print("上传失败")
# elif len(name)>=6 and (name.endswith("jpg") or name.endswith("jif") or name.endswith("png")):
#     print("上传成功")
#     print("文件名为"+name)
# elif len(name)<6 and (name.endswith("jpg") or name.endswith("jif") or name.endswith("png")):
#     str1=str(random.randint(0,9))
#     str2=str(random.randint(0,9))
#     str3=str(random.randint(0,9))
#     str4=str(random.randint(0,9))
#     str5=str(random.randint(0,9))
#     str6=str(random.randint(0,9))
#     st=str1+str2+str3+str4+str5+str6
#     # r=name[-1:-5:-1]
#     # r=r[::-1]
#     r=name[-4:]
#     # name=st+r
#     name=fileName+r
#     print("打印成功文件名为："+name)
# s="nihao1230"
# print(s.isalpha())
# s2="nihao"
# print(s2.isalpha())
# s="123456789"
# print(s.isdigit())
# s="123456789nihao"
# print(s.isdigit())
# s="A12306"
# print(s.isalnum())
# s="A#12306"
# print(s.isalnum())
# s="   "
# print(s.isspace())
# s=""
# print(s.isspace())
# s=" ABC "
# print(s.isspace())
# s="HELLO"
# print(s.isupper())
# s="HELLo"
# print(s.isupper())
# s="hello"
# print(s.islower())
# s="Hello"
# print(s.islower())