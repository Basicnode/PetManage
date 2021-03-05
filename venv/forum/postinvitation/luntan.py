from forum.common.urlmanager.baseurl import headers,Baseurl
from forum.common.boundfunction.bdf import findall_data
import requests
import random
from faker import Faker
faker = Faker('zh_CN')

# ********业务流：登录--刷新--上传附件--发帖--随机回复帖子********
class Dussiz:
    def __init__(self):
        self.uid = None
        self.fileid1 = None
        self.formash = None
        self.session = requests.sessions.session()

#  *********************登录论坛************************
    def DengLu(self):
        data = {'fastloginfield': 'username', 'username': 'admin123',
                'password': '123456', 'quickforward': 'yes', 'handlekey': 'ls'}
        res = self.session.post(
            url=Baseurl + '/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1',
            data=data, headers=headers)

#  **********************刷新页面获取hash****************
    def Refresh_Page(self):
        res = self.session.get(url=Baseurl +'/forum.php')  # 刷新获取服务器端返回的formhash

        formash = findall_data(res.text, lb='formhash" value="', rb='"')[0]
        print(formash)
        self.formash = formash
        uid = findall_data(res.text, lb='uid=', rb='"')[0]
        self.uid = uid
        # print('uid是:',uid)

# ***********************（发新帖）上传附件****************
    def Upload_file(self):
        res = self.session.get(url= Baseurl +'/forum.php?mod=post&action=newthread&fid=2')
        # print(res.text)
        hash1 = findall_data(res.text, lb='name="hash" value="', rb='"')[0]
        # print(hash1)

        # 遗留问题，附件上传不成功（已解决）
        file = r'E:\456.jpg'
        f = {'Filedata': open(file, 'rb')}
        res = self.session.post(url=Baseurl +'/misc.php?mod=swfupload&operation=upload&simple=1',
                           files=f, data={'uid': self.uid, 'hash': hash1})
        print('上传附件:',res.text)
        
        fileid = findall_data(res.text, lb='DISCUZUPLOAD|0|', rb='|-1|0')[4:7]
        print(fileid)
        fileid1 = fileid[0] + fileid[1] + fileid[2]
        print(fileid1)
        # fileid1 = fileids[0]
        self.fileid1 = fileid1
        print('上传成功的id:',fileid1)

# ************************发帖***************************
    def Publise_Invitation(self):
        data = {
            'formhash': self.formash,
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
            f'attachnew[{self.fileid1}][description]': ''
        }

        res = self.session.post(
            url=Baseurl + '/forum.php?mod=post&action=newthread&fid=2&extra=&topicsubmit=yes',
            data=data, headers=headers)
        print('发帖',res.text)

# ************************随机回复帖子*********************
    def Reply_Invitation(self):
        res = self.session.get(url=Baseurl+ '/forum.php?mod=forumdisplay&fid=2')
        tids = findall_data(res.text, lb='tid=', rb='&')  # 获取帖子Tid
        id = set(tids)  # 将列表转换为集合，去重
        tid = list(id)  # 将列表转为列表，方便获取列表元素
        # print('获取到的:', (tid))
        a = random.choice(tid)

        body = {
            'message': faker.province() + faker.city_name() + faker.district() + faker.building_number(),
            'posttime': '1614741492',
            'formhash': self.formash,
            'usesig': '1'
        }
        res = self.session.post(
            url=Baseurl+f'/forum.php?mod=post&action=reply&fid=2&tid={a}&extra=page%3D1&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1',
            data=body)
        print(res.text)


# if __name__ == '__main__':
#
#     dz = Dussiz()
#     dz.DengLu()
#     dz.Refresh_Page()
#     dz.Upload_file()
#     dz.Publise_Invitation()
#     dz.Reply_Invitation()