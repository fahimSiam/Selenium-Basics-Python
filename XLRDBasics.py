import xlrd
wb=xlrd.open_workbook("Sample.xls")
ws=wb.sheet_by_index(0)

rowCount=ws.nrows
print(rowCount)

