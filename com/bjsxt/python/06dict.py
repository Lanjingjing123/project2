# 字典通过{}来标识，字典中的数据可变，字典中的key不可以重复，如果有重复，覆盖之前的
# value 可以重复
# set:没有值的dict
'''
    可变类型和不可变类型
    可变：
        list
        set(没有value的字典)
        dict
    不可变：
        元组
        数值类型：int ,long,bool,float
        字符串
'''


dict={"a":100,"b":200,"c":300}
print(type(dict))
print(dict.__len__())

print(dict.keys())
print(dict.values())

for i in dict.keys():
    print(i, dict[i])

# for v in dict.values():
#     print(v)
#
# for i,v in dict.items():
#     print()
# print(dict)
# print(dict["a"])
# print(dict.get("b"))
# dict["d"]=400
# dict["a"]=None
# print(dict)


# set 可变


dict={1,2,3,4}
print(type(dict))
d1=set([1,2,3,4])
d1.add(5);
print(d1)
# 删除元素
# del d1
d1.clear()
print(d1)


