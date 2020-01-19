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
    if line.__contains__('"_id" : ObjectId'):
        print('result str is :'+line)
        return line
    if line.__contains__('_id'):
        str = re.search(r'("_id" : ")(.*)(",)', line, re.M | re.I)
        id = str.group(2)
        randNum = random.randint(0, 1000000)
        line = line.replace(id, intTOstr(randNum))
        print('result str is :'+line)
        return line
    if line.__contains__('userRealname'):
        print(">>>>>>>>>>>"+line)
        str = re.search(r'("userRealname" : ")(.*)(")', line, re.M | re.I)
        print(str)
        userRealname = str.group(2)

        line = line.replace(userRealname, getName())
        print('result str is :' + line)
        return line
    if line.__contains__('userIdcardNo'):
        str = re.search(r'("userIdcardNo": "|"userIdcardNo" : ")(\d+X|\d+)(")', line, re.M | re.I)
        userIdcardNo = str.group(2)
        randNum = random.randint(0, 1000000)
        line = line.replace(userIdcardNo,intTOstr(randNum))
        print('result str is :' + line)
        return line
    if line.__contains__('Name'):
        str = re.search('("Name" : )(.*)(")', line, re.M | re.I)
        Name = str.group(2)
        line = line.replace(Name, "未知")
        print('result str is :' + line)
    if line.__contains__('TelephoneNo'):
        str = re.search('("TelephoneNo" : )(.*)(")', line, re.M | re.I)
        TelephoneNo = str.group(2)
        line = line.replace(TelephoneNo, "12345678901")
        print('result str is :' + line)
    if line.__contains__('Certno'):
        str = re.search('("Certno" : )(.*)(")', line, re.M | re.I)
        Certno = str.group(2)
        line = line.replace(Certno, "12345678901")
        print('result str is :' + line)
    if line.__contains__('Certtype'):
        str = re.search('("Certtype" : )(.*)(")', line, re.M | re.I)
        Certtype = str.group(2)
        line = line.replace(Certtype, "未知")
        print('result str is :' + line)
    if line.__contains__('Employer'):
        str = re.search('("Employer" : )(.*)(")', line, re.M | re.I)
        Employer = str.group(2)
        line = line.replace(Employer, "未知")
        print('result str is :' + line)
str1 = '"userIdcardNo" : "26X"'

# str1 = rePlaceStr(str1)
# print(str1)



resultStr = ''


resultFile = open('./resultFile.json', 'w', encoding='utf8')
with open('test.txt', 'r', encoding='utf8') as lines:
    for line in lines:
        tempStr = line
        if line.__contains__('_id'):
            tempStr = rePlaceStr(line)

        if line.__contains__('userRealname'):
            tempStr = rePlaceStr(line)
        if line.__contains__('userIdcardNo'):
            print(line)
            tempStr = rePlaceStr(line)
        resultStr = resultStr + tempStr
        # resultFile.write(resultStr)
        pass

    # 打印输出结果
    print(resultStr)

    resultFile.writelines(resultStr)
    resultFile.close()









