from time import time
import csv
tic = time()

old_file = 'export_file_old_snyto.csv'
new_file = 'export_file_new_snyto.csv'

dist_snyto_old = {}
dist_snyto_new = {}

def csv_reader_old(file_elem):
    reader = csv.reader(file_elem)
    for row in reader:
        try:
            str_row = str("".join(row))
            str_name = str(str_row.split(';')[1])
            str_snyto = str(str_row.split(';')[2])
            dist_snyto_old[str_name] = str_snyto
        except:
            return 'Error'



def csv_reader_new(file_elem):
    reader = csv.reader(file_elem)
    for row in reader:
        try:
            str_row = str("".join(row))
            xml_id = str(str_row.split(';')[0])
            name = str(str_row.split(';')[1])
            if name in dist_snyto_old:
                if dist_snyto_old[name] == '12512':
                    print(f"{xml_id};{name};Постановление 969")
        except:
            return 'Error'



if __name__ == "__main__":

    with open(old_file, "r", encoding='utf-8') as f_obj:
        csv_reader_old(f_obj)

if __name__ == "__main__":

    with open(new_file, "r", encoding='utf-8') as f_obj:
        csv_reader_new(f_obj)



print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')