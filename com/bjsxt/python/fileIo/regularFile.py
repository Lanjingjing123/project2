import re
print('hello world')


str = ''
with open('test.json', 'r',encoding='utf8') as lines:
    for line in lines:
        if line.__contains__('_id'):
            print(line)

        pass


line = '		"_id" : "61",'

str = re.search(r'("_id" : ")(\d+)(",)', line, re.M|re.I)
print(str.group(0))
print(str.group(1))
print(str.group(2))
print(str.group(3))

