from time import time
import csv

tic = time()

file_news = 'export_file_news.csv'

list_404 = [
"https://landcomm.ru/news/10163/",
"https://landcomm.ru/news/10248/",
"https://landcomm.ru/news/10576/",
"https://landcomm.ru/news/4527/",
"https://landcomm.ru/news/4717/",
"https://landcomm.ru/news/5035/",
"https://landcomm.ru/news/5435/",
"https://landcomm.ru/news/7967/",
"https://landcomm.ru/news/9342/",
"https://landcomm.ru/news/6189/",
"https://landcomm.ru/news/10575/",
"https://landcomm.ru/news/4349/",
"https://landcomm.ru/news/10280/",
"https://landcomm.ru/news/10740/",
"https://landcomm.ru/news/10515/",
"https://landcomm.ru/news/10586/",
"https://landcomm.ru/news/10597/",
"https://landcomm.ru/news/10954/",
"https://landcomm.ru/news/11081/",
"https://landcomm.ru/news/11393/",
"https://landcomm.ru/news/14067/",
"https://landcomm.ru/news/14404/",
"https://landcomm.ru/news/15130/",
"https://landcomm.ru/news/15471/",
"https://landcomm.ru/news/4399/",
"https://landcomm.ru/news/5346/",
"https://landcomm.ru/news/6153/",
"https://landcomm.ru/news/6753/",
"https://landcomm.ru/news/6755/",
"https://landcomm.ru/news/8755/",
"https://landcomm.ru/news/9320/",
"https://landcomm.ru/news/9325/",
"https://landcomm.ru/news/9475/",
"https://landcomm.ru/news/9497/",
"https://landcomm.ru/news/9935/",
"https://landcomm.ru/news/10005/",
"https://landcomm.ru/news/10170/",
"https://landcomm.ru/news/10195/",
"https://landcomm.ru/news/10202/",
"https://landcomm.ru/news/10775/",
"https://landcomm.ru/news/10787/",
"https://landcomm.ru/news/11724/",
"https://landcomm.ru/news/14913/",
"https://landcomm.ru/news/3986/",
"https://landcomm.ru/news/4320/",
"https://landcomm.ru/news/7766/",
"https://landcomm.ru/news/7812/",
"https://landcomm.ru/news/8048/",
"https://landcomm.ru/news/8049/",
"https://landcomm.ru/news/8287/",
"https://landcomm.ru/news/9354/",
"https://landcomm.ru/news/9474/",
"https://landcomm.ru/news/10321/",
"https://landcomm.ru/news/10753/",
"https://landcomm.ru/news/10791/",
"https://landcomm.ru/news/10952/",
"https://landcomm.ru/news/11152/",
"https://landcomm.ru/news/11169/",
"https://landcomm.ru/news/11283/",
"https://landcomm.ru/news/11713/",
"https://landcomm.ru/news/11721/",
"https://landcomm.ru/news/13123/",
"https://landcomm.ru/news/14193/",
"https://landcomm.ru/news/15571/",
"https://landcomm.ru/news/3975/",
"https://landcomm.ru/news/5036/",
"https://landcomm.ru/news/5970/",
"https://landcomm.ru/news/6573/",
"https://landcomm.ru/news/7238/",
"https://landcomm.ru/news/7869/",
"https://landcomm.ru/news/8481/",
"https://landcomm.ru/news/9157/",
"https://landcomm.ru/news/9695/",
"https://landcomm.ru/news/9715/",
"https://landcomm.ru/news/9755/",
"https://landcomm.ru/news/9900/",
"https://landcomm.ru/news/9943/",
"https://landcomm.ru/news/9997/",
"https://landcomm.ru/news/10080/",
"https://landcomm.ru/news/11291/",
"https://landcomm.ru/news/11350/",
"https://landcomm.ru/news/13342/",
"https://landcomm.ru/news/14321/",
"https://landcomm.ru/news/14484/",
"https://landcomm.ru/news/14934/",
"https://landcomm.ru/news/14969/",
"https://landcomm.ru/news/5127/",
"https://landcomm.ru/news/6196/",
"https://landcomm.ru/news/8480/",
"https://landcomm.ru/news/9312/",
"https://landcomm.ru/news/9456/",
"https://landcomm.ru/news/9941/",
"https://landcomm.ru/news/11214/",
"https://landcomm.ru/news/11830/",
"https://landcomm.ru/news/14918/",
"https://landcomm.ru/news/14920/",
"https://landcomm.ru/news/15031/",
"https://landcomm.ru/news/6141/",
"https://landcomm.ru/news/7122/",
"https://landcomm.ru/news/9941/",
"https://landcomm.ru/news/11961/",
"https://landcomm.ru/news/14724/",
"https://landcomm.ru/news/9512/",
"https://landcomm.ru/news/13850/",
"https://landcomm.ru/news/9826/",
"https://landcomm.ru/news/9941/",
"https://landcomm.ru/news/12209/",
"https://landcomm.ru/news/9971/",
"https://landcomm.ru/news/13242/",
"https://landcomm.ru/news/10291/",
"https://landcomm.ru/news/10910/",
"https://landcomm.ru/news/11243/",
"https://landcomm.ru/news/11717/",
"https://landcomm.ru/news/12514/",
"https://landcomm.ru/news/13313/",
"https://landcomm.ru/news/14259/",
"https://landcomm.ru/news/14308/",
"https://landcomm.ru/news/14424/",
"https://landcomm.ru/news/14917/",
"https://landcomm.ru/news/14950/",
"https://landcomm.ru/news/4915/",
"https://landcomm.ru/news/4946/",
"https://landcomm.ru/news/5338/",
"https://landcomm.ru/news/6195/",
"https://landcomm.ru/news/6682/",
"https://landcomm.ru/news/7056/",
"https://landcomm.ru/news/7854/",
"https://landcomm.ru/news/8286/",
"https://landcomm.ru/news/8457/",
"https://landcomm.ru/news/9261/",
"https://landcomm.ru/news/9488/",
"https://landcomm.ru/news/4664/",
"https://landcomm.ru/news/10164/",
"https://landcomm.ru/news/11766/",
"https://landcomm.ru/news/9290/",
"https://landcomm.ru/news/13239/",
"https://landcomm.ru/news/10155/",
"https://landcomm.ru/news/10786/",
"https://landcomm.ru/news/10793/",
"https://landcomm.ru/news/10953/",
"https://landcomm.ru/news/11407/",
"https://landcomm.ru/news/11653/",
"https://landcomm.ru/news/11785/",
"https://landcomm.ru/news/11792/",
"https://landcomm.ru/news/11798/",
"https://landcomm.ru/news/11824/",
"https://landcomm.ru/news/12466/",
"https://landcomm.ru/news/13722/",
"https://landcomm.ru/news/13950/",
"https://landcomm.ru/news/15070/",
"https://landcomm.ru/news/4144/",
"https://landcomm.ru/news/4352/",
"https://landcomm.ru/news/4952/",
"https://landcomm.ru/news/5984/",
"https://landcomm.ru/news/6685/",
"https://landcomm.ru/news/7160/",
"https://landcomm.ru/news/7833/",
"https://landcomm.ru/news/8941/",
"https://landcomm.ru/news/9067/",
"https://landcomm.ru/news/9174/",
"https://landcomm.ru/news/9332/",
"https://landcomm.ru/news/9486/",
"https://landcomm.ru/news/11323/",
"https://landcomm.ru/news/11369/",
"https://landcomm.ru/news/13329/",
"https://landcomm.ru/news/13370/",
"https://landcomm.ru/news/4775/",
"https://landcomm.ru/news/14828/",
"https://landcomm.ru/news/9827/",
"https://landcomm.ru/news/13243/",
"https://landcomm.ru/news/8993/",
"https://landcomm.ru/news/9832/",
"https://landcomm.ru/news/10490/",
"https://landcomm.ru/news/10906/",
"https://landcomm.ru/news/11847/",
"https://landcomm.ru/news/14945/",
"https://landcomm.ru/news/14947/",
"https://landcomm.ru/news/4057/",
"https://landcomm.ru/news/5295/",
"https://landcomm.ru/news/5360/",
"https://landcomm.ru/news/11397/",
"https://landcomm.ru/news/11408/",
"https://landcomm.ru/news/11427/",
"https://landcomm.ru/news/11472/",
"https://landcomm.ru/news/12252/",
"https://landcomm.ru/news/12441/",
"https://landcomm.ru/news/13007/",
"https://landcomm.ru/news/13999/",
"https://landcomm.ru/news/14352/",
"https://landcomm.ru/news/14774/",
"https://landcomm.ru/news/14909/",
"https://landcomm.ru/news/4340/",
"https://landcomm.ru/news/6030/",
"https://landcomm.ru/news/6084/",
"https://landcomm.ru/news/6281/",
"https://landcomm.ru/news/7226/",
"https://landcomm.ru/news/7292/",
"https://landcomm.ru/news/9935/",
]
list_404_id = []

for url in list_404:
    id = url.split('/')[-2]
    list_404_id.append(id)

def csv_reader(file_elem):
    reader = csv.reader(file_elem)
    for row in reader:
        try:
            str_row = str("".join(row))
            row_list = str_row.split(';')
            id = str(row_list[2])
            if id in list_404_id:
                simvol_code = str(row_list[3])
                print(f"RewriteRule ^(.*)news/{id}/$ https://landcomm.ru/news/{simvol_code}/ [R=301,L]")

        except:
            return 'Error'



if __name__ == "__main__":
    with open(file_news, "r", encoding='utf-8') as f_obj:
        csv_reader(f_obj)


#print(list_404_id)

print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')