import openpyxl
from time import time

tic = time()

all_page = '8345859.xlsx'

list_url = []

count = 668

def gf(file):
    wb = openpyxl.reader.excel.load_workbook(filename=file)
    ws = wb.active
    return ws

for i in range(12,count):
    url = str(gf(all_page)['Q' + str(i)].value)
    if url not in list_url:
        list_url.append(url)


for url in list_url:
    print(f'"{url}",')


print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')