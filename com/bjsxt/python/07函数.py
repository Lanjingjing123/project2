'''
函数由三部分组成
    函数名称
    函数体
    函数参数列表
    返回值
1.函数的定义必须要以def开头
2.函数名称+(参数列表)调用
3. python的函数没有重载,重名的函数会覆盖


'''
# def add():
#     print("add")
#
# add()

# 带参数的函数
# def add(a,b):
#     print(a+b)
#
# add(1,2)
# add()
list=[5,2,4,3,1]
list.sort(reverse=True)
print(list)


def add(a=100,b=200):
    print(a)
    print(b)
    print(a+b)

add(b=1,a=2)

# 不定长参数
'''
*args: 表示一组值的集合，普通数据
**kwargs:表示k-v格式的数据

'''
# def fun(a,b,*args,**kwargs):
#     print("a=",a)
#     print("b=",b)
#     print("*args=",args)
#     print("**kwargs=",kwargs)
#     for k,v in kwargs.items():
#         print(k,v)
#
# fun(1,2,3,4,5,6,7,8,9,10,x=1,y=2,z=3)
#
# # 引用传参——可变类型与不可变类型的区别
# b=[1,2]
# a=1
#
# def fun(a):
#     a+=a
#     print("fun内",a)
#
# print("b=======")
# # 可变参数的引用传参
# fun(b)
# print(b)
#
# # 不可变函数的引用传参
# print("a==========")
# fun(a)
# print(a)
#
#
# # python可以返回多个值
# def fun(a,b):
#     return a+b,a-b,a*b,a/b
# a,b,c,d=fun(100,200)
# print(a)
# print(b)
# print(c)
# print(d)


# 全局变量和局部变量,方法中不可以改变全局变量的值
# 不能在global前定义同名的局部变量
count = 100
def fun():
    global count
    count=200
    print(count)
    print(count)

fun()



'''
    斐波那契数列
    1,1,2,3,5,8,13,21,34
'''
# def getNum(a):
#     if(a<=2):
#         return 1;
#     else:
#         return getNum(a-1)+getNum(a-2);
# # print(getNum(10))
#
# for i in range(1,11):
#     print(getNum(i),end="\t")

'''
    匿名函数
'''
# sum = lambda a,b:a+b
# print(type(sum))
# print(sum(1,2))


def fun(a,b,opt):
    print(a)
    print(b)
    print(opt(a,b))

fun(1,2,lambda a,b:a+b)
fun(1,2,lambda a,b:a*b)


stus=[{"name":"zhangsan","age":19},{"name":"lisi","age":20},{"name":"wangwu","age":"17"}]
print(stus[0]["name"])
# 语义：进来一个student对象，如上面的stus[0],对这个对象的name进行排序
stus.sort(key=lambda x:x["name"])
print(stus)