import csv
from time import time

tic = time()

news_code = 'export_file_solution.csv'

dist_news_code = {}

def csv_reader(file_elem):
    reader = csv.reader(file_elem)
    for row in reader:
        try:
            str_row = str("".join(row))
            row_list = str_row.split(';')
            name = str(row_list[1])
            code = str(row_list[2])
            #razdel = str(row_list[3])

            dist_news_code[name] = '/projects/'  + code + '/'
            #print('"' + name + '": "' + dist_news_code[name] + '",')
            print(f'"http://test.landcomm.ru{dist_news_code[name]}",')


        except:
            return 'Error'



if __name__ == "__main__":

    with open(news_code, "r", encoding='utf-8') as f_obj:
        csv_reader(f_obj)



print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')