# from mimesis import Person
#
# t = Person()
# for i in range(1000):
#     with open('D:/31/userdata.csv', 'a') as f:
#         f.write(t.username('l_d') + ',' +
#                 t.password(hashed=True)+',' +
#                 t.email(unique=True)+'\n')
#


import requests
import json
# from mimesis import Person

# 1、根据状态查询宠物-----------------------------------
# headers = {'accept': 'application/json'}  # 可以添加需要的其它头信息
# res = requests.get(url='https://petstore.swagger.io/v2/pet/findByStatus?status=available', headers=headers)
# res = requests.request(method='GET', url='https://petstore.swagger.io/v2/pet/findByStatus?status=available')
# res = requests.get(url='https://petstore.swagger.io/v2/pet/findByStatus',params={'status':'available'})
# res.text:json格式的字符串
# dictres = json.loads(res.text):字符串转换成字典格式
# 根据需要获取字典中需要的任何数据

# 2、添加宠物------------------------------------------
# dataS = '''
# {
#   "id": 0,
#   "category": {
#     "id": 0,
#     "name": "hobby888"
#   },
#   "name": "habagou888",
#   "photoUrls": [
#     "string"
#   ],
#   "tags": [
#     {
#       "id": 0,
#       "name": "pet"
#     }
#   ],
#   "status": "available"
# }
# '''
#
# headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
# # 请求方法一：
# # dataS是json格式的字符串数据
# # res = requests.post(url='https://petstore.swagger.io/v2/pet', data=dataS, headers=headers)
# # print(res.text)
#
# p = Person()
#
# dataD = {
#   "id": 0,
#   "category": {
#     "id": 0,
#     "name": "hobby888"
#   },
#   "name": p.name(),
#   "photoUrls": [
#     "string"
#   ],
#   "tags": [
#     {
#       "id": 0,
#       "name": "pet"
#     }
#   ],
#   "status": "available"
# }
#
# # 请求方法二：
# # dataD是一个字典，但是向服务器端发送的数据是json格式的
# # d = json.dumps(dataD)   # 字典转换成json字符串
# # res = requests.post(url='https://petstore.swagger.io/v2/pet', data=d, headers=headers)
# # print(res.text)
#
# # 请求方法三：
# # dataD是一个字典
# res = requests.post(url='https://petstore.swagger.io/v2/pet', json=dataD, headers=headers)
# print(res.text)
#
# # 3、上传文件
# file = r'D:\courses\locust\locust.png'
# f = {'file': open(file, 'rb')}
# res = requests.post(url='https://petstore.swagger.io/v2/pet/9222968140497203000/uploadImage', files=f)
# print(res.text)
# # f.close()
# # res.close()

# 4、接口之间存在关联关系，接口之间需要共享session信息，例如登录、发帖
# 业务流1：登录--刷新--发帖

# 抓包工具：录制的是基于协议的数据包（Jmeter、fiddler、loadrunner）

import re
import random
from faker import Faker
faker = Faker('zh_CN')

# 左右边界函数
def findall_data(text, lb="", rb=""):
    rule = lb + r"(.+?)" + rb
    datalist = re.findall(rule, text)
    return datalist


session = requests.sessions.session()
headers = {'Content-Type': 'application/x-www-form-urlencoded'}  # 默认头信息，可以省略

data = {'fastloginfield': 'username', 'username': 'huice001',
        'password': 'huice001', 'quickforward': 'yes', 'handlekey': 'ls'}
res = session.post(
    url='http://121.36.91.190/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1',
    data=data, headers=headers)

res = session.get(url='http://121.36.91.190/forum.php')  # 刷新获取服务器端返回的formhash

formash = findall_data(res.text, lb='formhash" value="', rb='"')[0]
print(formash)
uid = findall_data(res.text, lb='uid=', rb='"')[0]
print(uid)
# print(res.text)
#
# data = {
#     'formhash': formash,
#     'posttime': '1614687535',
#     'wysiwyg': '1',
#     'subject': 'pppppppppppppppppppppppppppppppppppppppppppppppppppppppp',
#     'message': 'eeeeeeeeeeeeeeeeeeeee',
#     'replycredit_extcredits': '0',
#     'replycredit_times': '1',
#     'replycredit_membertimes': '1',
#     'replycredit_random': '100',
#     'allownoticeauthor': '1',
#     'usesig': '1',
#     'save': ''
# }
#
# res = session.post(
#     url='http://121.36.91.190/forum.php?mod=post&action=newthread&fid=2&extra=&topicsubmit=yes',
#     data=data, headers=headers)
# print(res.text)


# 业务流2：登录--刷新？--上传附件--发帖
res = session.get(url='http://121.36.91.190/forum.php?mod=post&action=newthread&fid=2')
print(res.text)
hash1 = findall_data(res.text, lb='name="hash" value="', rb='"')[0]

# 遗留问题，附件上传不成功
file = r'E:\789.png'
f = {'Filedata': open(file, 'rb')}
res = session.post(url='http://121.36.91.190/misc.php?mod=swfupload&operation=upload&simple=1',
                   files=f, data={'uid': uid, 'hash': hash1})

print('上传成功附件',res.text)

fileid = findall_data(res.text, lb='DISCUZUPLOAD|0|', rb='|-1|0')[4:7]
# print(fileid)
fileid1 = fileid[0]+fileid[1]+fileid[2]
"""
# print(fileid1)

data = {
    'formhash': formash,
    'posttime': '1614687535',
    'wysiwyg': '1',
    'subject': faker.ssn(),
    'message': faker.company_prefix(),
    'replycredit_extcredits': '0',
    'replycredit_times': '1',
    'replycredit_membertimes': '1',
    'replycredit_random': '100',
    'allownoticeauthor': '1',
    'usesig': '1',
    'save': '',
    f'attachnew[{fileid1}][description]': ''
}

res = session.post(
    url='http://121.36.91.190/forum.php?mod=post&action=newthread&fid=2&extra=&topicsubmit=yes',
    data=data, headers=headers)
print(res.text)

# **************点击全部主题*********************************
res = session.get(url='http://121.36.91.190/forum.php?mod=forumdisplay&fid=2')
tids = findall_data(res.text, lb='tid=', rb='&')  # 获取帖子Tid
id = set(tids) #将列表转换为集合，去重
tid =list(id)   # 将列表转为列表，方便获取列表元素
print('获取到的:',(tid))
a = random.choice(tid)
# print(a)

# ************随机回复帖子***********************
body = {
'message': faker.province() + faker.city_name() + faker.district() + faker.building_number(),
'posttime':'1614741492',
'formhash':formash,
'usesig':'1'
}
res= session.post(url=f'http://121.36.91.190//forum.php?mod=post&action=reply&fid=2&tid={a}&extra=page%3D1&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1',
                  data=body)
print(res.text)

"""
# 常见的post请求发送的数据有两种：1、表单(数据存储方式是字典)；2、自定义数据（json）

# 功能的实现--requests
# 用例编写、用例执行、测试报告的输出---pytest
# 持续集成及自动运行--jenkins

# appium


#
# session = requests.sessions.session()
# headers = {'Accept-Language': 'zh-CN'}
# res = session.get(url='http://192.168.100.100:8888/share/page',headers=headers)
# # print(res.text)
#
# logindata = {'success': '/share/page', 'failure': '/share/page/type/login?error=true', 'username': 'admin', 'password': 'admin'}
# res = session.post(url='http://192.168.100.100:8888/share/page/dologin', data=logindata, headers=headers)
# print(res.text)
#
#
# res = session.get('点击创建html')
# # 解析res.headers中的值，把里面的token值获取到并保存到参数中，例如pp
#
# # 获取pp中的token值，然后对token进行url解码，将解码后的token值存到下面请求的头信息中
# headers={}
# data = {}
# res = session.post('提交创建html',headers=headers,data=data)
