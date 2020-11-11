import openpyxl
from time import time
from openpyxl import Workbook

tic = time()

old_id_list = "list_old_id.xlsx"
new_id_list = "list_new_id.xlsx"

# old_id_list = "list_filter_old.xlsx"
# new_id_list = "list_filter_new.xlsx"

def get_file(file):
    wb = openpyxl.reader.excel.load_workbook(filename=file)
    ws = wb.active
    return ws
dd = {}

for i in range(2,1265):
#for i in range(2,10):
    key_id = str(get_file(old_id_list)['A' + str(i)].value)
    val_id = str(get_file(old_id_list)['B' + str(i)].value)
    dd[key_id] = []
    dd[key_id].append(val_id)

for i in range(2,6376):
#for i in range(2, 8):
    key_id = str(get_file(new_id_list)['A' + str(i)].value)
    val_id = str(get_file(new_id_list)['B' + str(i)].value)
    if key_id in dd:
        dd[key_id].append(val_id)

print(len(dd))
print()
# print(dd)
fin_dd = {}
for i in dd:
    if len(dd[i]) == 2:
        fin_dd[i] = dd[i]

print(len(fin_dd))
print()
# for i in fin_dd:
#     print(f'{i} => {fin_dd[i][0]} - {fin_dd[i][1]}')

n = 2
wb = Workbook()
sheet = wb.active
sheet['A1'] = 'Name'
sheet['B1'] = 'Old_id'
sheet['C1'] = 'New_id'

for i in fin_dd:
    sheet['A'+str(n)] = i
    sheet['B'+str(n)] = fin_dd[i][0]
    sheet['C'+str(n)] = fin_dd[i][1]
    n = n + 1


wb.save('rez.xlsx')

print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')