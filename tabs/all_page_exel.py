import openpyxl
from time import time

tic = time()

all_page = 'https_landcomm.ru_443_b98e34f04dcdd1833a7aa074.xlsx'

dist_url = {}

count = 3743

def gf(file):
    wb = openpyxl.reader.excel.load_workbook(filename=file)
    ws = wb.active
    return ws

for i in range(2,count):
    key = str(gf(all_page)['G' + str(i)].value)
    url = str(gf(all_page)['B' + str(i)].value)
    if '?' not in url:
        dist_url[key] = url
        print(f'"{dist_url[key]}",')



print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')