import openpyxl
from openpyxl import Workbook, load_workbook

path = "D:\\files\\codes\\vs\\selenium\\Sample.xlsx"
wb=load_workbook(path)
ws=wb.active
cell = ws.cell(row = 1, column = 1) 
ws['A4']='2345'
print(ws['A4'].value)
print(wb.sheetnames)
#wb.save(filename='Sample.xlsx')