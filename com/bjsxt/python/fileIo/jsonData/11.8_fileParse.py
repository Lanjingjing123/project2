import json




# 初始化变量
_id = ''
userRealname = ''
userIdcardNo = ''
# 输出文件
theEndFile = open('11.8_TheEndFile.txt', 'w', encoding='utf8')


# 1.读取文件
file = open('11.8resultFile_deal.json', 'r', encoding='utf8')
lines = file.readlines()
strALl = ''
for line in lines:
    # print(line,end='')
    strALl += line

jsonArr = strALl.split(";")
# print(jsonArr[0])
# print(jsonArr[1])

# 处理条数
i = 0
# 结果行
resultLine = ''



for sigleJson in jsonArr:
    i += 1
    # 2.jsonObject为dict类型--dict_keys(['applyInfo', 'bbgScoreCardResult', 'bbgReport'])
    jsonObject = json.loads(sigleJson)
    print(i)
    print(jsonObject)
    # 申请信息 applyInfo <class 'dict'>
    applyInfo = jsonObject['applyInfo']
    _id = applyInfo['_id']
    userRealname = applyInfo['userRealname']
    userIdcardNo = applyInfo['userIdcardNo']
    # print('%s,%s,%s'%(_id, userRealname, userIdcardNo))

    str = ''
    # 申请分数 bbgScoreCardResult ,dict_keys(['contentList'])
    if 'bbgScoreCardResult' in jsonObject:
        bbgScoreCardResult = jsonObject['bbgScoreCardResult']
        # contentList --<class 'list'>
        contentList = bbgScoreCardResult['contentList']
        for item in contentList:
            # item  <class 'dict'>
            title = item['title']
            value = item['value']

            str = str + '%s:%s,' % (title, value)
            pass

        pass

    # 申请报表 bbgReport <class 'dict'> key:Loan ,CurrAccountInfo
    print("=================================================")
    bbgReport = jsonObject['bbgReport']
    # CreditDetail,dict_keys(['Loan'])

    # 初始化字段
    Type = ''
    PaymentCyc = ''
    GuaranteeType = ''
    CreditLimitAmount = ''
    OpenDate = ''
    EndDate = ''
    PaymentRating = ''
    ScheduledPaymentAmount = ''
    Balance = ''

    # bbgReport有元素
    if bbgReport.__len__() > 0:
        Loan = []
        Header = {}
        CreditDetail = {}
        if 'CreditDetail' in bbgReport:
            CreditDetail = bbgReport['CreditDetail']
            pass
        else:
            print('Exception: CreditDetail is not a existed node!')

        if 'Header' in bbgReport:
            Header = bbgReport['Header']

        if 'Loan' in CreditDetail:
            Loan = CreditDetail['Loan']
            # 如果Loan是dict类型 则把他封装成list
            if isinstance(Loan, dict):
                print("Loan is dict type!")
                Loan = [Loan]
    # print(type('Loan'))
            for item in Loan:
                Type = ''
                PaymentCyc = ''
                GuaranteeType = ''
                CreditLimitAmount = ''
                OpenDate = ''
                EndDate = ''
                PaymentRating = ''
                ScheduledPaymentAmount = ''
                Balance = ''

                # item dict_keys(['ContractInfo', 'CurrAccountInfo'])
                # print(type(item))
                # print(item.keys())
                ContractInfo = item['ContractInfo']
                if 'ContractInfo' in item:
                    ContractInfo = item['ContractInfo']

                    Type = ContractInfo['Type']
                    if ('PaymentCyc' in ContractInfo):
                        PaymentCyc = ContractInfo["PaymentCyc"]
                    GuaranteeType = ContractInfo['GuaranteeType']
                    CreditLimitAmount = ContractInfo['CreditLimitAmount']
                    OpenDate = ContractInfo['OpenDate']
                    EndDate = ContractInfo['EndDate']
                    PaymentRating = ContractInfo['PaymentRating']
                    pass
                if 'CurrAccountInfo' in item:
                    CurrAccountInfo = item['CurrAccountInfo']
                    if 'ScheduledPaymentAmount' in CurrAccountInfo:
                        ScheduledPaymentAmount = CurrAccountInfo['ScheduledPaymentAmount']

                    if 'Balance' in CurrAccountInfo:
                        Balance = CurrAccountInfo['Balance']
                    pass
                resultLine = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n'%(_id, userRealname, userIdcardNo,str,Type, PaymentCyc, GuaranteeType, CreditLimitAmount,
                                                OpenDate, EndDate, PaymentRating, ScheduledPaymentAmount, Balance)
                # 文件写入
                theEndFile.write(resultLine)
                print(resultLine,end='')
                pass
            pass
        else:
            # 无 Loan
            resultLine = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (
            _id, userRealname, userIdcardNo, str, Type, PaymentCyc, GuaranteeType, CreditLimitAmount,
            OpenDate, EndDate, PaymentRating, ScheduledPaymentAmount, Balance)
            # 文件写入
            theEndFile.write(resultLine)
            print(resultLine,end='')
    else:
        # 无 bbgReport
        resultLine = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (
        _id, userRealname, userIdcardNo, str, Type, PaymentCyc, GuaranteeType, CreditLimitAmount,
        OpenDate, EndDate, PaymentRating, ScheduledPaymentAmount, Balance)
        # 文件写入
        theEndFile.write(resultLine)
        print(resultLine,end='')