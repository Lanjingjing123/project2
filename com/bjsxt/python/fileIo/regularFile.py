import re
import random
print('hello world')

def intTOstr(a):
    return str(a)

def getName():
    # 姓
    arr = ['赵', '王', '孙', '李', '郭', '农', '徐', '陈', '秦', '张', '钱', '高', '江', '刘', '孔']
    randomNum = random.randint(0, arr.__len__() - 1)
    firstName = arr[randomNum]
    return firstName

def rePlaceStr( line ):
    print('input str is :' + line)
    if line.__contains__('_id'):
        str = re.search(r'("_id" : ")(\d+)(",)', line, re.M | re.I)
        id = str.group(2)
        randNum = random.randint(0, 1000000)
        line = line.replace(id, intTOstr(randNum))
        print('result str is :'+line)
        return line
    if line.__contains__('userRealname'):
        str = re.search(r'("userRealname" : ")(.*)(",)', line, re.M | re.I)
        userRealname = str.group(2)

        line = line.replace(userRealname, getName())
        print('result str is :' + line)
        return line
    if line.__contains__('userIdcardNo'):
        str = re.search(r'("userIdcardNo" : ")(\d+X|\d+)(")', line, re.M | re.I)
        userIdcardNo = str.group(2)
        randNum = random.randint(0, 1000000)
        line = line.replace(userIdcardNo,intTOstr(randNum))
        print('result str is :' + line)
        return line

str1 = '"userIdcardNo" : "26X"'

str1 = rePlaceStr(str1)
print(str1)



resultStr = ''


resultFile = open('./resultFile.json', 'w', encoding='utf8')
with open('test.json', 'r',encoding='utf8') as lines:
    for line in lines:
        tempStr = line
        if line.__contains__('_id'):
            tempStr = rePlaceStr(line)

        if line.__contains__('userRealname'):
            tempStr = rePlaceStr(line)
        if line.__contains__('userIdcardNo'):
            tempStr = rePlaceStr(line)
        resultStr = resultStr + tempStr
        # resultFile.write(resultStr)
        pass

    # 打印输出结果
    print(resultStr)

    resultFile.writelines(resultStr)
    resultFile.close()









