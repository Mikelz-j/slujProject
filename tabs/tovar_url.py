import openpyxl
import csv
from time import time

tic = time()

old_razdel = {
"Цифровые телефонные станции": "532",
"Цифровое оборудование": "530",
"Факсы": "558",
"УКВ антенны VHF": "342",
"УКВ антенны": "341",
"Терминалы и модули систем безопасности и связи": "499",
"Терминалы для тюремных камер": "519",
"Терминалы для промышленности": "515",
"Телефоны DECT": "533",
"Телефоны / факсы": "382",
"Системы безопасности и связи": "528",
"Системные телефоны": "534",
"Сетевое оборудование": "673",
"Ретрансляторы": "retranslyatory",
"Репитеры": "489",
"Распродажа со склада - дёшево и в наличии!": "688",
"Радиотелефоны": "575",
"Промышленные телефоны": "524",
"Промышленные роутеры и модемы": "488",
"Программное обеспечение, ключи активации и лицензии": "535",
"Программное обеспечение, ключи активации и лицензии": "539",
"Постановление 969 Транспортная безопасность": "postanovlenie-969",
"Портативные радиостанции": "kupit-raciyu",
"Поворотные IP-камеры": "373",
"Переговорное оборудование": "490",
"Настенные и настольные терминалы связи, вызывные панели": "497",
"Модули, платы и блоки расширения": "moduli-platy-i-bloki-rasshireniya",
"Модули, платы и блоки расширения": "537",
"Модули Системы контроля и управления доступом (СКУД)": "517",
"Микрофоны": "371",
"Маршрутизаторы": "674",
"Купольные IP-камеры": "366",
"Кубические IP-камеры": "543",
"Крепления и принадлежности для установки": "538",
"Крепления": "509",
"Корпусные IP-камеры": "368",
"Коммутаторы": "675",
"КВ трансиверы": "kv-transivery",
"КВ антенны": "552",
"Источники питания": "365",
"Источники питания": "540",
"Интерком-модули": "518",
"ЖК-мониторы": "607",
"Дуплексеры и преселекторы": "340",
"Другие аксессуары": "drugie-aksessuary",
"Дополнительное оборудование": "608",
"Дверные переговорные устройства": "516",
"Гарнитуры": "331",
"Видеосерверы": "635",
"Видеорегистраторы": "583",
"Видеонаблюдение": "581",
"Видеоконференцсвязь": "346",
"Видеокамеры": "582",
"Антивандальные терминалы": "514",
"Антенны для раций": "antenna-dlya-racii",
"Аналоговые телефоны": "542",
"Аксессуары для цифрового оборудования": "536",
"Аксессуары для терминалов системы безопасности и связи": "501",
"Аксессуары для портативных радиостанций": "328",
"Аксессуары для мобильных радиостанций": "329",
"Аксессуары для IP оборудования": "aksessuary-dlya-ip-oborudovaniya",
"Автомобильные телефоны": "406",
"Автомобильные рации": "kupit-avtomobilnuyu-raciyu",
"Автомобильные антенны": "587",
"Wi-Fi роутеры": "676",
"VoIP шлюзы": "383",
"SIP адаптеры": "545",
"IP телефоны": "ip-telefony",
"IP конференц-телефоны": "ip-konferents-telefony",
"IP и SIP телефоны": "kupit-ip-telefon",
"IP видеотелефоны": "ip-videotelefony",
"IP видеокамеры": "353",
"IP АТС": "320",
"IP DECT": "ip-dect",
"GSM оборудование": "405",
}

new_razdel = {
"Сетевое оборудование": "setevoe-oborudovanie",
"IP телефония и сетевое оборудование": "ip-telefoniya-i-setevoe-oborudovanie",
"Сетевое GSM оборудование": "setevoe-gsm-oborudovanie",
"Wi Fi роутеры": "wi-fi-router",
"Сетевые коммутаторы": "setevoy-kommutator",
"Маршрутизаторы": "marshrutizator",
"IP телефоны": "ip-telefon",
"IP АТС": "ip-ats",
"IP видеокамеры": "ip-videokamery",
"Видеоконференцсвязь": "videokonferencsvyaz",
"VoIP шлюзы": "voip-shlyuzy",
"SIP адаптеры": "sip-adaptery",
"Аксессуары для IP оборудования": "aksessuary-dlya-ip-oborudovaniya",
"Спутниковое оборудование": "sputnikovoe-oborudovanie",
"Портативные радиостанции": "kupit-raciyu",
"Рации": "radiostancii",
"КВ-трансиверы": "kv-transiver",
"Ретрансляторы": "retranslyator",
"Аксессуары для мобильных радиостанций": "aksessuary-dlya-mobilnykh-radiostantsiy",
"Аксессуары для портативных радиостанций": "aksessuary-dlya-portativnykh-radiostantsiy",
"Антенны для раций": "antenna-dlya-racii",
"Тарифы спутниковой связи": "tarif-sputnikovoy-svyazi",
"Домашний спутниковый Интернет": "domashniy-sputnikovyy-internet",
"Аксессуары спутникового оборудования": "aksessuar-sputnikovogo-oborudovaniya",
"VSAT": "vsat",
"Спутниковые телефоны": "sputnikovyj-telefon",
"Спутниковые терминалы": "sputnikovyj-terminal",
"Дополнительное телефонное оборудование": "dopolnitelnoe-telefonnoe-oborudovanie",
"Дополнительное оборудование систем видеонаблюдения": "dopolnitelnoe-oborudovanie-sistem-videonablyudeniya",
"ЖК мониторы систем видеонаблюдения": "zhk-monitory",
"Видеорегистраторы систем видеонаблюдения": "videoregistrator-sistem-videonablyudeniya",
"Камеры систем видеонаблюдения": "kamera-sistem-videonablyudeniya",
"Системы видеонаблюдения": "sistemy-videonablyudeniya",
"Комплекты систем безопасности и связи": "komplekty-sistem-bezopasnosti",
"Промышленные телефоны": "promyshlennyj-telefon",
"АТС": "ats",
"Факсы": "faks",
"Радиотелефоны": "radiotelefon",
"Системные телефоны": "sistemnyj-telefon",
"Телефоны DECT": "telefon-dect",
"Системы безопасности и связи": "sistemy-bezopasnosti-i-svyazi",
"Телефоны и факсы": "telefony-i-faksy",
"Автомобильные рации": "kupit-avtomobilnuyu-raciyu",
}

#tovar_code = 'new_code_tovar_1.xlsx'

tovar_code = 'export_file_url_tovara.csv'

#count = 4671

dist_tovar_code = {}


# def gf(file):
#     wb = openpyxl.reader.excel.load_workbook(filename=file)
#     ws = wb.active
#     return ws
#
# for i in range(2,count):
#     key = str(gf(tovar_code)['A' + str(i)].value)
#     razdel = str(gf(tovar_code)['B' + str(i)].value)
#     if razdel in new_razdel:
#         razdel_code = new_razdel[razdel]
#         code = str(gf(tovar_code)['C' + str(i)].value)
#
#         dist_tovar_code[key] = '/catalog/' + razdel_code + '/' + code + '/'
#
#         print('"' + key + '": "' + dist_tovar_code[key] + '",')



def csv_reader(file_elem):
    reader = csv.reader(file_elem)
    for row in reader:
        try:
            str_row = str("".join(row))
            row_list = str_row.split(';')
            #xml_id = str(row_list[0])
            name = str(row_list[1])
            code = str(row_list[2])
            razdel = str(row_list[3])

            if razdel in new_razdel:
                razdel_code = new_razdel[razdel]

                dist_tovar_code[name] = 'catalog/' + razdel_code + '/' + code + '/'

                #print('"' + name + '": "' + dist_tovar_code[name] + '",')
        except:
            return 'Error'



if __name__ == "__main__":

    with open(tovar_code, "r", encoding='utf-8') as f_obj:
        csv_reader(f_obj)


for name in old_razdel:
    if name in new_razdel and old_razdel[name] != new_razdel[name]:
        print(f"RewriteRule ^catalog/{old_razdel[name]}/$ https://landcomm.ru/catalog/{new_razdel[name]}/ [R=301,L]")

print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')