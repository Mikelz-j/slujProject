import openpyxl
from time import time
from openpyxl import Workbook
tic = time()

tabs_id = 'tabs_elements.xlsx'
id = 'rez.xlsx'

def gf(file):
    wb = openpyxl.reader.excel.load_workbook(filename=file)
    ws = wb.active
    return ws

def list_to_string(ll):
    str = ''
    for i in ll:
        str = str + i + ' / '

    return str

old_new_id = {}
dist_id = {}



for i in range(2,607):
    key_id = str(gf(tabs_id)['A' + str(i)].value)
    dist_id[key_id] = [(str(gf(tabs_id)['C' + str(i)].value)).split('/')]
    dist_id[key_id].append(str(gf(tabs_id)['E' + str(i)].value).split('/'))
    dist_id[key_id].append(str(gf(tabs_id)['F' + str(i)].value).split('/'))

n = 0
for i in range(2,788):
    key = str(gf(id)['B' + str(i)].value)
    old_new_id[key] = str(gf(id)['C' + str(i)].value)
    # if (n % 80) == 0:
    #     print(f'{int(n/8)} %')
    # n = n + 1
print(len(old_new_id))

wb = Workbook()
sheet = wb.active
sheet['A1'] = 'Name'
sheet['B1'] = 'Фильтры'
sheet['C1'] = 'Аксессуары и сопуствующие товары'
sheet['D1'] = 'Похожие товары'
n = 2
for i in dist_id:
    sheet['A'+str(n)] = i
    pp = 0
    for j in dist_id[i]:
        b =[]
        for k in j:
            if k != 'None':
                p = k
                s = k.split()
                if s[-1][1:-1] in old_new_id:
                    rs = s[-1][1:-1]
                    b.append(k.replace(rs, old_new_id[rs]))
        if pp == 0:
            sheet['B'+str(n)] = list_to_string(b)
        elif pp == 1:
            sheet['C'+str(n)] = list_to_string(b)
        else:
            sheet['D'+str(n)] = list_to_string(b)
        pp = pp + 1
    n = n + 1

wb.save('tt.xlsx')



print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')