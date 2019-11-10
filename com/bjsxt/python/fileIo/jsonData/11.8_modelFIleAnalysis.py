import json




# 初始化变量
_id = ''
userRealname = ''
userIdcardNo = ''

# 1.将json文件转换成python的数据类型(dict)
jsonFile = open('modelJson3.json', 'r', encoding='utf8')
# jsonObject为dict类型--dict_keys(['applyInfo', 'bbgScoreCardResult', 'bbgReport'])
jsonObject = json.load(jsonFile)

print(jsonObject)
# 申请信息 applyInfo <class 'dict'>
applyInfo = jsonObject['applyInfo']
_id = applyInfo['_id']
userRealname = applyInfo['userRealname']
userIdcardNo = applyInfo['userIdcardNo']
print('%s,%s,%s'%(_id,userRealname,userIdcardNo))

str = ''
# 申请分数 bbgScoreCardResult ,dict_keys(['contentList'])
if 'bbgScoreCardResult' in jsonObject:
    bbgScoreCardResult = jsonObject['bbgScoreCardResult']
    print(bbgScoreCardResult)
    # contentList --<class 'list'>
    contentList = bbgScoreCardResult['contentList']
    for item in contentList:
        # item  <class 'dict'>
        title = item['title']
        value = item['value']

        str = str + '%s:%s,' % (title, value)
        print(title+':'+value+',',end='')
        pass
    print('')
    print(str)
    print("结束")
    pass


# 申请报表 bbgReport <class 'dict'> key:Loan ,CurrAccountInfo
print("=================================================")
bbgReport = jsonObject['bbgReport']
print(bbgReport)
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
        print('---------------------------------------')
        # loan = list(Loan)
        # 判断 Loan是否为 dict类型，如果是则转换成List类型
        if isinstance(Loan, dict):
            print("Loan is dict type!")
            Loan = [Loan]

        # print(type(Loan))
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
                ScheduledPaymentAmount = CurrAccountInfo['ScheduledPaymentAmount']
                Balance = CurrAccountInfo['Balance']
                pass
            print('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s'%(_id, userRealname, userIdcardNo,str,Type, PaymentCyc, GuaranteeType, CreditLimitAmount,
                                            OpenDate, EndDate, PaymentRating, ScheduledPaymentAmount, Balance))
            pass
        pass
    else:
        print('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (
        _id, userRealname, userIdcardNo, str, Type, PaymentCyc, GuaranteeType, CreditLimitAmount,
        OpenDate, EndDate, PaymentRating, ScheduledPaymentAmount, Balance))
else:
    print('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (
    _id, userRealname, userIdcardNo, str, Type, PaymentCyc, GuaranteeType, CreditLimitAmount,
    OpenDate, EndDate, PaymentRating, ScheduledPaymentAmount, Balance))