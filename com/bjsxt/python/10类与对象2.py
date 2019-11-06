'''
类与对象：
    1.私有属性，在Init里面进行设置，self.__name=name 属性前加__可将属性成为私有的
'''
class Person(object):
    def __init__(self,name,age):
        self.__name=name
        self.age=age

    def show(self):
        print(self.__name)
    def setName(self,name):
        self.__name=name

    def getName(self):
        return self.__name
    def __test(self):
        print("private test")
p=Person("abc",100)
p.setName("wangwu")

print(p.getName())