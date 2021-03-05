import re
# 左右边界函数 (提取字段)
def findall_data(text, lb="", rb=""):
    rule = lb + r"(.+?)" + rb
    datalist = re.findall(rule, text)
    return datalist