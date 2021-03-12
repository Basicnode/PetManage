# import allure
from  api.tests.test_case import TestCase
import  pytest
import pytest_html
import json
from api.common.data_factory import PetData
from api.common.httpclient import HttpClient
from api.common.data_factory import CaseTitle
from api.common.excel_util import Excel

# import allure


# pytest -v -s --html=report.html
if __name__ == '__main__':

    pytest.main(['-m','huice', 'test_case.py', '-v','--html=./report/report.html'])