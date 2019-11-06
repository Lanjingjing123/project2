# age=input("请输入年龄")
# age=int(age)
# if(age<20):
#     print("小孩")
# elif(age<40):
#     print("青年")
# else:
#     print("old")


for i in range(1,10,3):
    print(i)

for i in "abc","def","jks":
    print(i)


# 9*9乘法表
# i=1
# while i<10:
#     j=1
#     while j<=i:
#         print("%d*%d=%d"%(j,i,j*i),end="\t")
#         if(j==i):
#             print()
#         j+=1
#     i+=1
#
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d"%(j,i,i*j),end="\t")
#         if(i==j):
#             print()

str="abcdef"
print(str[2])
print(str[::2])
print(str[4:2:-1])

for letter in "Python":
    print(letter,end="\t")