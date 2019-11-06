# 读取文件的内容
# f = open("E://python_project//project2//data//test.txt")
# content=f.read()
# content=f.readline()
# print(content)
# content=f.readline()
# print(content)
# # f.write("\n123")
# f.close()


# 获取文件读取位置
f = open("E://python_project//project2//data//test.txt","a")

# content = f.readline()
# print(content)
# print(f.tell())
# f.seek(1,1)
# content = f.readline()
# print(content)
# f.close()
#
# import os
# print(os.name)
# print(os.listdir())

f.write("this is new line!")
f.close()
# str=input("q请输入一行：")
# print("你输入的内容是：",str)


