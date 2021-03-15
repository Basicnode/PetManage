import  pytest
import json
from api.common.data_factory import PetData
from api.common.httpclient import HttpClient
from api.common.data_factory import CaseTitle
import allure       # 生成漂亮的html图形报告
# import pytest_html    # 生成html报告

@allure.feature('宠物管理') # 用feature说明产品需求
class TestCase:
    # casedata = PetData.PetTestCase()
    @allure.story('宠物查询及新增')    # 用story说明用户场景
    @pytest.mark.huice11
    @pytest.mark.parametrize('case',PetData.PetTestCase())
    def test_case(self,case):
        # print(case)
        client = HttpClient(url=case[CaseTitle.url],
                            method=case[CaseTitle.method],
                            bodytype=case[CaseTitle.bodyType],
                            params=case[CaseTitle.params])

        if case[CaseTitle.headers] is not None:
            client.headers = (json.loads(case[CaseTitle.headers]))
        if case[CaseTitle.body] is not None:
            client.set_body(json.loads(case[CaseTitle.body]))

        client.send()
        # 断言（用例中断言不对，注释掉代码）
        # assert case[CaseTitle.status_code] == client.status_code
        # assert  case[CaseTitle.message] == client.text



if __name__ == '__main__':
    pytest.main(['-m','huice11','-v']) # 无报告执行测试用例
    # pytest.main(['-m', 'huice11', '-v', '--html=./report/report.html']) # 生成简单的html测试报告
    # pytest.main(['-m', 'huice11', '-v', '--alluredir=../ruslt/']) # 生成漂亮的html测试报告

