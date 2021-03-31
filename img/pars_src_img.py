import requests
from bs4 import BeautifulSoup
from time import time

tic = time()

osn_url = 'http://test.landcomm.ru/projects/'
count_pag = 4
dist_img = {}

def response(url):
    req = requests.get(url, allow_redirects=False, verify=True)
    if req.ok:
        return req

def response_code(url):
    try:
        return response(url).status_code
    except:
        return 'Error'

def find_url(url):
    href_list = []
    stran = ''
    for i in range(count_pag):
        if i == 0:
            stran = url
        else:
            stran = url + '?PAGEN_1=' + str(i)

        soup = BeautifulSoup(response(stran).content, 'html.parser')
        items = soup.select('.slujeb')

        for item in items:
            href = str(item.get('href'))
            href_list.append('http://test.landcomm.ru' + href)
    return href_list

def find_img(list_url):
    for url in list_url:
        soup = BeautifulSoup(response(url).content, 'html.parser')
        title_page = soup.find('h1').get_text()
        dist_img[url] = [title_page]
        list_img_page = soup.findAll('img')
        for link in list_img_page:
            src = str(link.get('data-src'))
            if src[0:4] != 'http' and src[0:4] != 'data':
                src = ('http://test.landcomm.ru' + src)
                if response_code(src) !=200:
                    dist_img[url].append(src + ' - ' + str(response_code(src)))
    return dist_img


prov = find_img(find_url(osn_url))

for i in prov:
    if len(prov[i]) > 1:
        print(f'{prov[i][0]} - {prov[i][1:]}')

print(len(prov))


print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')