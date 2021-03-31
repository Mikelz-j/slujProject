import requests
from bs4 import BeautifulSoup
from time import time

tic = time()

list_url = [
"https://www.stoloto.ru/ruslotto/archive/1300",
"https://www.stoloto.ru/ruslotto/archive/1301",
"https://www.stoloto.ru/ruslotto/archive/1302",
"https://www.stoloto.ru/ruslotto/archive/1303",
"https://www.stoloto.ru/ruslotto/archive/1304",
"https://www.stoloto.ru/ruslotto/archive/1305",
"https://www.stoloto.ru/ruslotto/archive/1306",
"https://www.stoloto.ru/ruslotto/archive/1307",
"https://www.stoloto.ru/ruslotto/archive/1308",
"https://www.stoloto.ru/ruslotto/archive/1309",
"https://www.stoloto.ru/ruslotto/archive/1310",
"https://www.stoloto.ru/ruslotto/archive/1311",
"https://www.stoloto.ru/ruslotto/archive/1312",
"https://www.stoloto.ru/ruslotto/archive/1313",
"https://www.stoloto.ru/ruslotto/archive/1314",
"https://www.stoloto.ru/ruslotto/archive/1315",
"https://www.stoloto.ru/ruslotto/archive/1316",
"https://www.stoloto.ru/ruslotto/archive/1317",
"https://www.stoloto.ru/ruslotto/archive/1318",
"https://www.stoloto.ru/ruslotto/archive/1319",
"https://www.stoloto.ru/ruslotto/archive/1320",
"https://www.stoloto.ru/ruslotto/archive/1321",
"https://www.stoloto.ru/ruslotto/archive/1322",
"https://www.stoloto.ru/ruslotto/archive/1323",
"https://www.stoloto.ru/ruslotto/archive/1324",
"https://www.stoloto.ru/ruslotto/archive/1325",
"https://www.stoloto.ru/ruslotto/archive/1326",
"https://www.stoloto.ru/ruslotto/archive/1327",
"https://www.stoloto.ru/ruslotto/archive/1328",
"https://www.stoloto.ru/ruslotto/archive/1329",
"https://www.stoloto.ru/ruslotto/archive/1330",
"https://www.stoloto.ru/ruslotto/archive/1331",
"https://www.stoloto.ru/ruslotto/archive/1332",
"https://www.stoloto.ru/ruslotto/archive/1333",
"https://www.stoloto.ru/ruslotto/archive/1334",
"https://www.stoloto.ru/ruslotto/archive/1335",
"https://www.stoloto.ru/ruslotto/archive/1336",
"https://www.stoloto.ru/ruslotto/archive/1337",
"https://www.stoloto.ru/ruslotto/archive/1338",
"https://www.stoloto.ru/ruslotto/archive/1339",
"https://www.stoloto.ru/ruslotto/archive/1340",
"https://www.stoloto.ru/ruslotto/archive/1341",
"https://www.stoloto.ru/ruslotto/archive/1342",
"https://www.stoloto.ru/ruslotto/archive/1343",
"https://www.stoloto.ru/ruslotto/archive/1344",
"https://www.stoloto.ru/ruslotto/archive/1345",
"https://www.stoloto.ru/ruslotto/archive/1346",
"https://www.stoloto.ru/ruslotto/archive/1347",
"https://www.stoloto.ru/ruslotto/archive/1348",
"https://www.stoloto.ru/ruslotto/archive/1349",
"https://www.stoloto.ru/ruslotto/archive/1350",
"https://www.stoloto.ru/ruslotto/archive/1351",
"https://www.stoloto.ru/ruslotto/archive/1352",
"https://www.stoloto.ru/ruslotto/archive/1353",
"https://www.stoloto.ru/ruslotto/archive/1354",
"https://www.stoloto.ru/ruslotto/archive/1355",
"https://www.stoloto.ru/ruslotto/archive/1356",
"https://www.stoloto.ru/ruslotto/archive/1357",
"https://www.stoloto.ru/ruslotto/archive/1358",
"https://www.stoloto.ru/ruslotto/archive/1359",
"https://www.stoloto.ru/ruslotto/archive/1360",
"https://www.stoloto.ru/ruslotto/archive/1361",
"https://www.stoloto.ru/ruslotto/archive/1362",
"https://www.stoloto.ru/ruslotto/archive/1363",
"https://www.stoloto.ru/ruslotto/archive/1364",
"https://www.stoloto.ru/ruslotto/archive/1365",
"https://www.stoloto.ru/ruslotto/archive/1366",
"https://www.stoloto.ru/ruslotto/archive/1367",
"https://www.stoloto.ru/ruslotto/archive/1368",
"https://www.stoloto.ru/ruslotto/archive/1369",
"https://www.stoloto.ru/ruslotto/archive/1370",
"https://www.stoloto.ru/ruslotto/archive/1371",
"https://www.stoloto.ru/ruslotto/archive/1372",
"https://www.stoloto.ru/ruslotto/archive/1373",
"https://www.stoloto.ru/ruslotto/archive/1374",
"https://www.stoloto.ru/ruslotto/archive/1375",
"https://www.stoloto.ru/ruslotto/archive/1376",
"https://www.stoloto.ru/ruslotto/archive/1377",
"https://www.stoloto.ru/ruslotto/archive/1378",
"https://www.stoloto.ru/ruslotto/archive/1379",
"https://www.stoloto.ru/ruslotto/archive/1380",
"https://www.stoloto.ru/ruslotto/archive/1381",
]

def write_result(str):
    r = open("rez.txt", "a")
    r.write(str + '\n')
    r.close()

def response(url):
    req = requests.get(url, allow_redirects=False, verify=True)
    if req.ok:
        return req

def response_code(url):
    try:
        return response(url).status_code
    except:
        return 'Error'

def find_num(url):
    list_num = []
    soup = BeautifulSoup(response(url).content, 'html.parser')
    items = soup.findAll('span')
    for item in items:
        num = str(item.get_text())
        if len(num) == 2 and num != '\n\n':
            list_num.append(num)
    return list_num

def iterating_url(list_url):
    for url in list_url:
        num = find_num(url)
        str_num = ''.join(num)
        write_result(str_num)

iterating_url(list_url)

print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')