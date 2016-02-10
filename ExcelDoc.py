import os
import datetime
from openpyxl import Workbook


class ExcelDoc:

    def __init__(self):
        pass

    def create_excel_doc(self, infosheet, monday, tuesday, wednesday,
                         thursday, friday, saturday, sunday):

        workbook = Workbook()
        sheet1 = workbook.create_sheet(infosheet)
        sheet2 = workbook.create_sheet(monday)
        sheet3 = workbook.create_sheet(tuesday)
        sheet4 = workbook.create_sheet(wednesday)
        sheet5 = workbook.create_sheet(thursday)
        sheet6 = workbook.create_sheet(friday)
        sheet7 = workbook.create_sheet(saturday)
        sheet8 = workbook.create_sheet(sunday)

        workbook.save('workbook_test.xlsx')

        return

    def fill_excel_doc(self):

        return