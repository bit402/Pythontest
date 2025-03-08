# for i in range(1,5):
#     for j in range(4-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()
# for i in range(1,4):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(7-(2*i)):
#         print("*",end="")
#     print()
# a=eval(input("请输入菱形行数："))
# b=(a+1)//2
# for i in range(1,b+1):
#     for j in range(b-i):
#         print(" ",end="")
#     if(i==1):
#         print("*",end="")
#     else:
#         print("*",end="")
#         for k in range(2*(i-1)-1):
#             print(" ",end="")
#         print("*",end="")
#     print()
# for i in range(1,b):
#     for j in range(i):
#         print(" ",end="")
#     if(i==b-1):
#         print("*",end="")
#     else:
#         print("*",end="")
#         for k in range(1,a-(2*i+1)):
#             print(" ",end="")
#         print("*",end="")
#     print()

s=0
i=1
while i<11:
    s+=i
    if(s>20):
        print("累加和大于20的当前数是：",i)
        break
    i+=1
print(i)
print(s)