
from api.common.excel_util import Excel

class PetData:
    @staticmethod
    def PetTestCase(torow = None):
        excel = Excel('../data/testcases.xlsx')
        if torow:
            lastrow = torow
        else:
            lastrow = excel.get_rows_count()

        data = excel.get_range_value('A2',f'M{lastrow}')
        return data

class CaseTitle:
    module =0
    id = 1
    casename = 2
    url = 3
    method = 4
    params = 5
    headers = 6
    body = 7
    bodyType = 8
    status_code = 9
    message = 10
    result = 11
    tester =12

headers = {"Accept":"application/json"}

# h = eval(headers)
# print(h)



if __name__ == '__main__':
    case = CaseTitle
    print(CaseTitle.headers)
    # print(case)