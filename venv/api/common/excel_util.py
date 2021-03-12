# 功能：
# 1、打开；2、获取指定单元格数据；3、获取指定范围的单元格数据；4、获取用例（行）条数；5、获取列的数量；6、写入excel；7、关闭
# 类（方法、属性（类属性、实例属性））,实例属性在构造函数中定义,也可以在普通函数中定义
# Excel对象：App-->book-->sheet
import xlwings as xw
class Excel:

    def __init__(self, file):
        self.__file = file
        self.__book = None
        self.__app = None
        self.open()

    def open(self):
        """
        打开excel应用及book
        :return:
        """
        self.__app = xw.App(visible=True, add_book=False)   # 启动excel应用
        self.__book = self.__app.books.open(self.__file)    # 打开指定的excel文件

    def get_cell_value1(self, row, col, sheetname = 'sheet1'):
        """
        获取指定单元格数据
        :param row:行号
        :param col:列号
        :param sheetname:sheet名称或编号
        :return:单元格数据
        """
        if self.__book:
            sheet = self.__book.sheets[sheetname]
            return sheet[row, col].value
        else:
            # 1、写日志（推荐）；2、直接抛出异常
            raise Exception('excel文件打开失败')

    def get_cell_value2(self, cell, sheetname = 'sheet1'):
        """
        获取指定单元格数据
        :param cell: 单元格，例如A5
        :param sheetname:
        :return:
        """
        if self.__book:
            sheet = self.__book.sheets[sheetname]
            return sheet[cell].value
        else:
            # 1、写日志（推荐）；2、直接抛出异常
            raise Exception('excel文件打开失败')
    def get_range_value(self, fromcell, tocell, sheetname = 'sheet1'):
        """
        获取指定范围的单元格数据
        :param fromcell:
        :param tocell:
        :param sheetname:
        :return:
        """
        if self.__book:
            sheet = self.__book.sheets[sheetname]
            return sheet.range(fromcell, tocell).value
        else:
            # 1、写日志（推荐）；2、直接抛出异常
            raise Exception('excel文件打开失败')

    def get_rows_count(self, sheetname = 'sheet1'):
        """
        获取数据行数
        :param sheetname:
        :return:
        """
        if self.__book:
            sheet = self.__book.sheets[sheetname]
            return sheet.used_range.last_cell.row
        else:
            # 1、写日志（推荐）；2、直接抛出异常
            raise Exception('excel文件打开失败')

    def get_columns_count(self, sheetname='sheet1'):
        """
        获取数据的列数
        :param sheetname:
        :return:
        """
        if self.__book:
            sheet = self.__book.sheets[sheetname]
            return sheet.used_range.last_cell.column
        else:
            # 1、写日志（推荐）；2、直接抛出异常
            raise Exception('excel文件打开失败')

    def set_cell_color(self, cell, sheetname = 'sheet1', color=(255,0,0)):
        """
        为指定单元格设置背景色，默认红色
        :param cell:
        :param sheetname:
        :param color:
        :return:
        """
        if self.__book:
            sheet = self.__book.sheets[sheetname]
            sheet.range(cell).color=color
        else:
            # 1、写日志（推荐）；2、直接抛出异常
            raise Exception('excel文件打开失败')

    def writedata(self, cell, value):
        """
        将数据写入指定单元格中
        :param cell:
        :param value:
        :return:
        """
        if self.__book:
            sheet = self.__book.sheets[sheetname]
            sheet.range(cell).value = value
        else:
            # 1、写日志（推荐）；2、直接抛出异常
            raise Exception('excel文件打开失败')

    def close(self):
        """
        关闭excel
        :return:
        """
        if self.__book:
            self.__book.close()
        if self.__app:
            self.__app.quit()


# 以下为测试代码

if __name__ == '__main__':
    excel = Excel(r'C:\Users\86132\Desktop\testcases.xlsx') # 对应的就是一个excel文件

    m = excel.get_range_value('A2','M8')
    print(type(m))
    print(m)