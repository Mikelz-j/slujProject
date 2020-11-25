import openpyxl
from time import time

tic = time()

dist_red = {}
dist_fin = {}


old_list = 'list_old_catalog1.xlsx'
new_list = 'list_new_catalog.xlsx'
# old_directori = 'dokumentacija'
# new_directori = 'dokumentacija'
old_count = 287
new_count = 315
old_raz = 'old_razdel.xlsx'
new_raz = 'new_razdel.xlsx'

list_old_razdel = {}
list_new_razdel = {}

def gf(file):
    wb = openpyxl.reader.excel.load_workbook(filename=file)
    ws = wb.active
    return ws

for i in range(2,50):
    key = str(gf(old_raz)['A' + str(i)].value)
    raz = str(gf(old_raz)['B' + str(i)].value)
    list_old_razdel[key] = raz

for i in range(2,168):
    key = str(gf(new_raz)['A' + str(i)].value)
    raz = str(gf(new_raz)['B' + str(i)].value)
    list_new_razdel[key] = raz

# print(len(list_old_razdel))
# print(list_old_razdel)
# print()
# print(len(list_new_razdel))
# print(list_new_razdel)

for i in range(2,old_count+1):
    key = str(gf(old_list)['A' + str(i)].value)
    old_url = [str(gf(old_list)['B' + str(i)].value)]
    old_raz = str(gf(old_list)['C' + str(i)].value)
    dist_red[key] = old_url
    dist_red[key].append(old_raz)

for i in range(2,new_count+1):
    key = str(gf(new_list)['A' + str(i)].value)
    new_url = str(gf(new_list)['B' + str(i)].value)
    new_raz = str(gf(new_list)['C' + str(i)].value)
    if key in dist_red:
        dist_red[key].append(new_url)
        dist_red[key].append(new_raz)

for i in dist_red:
    if len(dist_red[i]) == 4:
        dist_fin[i] = dist_red[i]

print(len(dist_fin))
print(dist_fin)


print('Redirect rule')
print()
for i in dist_fin:
    print(f"RewriteRule catalog/{list_old_razdel[dist_fin[i][1]]}/{dist_fin[i][0]}/$ https://seacomm.ru/catalog/{list_new_razdel[dist_fin[i][3]]}/{dist_fin[i][2]}/ [R=301,L]")

print()
print('////////////////////////////////////////////////////////////////////////////////////////////////////////')
print()

print('List old urls')
print()
for i in dist_fin:
    print(f"https://satprocom.ru/catalog/{list_old_razdel[dist_fin[i][1]]}/{dist_fin[i][0]}/")

print()
print('////////////////////////////////////////////////////////////////////////////////////////////////////////')
print()

print('List new urls')
print()
for i in dist_fin:
    print(f"https://seacomm.ru/catalog/{list_new_razdel[dist_fin[i][3]]}/{dist_fin[i][2]}/")


print()
toc = time()
print(str(round((toc - tic), 1)) + ' sec')