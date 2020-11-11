import openpyxl
from time import time

tic = time()

dist_red = {}


wb = openpyxl.reader.excel.load_workbook(filename="red.xlsx")
ws = wb.active

for i in range(2,19):
    key = str(ws['A' + str(i)].value)
    val = [str(ws['B' + str(i)].value), str(ws['C' + str(i)].value)]
    #val[0] = str(ws['B' + str(i)].value)
    #val[1] = str(ws['C' + str(i)].value)]
    dist_red[key] = val

# for i in range(2,19):
#     key = str(ws['D' + str(i)].value)
#     val = [dist_red[key][0], str(ws['E' + str(i)].value)]
#     #val[0] = str(ws['B' + str(i)].value)
#     #val[1] = str(ws['C' + str(i)].value)]
#     dist_red[key] = val


# for i in dist_red:
#     print(i)
# print('-----------------------------')
# for i in dist_red:
#     print(dist_red[i][0])
# print('-----------------------------')
# for i in dist_red:
#     print(dist_red[i][1])
#print(len(dist_red))


for i in dist_red:
    k = dist_red[i][1]
    s = dist_red[i][0]
    print(f'RewriteRule solutions/{k}/$ https://seacomm.ru/solutions/{s}/ [R=301,L]')
    #print(f'"https://suddiesel.ru/solutions/{k}/",')
    #print(f'"https://seacomm.ru/solutions/{s}/",')

#print(dist_red)

toc = time()
print(str(round((toc - tic), 1)) + ' sec')