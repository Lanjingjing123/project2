import re
# 读取文件
file = open('11.8_resultFile.json', 'r+', encoding='utf8')

lines = file.readlines()
resultFile = open('11.8resultFile_deal.json', 'w', encoding='utf8')
# print(lines)
for line in lines:
    # print(line, end='')
    findStr = re.search('^('')[}][,]$', line, re.M | re.I)
    if findStr:
        print(findStr.group(0))
        line = line.replace('},', '};')
        print('replace str = %s'%(line))
    resultFile.write(line)
resultFile.close()