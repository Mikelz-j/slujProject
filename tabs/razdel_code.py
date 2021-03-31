import openpyxl
from time import time

tic = time()

list_code = 'new_razdel_code.xlsx'
count_str = 45
dd = {}

def get_file(file):
    wb = openpyxl.reader.excel.load_workbook(filename=file)
    ws = wb.active
    return ws

for i in range(2, count_str):
    key = str(get_file(list_code)['A' + str(i)].value)
    value = str(get_file(list_code)['B' + str(i)].value)
    dd[key] = value
    print('"'+key+'": "'+value+'",')
#print(dd)

print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')