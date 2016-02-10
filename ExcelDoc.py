import os
import datetime
from xlwt import Workbook

class ExcelDoc:

    def __init__(self):
        pass

    def create_excel_doc(self):

        workbook = Workbook()
        sheet1 = workbook.add_sheet('Info')
        sheet2 = workbook.add_sheet('Monday')
        sheet3 = workbook.add_sheet('Tuesday')
        sheet4 = workbook.add_sheet('Wednesday')
        sheet5 = workbook.add_sheet('Thursday')
        sheet6 = workbook.add_sheet('Friday')
        sheet7 = workbook.add_sheet('Saturday')
        sheet7 = workbook.add_sheet('Sunday')

        workbook.save('workbook_test.xls')
        return