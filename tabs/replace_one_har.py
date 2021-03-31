from time import time
import csv
tic = time()

fille_har = 'export_file_kol.csv'

def csv_reader(file_elem):
    reader = csv.reader(file_elem)
    for row in reader:
        try:
            str_row = str("".join(row))
            xml_id = str(str_row.split(';')[0])
            name = str(str_row.split(';')[1])
            kol = str(str_row.split(';')[2])
            price = str(str_row.split(';')[3])

            if price != '0.00' or price == '':
                print(f'{xml_id};{name}; ')

        except:
            return 'Error'



if __name__ == "__main__":

    with open(fille_har, "r", encoding='utf-8') as f_obj:
        csv_reader(f_obj)


print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')