import openpyxl
from time import time
import requests

def response_code(url):
    return requests.get(url, allow_redirects=False).status_code

tic = time()

sd = {}
ff = 'redirect.xlsx'
def gf(file):
    wb = openpyxl.reader.excel.load_workbook(filename=file)
    ws = wb.active
    return ws

for i in range(2,136):
    # key = str(gf(ff)['A' + str(i)].value)
    # val = str(gf(ff)['B' + str(i)].value)
    # if val != 'None' and key != 'None':
    #     pp = val
    # if val=='None' and i > 4 :
    #     val = pp
    # if key[0:5] == 'https' and key[-4:-2] != '/p':
    #
    #     sd[key] = val
    key = str(gf(ff)['A' + str(i)].value)
    val = str(gf(ff)['B' + str(i)].value)
    if val != 'None':
        pp = val
    if response_code(key) != 301 and key[-4:-2] != '/p':
        sd[key] = pp

print()
print(len(sd))
print(sd)

for i in sd:
    old = i[21:-1]
    new = sd[i]
    print(f'RewriteRule {old}/$ {new} [R=301,L]')

#print(str_1[20:-1])

print()
toc = time()
print(str(round((toc - tic), 1)) + ' sec')