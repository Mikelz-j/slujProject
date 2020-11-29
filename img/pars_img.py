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
        items = soup.findAll('img', {"class": "slujeb"})
        for item in items:
            src = str(item.get('src'))
            href_list.append('https://landcomm.ru/' + src)
    return href_list

def find_title(url):
    title_list = []
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
            title = href.split('/')[-2]
            title_list.append(title)
    return title_list

def title_url(list_title, list_url):
    for i in range(len(list_title)):
        dist_img[list_title[i]] = list_url[i]
    return dist_img

def get_file(url):
    return requests.get(url, stream=True)

def get_extension(url):
    path_url = url.split('/')[-1]
    return path_url[-3:]

def save_img(file, name, extension):
    with open(name+'.'+extension, 'bw') as f:
        for chunk in file.iter_content(8192):
            f.write(chunk)

def main():
    title_url(find_title(osn_url), find_url(osn_url))
    for i in dist_img:
        url = dist_img[i]
        name = i
        save_img(get_file(url), name, get_extension(url))

if __name__ == '__main__':
    main()

# print(urls)

# prov = title_url(find_title(url), find_url(url))
# prov =
# print(prov)

# print(len(find_title(url)))
# print(len(find_url(url)))

print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')