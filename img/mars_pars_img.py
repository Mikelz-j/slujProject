import requests
from bs4 import BeautifulSoup
from time import time

tic = time()

osn_url = 'https://landcomm.ru/solutions/'
count_pag = 5
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
            stran = url + 'p' + str(i) + '/'

        soup = BeautifulSoup(response(stran).content, 'html.parser')
        items = soup.findAll('a', {"class": "title"})
        for item in items:
            href = str(item.get('href'))
            href_list.append('https://landcomm.ru/' + href)
    return href_list

def find_img(list_url):
    url_img = []
    for url in list_url:
        soup = BeautifulSoup(response(url).content, 'html.parser')
        list_img_page = soup.findAll('img')
        # images_box = soup.findAll('div', {"class": "content_inner"})
        # list_img_page = images_box.find_all('img')
        for link in list_img_page:
            src =  str(link.get('src'))
            if src[0:4] != 'http':
                src = ('https://landcomm.ru' + src)
                if src not in url_img:
                    url_img.append(src)
    return url_img

def get_file(url):
    try:
        return requests.get(url, stream=True)
    except:
        return 'Error'

def get_name(url):
    try:
        path_url = url.split('/')[-1]
        path_url = path_url.replace('%20', '_')
        return path_url[:-4]
    except:
        return 'Error'

def get_extension(url):
    try:
        path_url = url.split('/')[-1]
        return path_url[-3:]
    except:
        return 'Error'

def save_img(file, name, extension):
    with open(name+'.'+extension, 'bw') as f:
        for chunk in file.iter_content(8192):
            f.write(chunk)

def main():
    for url in urls:
        try:
            save_img(get_file(url), get_name(url), get_extension(url))
        except:
            return 'Error'

urls = find_img(find_url(osn_url))

if __name__ == '__main__':
    main()

# print(urls)

prov = find_img(find_url(osn_url))
# print(prov)
print(len(prov))

# print(len(find_title(url)))
# print(len(find_url(url)))

print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')