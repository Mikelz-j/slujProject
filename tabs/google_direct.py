from time import time
import csv

tic = time()

file = 'google.csv'

list_url = []

def csv_reader(file_elem):
    reader = csv.reader(file_elem)
    for row in reader:
        try:
            str_row = str("".join(row))
            #row_list = str_row.split(',')
            url = str(str_row.split(',')[0])
            if url[0:5] == 'https' and url not in list_url:
                list_url.append(url.split(' ')[0])
        except:
            return 'Error'



if __name__ == "__main__":
    with open(file, "r", encoding='utf-8') as f_obj:
        csv_reader(f_obj)

for url in list_url:
    print(f'"{url}",')


print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')