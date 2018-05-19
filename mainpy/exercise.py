
#第一练：1,2.3,4,5组成数字前三位无重复数字的5位数
# for i in range(1,6):
#     for j in range(1,6):
#         for k in range(1,6):
#             for l in range(1,6):
#                 for m in range(1,6):
#                     if( i != k ) and (i != j) and (j != k):
#                         print (i,j,k,l,m)
#

#第二练：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，
# 奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，
# 高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，
# 可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
# i = int(input('当月的利润为:'))
# arr = [1000000,600000,400000,200000,100000,0]
# rat = [0.01,0.015,0.03,0.05,0.075,0.1]
# r = 0
# for idx in range(0,6):
#     if i>arr[idx]:
#         r+=(i-arr[idx])*rat[idx]
#         print ('第',idx,'部分:',(i-arr[idx])*rat[idx])
#         i=arr[idx]
# print ('奖金总数',r)

#第三练：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# 思路：
# 1、则：x + 100 = n2, x + 100 + 168 = m2
# 2、计算等式：m2 - n2 = (m + n)(m - n) = 168
# 3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
# 4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
# 5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
# 6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
# # 7、接下来将 i 的所有数字循环计算即可
# for i in range(1,85):
#     if 168 % i == 0:
#         j = 168 / i;
#         if  i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0 :
#             m = (i + j) / 2
#             n = (i - j) / 2
#             x = n * n - 100
#             print(x)

#第四练：输入某年某月某日，判断这一天是这一年的第几天？
# year = int(input('year:\n'))
# month = int(input('month:\n'))
# day = int(input('day:\n'))
#
# months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
# if 0 < month <= 12:
#     sum = months[month - 1]
# else:
#     print('data error')
# sum += day
# leap = 0
# if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#     leap = 1
# if (leap == 1) and (month > 2):
#     sum += 1
# print ('it is the %dth day.' % sum)
import requests
import itchat
import random

KEY = '04f44290d4cf462aae8ac563ea7aac16'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    robots=['(自动回复)','(自动吐槽)','(按错了)']
    reply = get_response(msg['Text'])+random.choice(robots)
    return reply or defaultReply

itchat.auto_login(enableCmdQR=True)
itchat.run()