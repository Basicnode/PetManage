import  pytest
import json
from api.common.data_factory import PetData
from api.common.httpclient import HttpClient
from api.common.data_factory import CaseTitle
import allure       # 生成漂亮的html图形报告
# import pytest_html    # 生成html报告

@allure.feature('宠物管理') # 用feature说明产品需求
class TestCase:
    casedata = PetData.PetTestCase()
    @allure.story('宠物查询及新增')    # 用story说明用户场景
    @pytest.mark.huice11
    @pytest.mark.parametrize('case',casedata)
    def test_case(self,case):
        # print(case)
        client = HttpClient(url=case[CaseTitle.url],
                            method=case[CaseTitle.method],
                            bodytype=case[CaseTitle.bodyType],
                            params=case[CaseTitle.params])
        """
        百思不得其解。经过调试，最终发现，python中默认使用单引号表示字符串"'"
        所以当，用字符串符值以后，python会把双引号转换为单引号
        可以用下面的方法转换
        json_string=json.dumps(s)
        python_obj=json.loads(json_string)
        """
        client.headers = HttpClient(json.loads(json.dumps(case[CaseTitle.headers])))
        client.set_body = HttpClient(json.loads(json.dumps(case[CaseTitle.body])))
        # client.headers(json.loads(json.dumps(case[CaseTitle.headers])))
        # client.set_body(json.loads(json.dumps(case[CaseTitle.headers])))

        client.send()
        # 断言（用例中断言不对，注释掉代码）
        # assert case[CaseTitle.status_code] == client.status_code
        # assert  case[CaseTitle.message] == client.text



if __name__ == '__main__':
    # pytest.main(['-m','huice11','-v']) # 无报告执行测试用例
    # pytest.main(['-m', 'huice11', '-v', '--html=./report/report.html']) # 生成简单的html测试报告
    pytest.main(['-m', 'huice11', '-v', '--alluredir=../ruslt/']) # 生成漂亮的html测试报告

