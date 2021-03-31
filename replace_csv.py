from time import time
import csv
import openpyxl

tic = time()

id = 'rez_cat.xlsx'
count_row = 4588
csv_path = "export_file_arsesuar.csv"


dist_id = {}

def gf(file):
    wb = openpyxl.reader.excel.load_workbook(filename=file)
    ws = wb.active
    return ws


def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    for row in reader:
        try:
            str_row = (" ".join(row))
            id_old = (str_row.split(';')[-1])
        except:
            return 'Error'

        if id_old in dist_id:
            str_new_id = str_row.replace(id_old, dist_id[id_old])
            print(str_new_id)

for i in range(2,count_row):
    key_id = str(gf(id)['B' + str(i)].value)
    dist_id[key_id] = str(gf(id)['C' + str(i)].value)




if __name__ == "__main__":

    with open(csv_path, "r", encoding='utf-8') as f_obj:
        csv_reader(f_obj)




print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')