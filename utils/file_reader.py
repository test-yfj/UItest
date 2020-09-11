# -*- coding: utf-8 -*-
# @Department: 测试
# @Author: 杨凤娇
# @Description: 文件读取。YamlReader读取yaml文件，ExcelReader读取excel。
import yaml
import os
from xlrd import open_workbook
from datetime import datetime
from xlrd import xldate_as_tuple


class YamlReader:

    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('文件不存在！')
        self._data = None

    @property
    def data(self):
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))  # load后是个generator，用list组织成列表
        return self._data


class SheetTypeError(Exception):
    pass


class ExcelReader:
    """
        读取excel文件中的内容。返回list。
        如：
        excel中内容为：                                                               .
        | A  | B  | C  |
        | A1 | B1 | C1 |
        | A2 | B2 | C2 |
        如果 print(ExcelReader(excel, title_line=True).data)，输出结果：
        [{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]
        如果 print(ExcelReader(excel, title_line=False).data)，输出结果：
        [[A,B,C], [A1,B1,C1], [A2,B2,C2]]
        可以指定sheet，通过index或者name：
        ExcelReader(excel, sheet=2)
        ExcelReader(excel, sheet='BaiDuTest')
        """
    def __init__(self, excel, sheet=None, title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError('文件不存在！')
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()

    @property
    def data(self):
        if not self._data:
            workbook = open_workbook(self.excel)
            if type(self.sheet) not in [int, str]:
                raise SheetTypeError('Please pass in <type int> or <type str>, not {0}'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)

            if self.title_line:
                # title = s.row_values(0)  # 首行为title
                # print("读取文件中一共有"+str(s.nrows)+"行")
                nrows = s.nrows  # 行数
                first_row_values = s.row_values(0)  # 第一行数据
                list = []
                num = 1
                for col in range(1, nrows):
                    # 依次遍历其余行，与首行组成dict，拼到self._data中
                    # self._data.append(dict(zip(title, s.row_values(col))))
                    row_values = s.row_values(col)
                    if row_values:
                        str_obj = {}
                    for i in range(len(first_row_values)):
                        ctype = s.cell(num, i).ctype
                        cell = s.cell_value(num, i)
                        if ctype == 2 and cell % 1 == 0.0:  # ctype为2且为浮点
                            cell = int(cell)  # 浮点转成整型
                            cell = str(cell)  # 转成整型后再转成字符串，如果想要整型就去掉该行
                        elif ctype == 3:
                            date = datetime(*xldate_as_tuple(cell, 0))
                            cell = date.strftime('%Y-%m-%d')
                        elif ctype == 4:
                            cell = True if cell == 1 else False
                        str_obj[first_row_values[i]] = cell
                    list.append(str_obj)
                    num = num + 1
                    self._data = list
            else:
                for col in range(0, s.nrows):
                    # 遍历所有行，拼到self._data中
                    self._data.append(s.row_values(col))
        return self._data


if __name__ == '__main__':
    # y = 'D:\\Users\\yanghuan\\PycharmProjects\\Testing\\config\\config.yml'
    # reader = YamlReader(y)
    # print(reader.data)

    e = 'D:\\Users\\yanghuan\\PycharmProjects\\Testing\\data\\pro_add.xlsx'
    reader = ExcelReader(e, sheet=0).data
    # print(reader)
    for b in reader:
        print(b.get("申请编号"))
        s = b.get("申请编号")
        print(s)
        for item, value in b.items():
            print(item)
            print(value)
