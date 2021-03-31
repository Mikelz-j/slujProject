import openpyxl
from time import time

tic = time()

list_old_url = [
"https://seacomm.ru/catalog/95/9665/",
"https://seacomm.ru/catalog/95/9668/",
"https://seacomm.ru/catalog/95/9669/",
"https://seacomm.ru/catalog/95/9670/",
"https://seacomm.ru/catalog/95/9671/",
"https://seacomm.ru/catalog/95/9672/",
"https://seacomm.ru/catalog/95/9674/",
"https://seacomm.ru/catalog/95/9678/",
"https://seacomm.ru/catalog/95/9679/",
"https://seacomm.ru/catalog/95/9680/",
"https://seacomm.ru/catalog/95/9681/",
"https://seacomm.ru/catalog/95/9682/",
"https://seacomm.ru/catalog/95/9683/",
"https://seacomm.ru/catalog/95/9684/",
"https://seacomm.ru/catalog/95/9686/",
"https://seacomm.ru/catalog/95/9687/",
"https://seacomm.ru/catalog/95/9689/",
"https://seacomm.ru/catalog/95/9691/",
"https://seacomm.ru/catalog/95/9692/",
]

file_url = "cat95.xlsx"
count_url = 25

def find_id(list_url, id_xlsx, s_code):
    for url in list_url:
        id = url.split('/')[-2]
        if id == id_xlsx:

            new_url = url.replace(id, s_code)
            print(f"RewriteRule ^(.*){url[19:]}$ {new_url} [R=301,L]")

def gf(file):
    wb = openpyxl.reader.excel.load_workbook(filename=file)
    ws = wb.active
    return ws

for i in range(1, count_url):
    id_xlsx = str(gf(file_url)['A' + str(i)].value)
    s_code = str(gf(file_url)['B' + str(i)].value)
    find_id(list_old_url, id_xlsx, s_code)


print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')