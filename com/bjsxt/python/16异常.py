try:
    print ("test1")
    f = open("123.txt","r")
    print("test2")
except FileNotFoundError as msg:
    print("发生异常了")
    print(msg)
finally:
    # f.close()
    print("finally")
print("go on")
# else:
#     print("异常处理完了")