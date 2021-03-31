from time import time
import requests
from bs4 import BeautifulSoup
import csv

tic = time()


main_url = "https://test.landcomm.ru/catalog/brands/14802/?page_size=all"
#main_url = "https://landcomm.ru/catalog/kupit-raciyu/"

directory = "https://test.landcomm.ru"
file_elem = "export_file_nb.csv"

def response(url):
    req = requests.get(url, allow_redirects=False, verify=True)
    if req.ok:
        return req

def response_code(url):
    return requests.get(url, allow_redirects=False).status_code

def find_item (url):
    item_list = []
    soup = BeautifulSoup(response(url).content, 'html.parser')
    elements = soup.findAll("a", class_="item")
    for elem in elements:
        href = directory + str(elem.get('href'))
        item_list.append(href)

    return item_list


def parser_har (list_url):
    dist_har = {}
    for url in list_url:
        if response_code(url) == 200:
            soup = BeautifulSoup(response(url).content, 'html.parser')
            name_elem = (soup.find("h1"))
            name = str(name_elem.get('data-name'))
            har_elem = (soup.find("div", class_="features"))
            dist_har[name] = str(har_elem)

    return dist_har


def csv_reader(file_elem):
    dist_har = parser_har(find_item(main_url))
    reader = csv.reader(file_elem)
    for row in reader:
        try:
            str_row = str("".join(row))
            str_name = str(str_row.split(';')[-1])

        except:
            return 'Error'
        if str_name in dist_har:
            print(str_row+";"+dist_har[str_name])

# print(find_item(main_url))
# print(len(find_item(main_url)))


if __name__ == "__main__":

    with open(file_elem, "r", encoding='utf-8') as f_obj:
        csv_reader(f_obj)




# csv_reader(file_elem)
#print(parser_har(find_item(main_url)))
# print(len(prov))




print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')