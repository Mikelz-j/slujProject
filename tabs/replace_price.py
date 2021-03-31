from time import time
import csv
tic = time()


old_file_price = 'export_file_611468.csv'
new_file_price = 'export_file_379701.csv'

dist_tovar = {}



def csv_reader(file_elem):
    reader = csv.reader(file_elem)
    for row in reader:
        try:
            str_row = str("".join(row))
            xml_id = str(str_row.split(';')[0])
            name = str(str_row.split(';')[1])

            dist_tovar[name] = xml_id

        except:
            return 'Error'



if __name__ == "__main__":

    with open(new_file_price, "r", encoding='utf-8') as f_obj:
        csv_reader(f_obj)



def csv_reader_for_replace(file_elem):
    reader = csv.reader(file_elem)
    for row in reader:
        try:
            str_row = str("".join(row))
            xml_id = str(str_row.split(';')[0])
            name = str(str_row.split(';')[1])
            price = str(str_row.split(';')[2])

            if name in dist_tovar:
                print(f'{dist_tovar[name]};{name};{price}')

        except:
            return 'Error'


if __name__ == "__main__":

    with open(old_file_price, "r", encoding='utf-8') as f_obj:
        csv_reader_for_replace(f_obj)




print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')