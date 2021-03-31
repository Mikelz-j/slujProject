import csv
from time import time

tic = time()

all_page = 'all_yandex.csv'

dist_url = {}

def csv_reader(file_elem):
    reader = csv.reader(file_elem)
    for row in reader:
        try:
            str_row = str(" ".join(row))
            # row_list = str_row.split(',')
            # name = str(row_list[6])
            # url = str(row_list[1])
            #razdel = str(row_list[3])

            dist_url[name] = url
            print(str_row)
            #print(f'{url},')


        except:
            return 'Error'



if __name__ == "__main__":

    with open(all_page, "r", encoding='utf-8', newline='') as f_obj:
        csv_reader(f_obj)


print(dist_url)
print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')