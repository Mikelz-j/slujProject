import openpyxl
from time import time

tic = time()

sd = {}
ff = 'list_url_solut.xlsx'
count_str = 35
razdel = 'solutions'
site = 'https://landcomm.ru'


def gf(file):
    wb = openpyxl.reader.excel.load_workbook(filename=file)
    ws = wb.active
    return ws

for i in range(2,count_str + 1):
    key = str(gf(ff)['B' + str(i)].value)
    val = str(gf(ff)['C' + str(i)].value)
    sd[key] = val

print()
print(len(sd))
print(sd)

for i in sd:
    new = i
    old = sd[i]
    print(f'RewriteRule {razdel}/{old}/$ {site}/{razdel}/{new}/ [R=301,L]')

print()
print('List old url')

for i in sd:
    print(f'"{site}/{razdel}/{sd[i]}/",')


print()
print('List new url')

for i in sd:
    print(f'"{site}/{razdel}/{i}/",')




print()
toc = time()
print(str(round((toc - tic), 1)) + ' sec')