# 元组通过()来标识，元组中的数据不可用
tuple=(1,"abcd",True,1.123)
print(tuple)
print(tuple[2])
t=(1,)
print(t)
print(type(t))

list={1,2,3}
# tuple 的引用地址不可改变，被引用地址的值可以改变
t=(123,"abc",["a","b","c"])
print(t)
# 改变引用地址的值
t[2][2]="sxt"

# 改变引用地址,启动报错
# t[2] = list
print(t)
