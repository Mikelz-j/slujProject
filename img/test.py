import requests
from bs4 import BeautifulSoup
from time import time

tic = time()

dist_img ={}
url = 'http://test.landcomm.ru/news/lineyka-ip-telefonov-escene-us102-smenyaetsya-lineykoy-escene-es206/'

def response(url):
    req = requests.get(url, allow_redirects=False, verify=True)
    if req.ok:
        return req

def response_code(url):
    try:
        return response(url).status_code
    except:
        return 'Error'


def find_img(url):

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



prov = find_img(url)

print(f'{prov[url][0]} - {prov[url][1:]}')

print(len(prov[url])-1)


print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')