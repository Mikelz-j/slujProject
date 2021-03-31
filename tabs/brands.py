import openpyxl
from time import time

tic = time()

file_brands = 'Редиректы.xlsx'
count = 33
# dist_brands = {}
#
# file_brands_new = 'new_brands.xlsx'
# count_new = 66




def gf(file):
    wb = openpyxl.reader.excel.load_workbook(filename=file)
    ws = wb.active
    return ws

# for i in range(2,count):
#     name = str(gf(file_brands)['A' + str(i)].value)
#     url = str(gf(file_brands)['B' + str(i)].value)
#     dist_brands[name] = url

for i in range(2, count):
    old_url = str(gf(file_brands)['A' + str(i)].value)
    new_url = str(gf(file_brands)['B' + str(i)].value)
    #if name in dist_brands and url != dist_brands[name]:
        #print(f'"https://landcomm.ru/catalog/{dist_brands[name]}/",')
        #print(f'"https://landcomm.ru/company/brands/{url}/",')
    #print(f"RewriteRule ^(.*){old_url[25:]}$ {new_url} [R=301,L]")
    print(f'"{new_url}",')

print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')