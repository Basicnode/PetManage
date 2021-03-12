# 封装requests
# http请求内容分析：输入-- url、method、bodytype、params、headers、body，输出--response
from api.common.excel_util import Excel
import requests
# import urllib3


class Method:
    GET = 'get'
    POST = 'post'
    DELETE = 'delete'
    PUT = 'put'

class BodyType:
    FORM_DATA = 'multipart/form-data'
    JSON = 'application/json'
    XML = 'application/xml'
    URL_ENCODE = 'application/x-www-form-urlencoded'


class HttpClient:
    def __init__(self, url, method = Method.GET, bodytype = None, params = None):
        self.__url = url
        self.__method = method
        self.__bodytype = bodytype
        self.__params = params
        self.__headers = {}
        self.__body = {}
        self.__response = None
        self.__session = None

    @property
    def response(self):
        return self.__response

    def text(self):
        return self.__response.text

    def status_code(self):
        return self.__response.status_code

    def set_body(self,body):
        if isinstance(body,dict):
            self.__body = body
        else:
            raise Exception('body数据类型必须是字典格式')

    def add_header(self, name, value):
        self.__headers[name] = value

    @property
    def headers(self):
        return self.__headers

    @headers.setter
    def headers(self, headers):
        if isinstance(headers,dict):
            self.__headers=headers

    @property
    def session(self):
        if self.__session:
            return self.__session
        self.__session = requests.sessions.session()
        return self.__session

    def send(self):
        if self.__method == Method.GET:
            self.__response = self.session.get(url=self.__url,params=self.__params,headers=self.headers)

        elif self.__method == Method.POST:
            if self.__bodytype == BodyType.JSON:
                self.__response = self.session.post(url=self.__url,json=self.__body,headers = self.headers)

            elif self.__bodytype == BodyType.URL_ENCODE or self.__bodytype == BodyType.FORM_DATA:
                self.__response = self.session.post(url=self.__url,headers=self.headers,data=self.__body)

        elif self.__method == Method.DELETE:
            pass

if __name__ == '__main__':
    excel = Excel(r'C:\Users\86132\Desktop\testcases.xlsx')
    url = excel.get_cell_value1(2, Column.Url)
    method = excel.get_cell_value1(2, Column.Method)
    client = HttpClient(url=url, method=method)

    client.send()

