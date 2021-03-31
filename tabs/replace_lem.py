import openpyxl
from time import time
from openpyxl import Workbook
tic = time()


tabs_null = 'list_item.xlsx'
tabs_price = 'list_price.xlsx'

dist_elem = {}


def gf(file):
    wb = openpyxl.reader.excel.load_workbook(filename=file)
    ws = wb.active
    return ws


# for i in range(2,10):
#     key = str(gf(tabs_price)['B' + str(i)].value)
#     dist_elem[key] = [gf(tabs_price)['G' + str(i)].value]
#     dist_elem[key].append(gf(tabs_price)['H' + str(i)].value)




#print(dist_elem)

print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')