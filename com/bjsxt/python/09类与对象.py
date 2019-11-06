'''
类与对象
    1._init_完成对象的初始化操作，在对象被创建完成之后，立即被调用执行，隐式调用，创建对象时的参数
    2._new_是构造方法，创建对象的时候，首先调用的是new方法，new方法必须有返回值，参数必须跟创建对象传递的参数一致
    3. 无论什么情况，init和new方法的参数必须保持一致
'''
class Person(object):
    def __init__(self,name="wangwu",age=14):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
        print("*******************")

    def __new__(cls, name, age):
        # cls.name = name
        # cls.age = age
        # print(cls.name)
        # print(cls.age)
        print("========")
        return object.__new__(cls)

    # 对象的toString方法
    def __str__(self):
        return "hhahh"
    def __del__(self):
        print("del...")
    def getName(self):
        return self.name
    def run(self):
        print("person is running")

# p=Person("zhangsan",12)
p1=Person("wangwu",13)
print(".....")
print(p1.getName())
p2=p1
p3=p1

# 删除对象的引用，只有该对象的引用计数为0 才会执行对象的del方法删除对象
# 如下 p1,p2,p3对person这个对象具有引用，只有最后一行del p1时，才会执行对象里面的del方法
del p2
print(p3)
del p3
print(p1)
del p1
# print(p1)
# p1.run()
# p.name="zhangsan"
# p.age="12"
# print(p.name)
# print(p.age)

# p2=Person("lisi",13)
# # p2.name="lisi"
# # p2.sex="male"
# print(p2.name)
# print(p2.sex)

