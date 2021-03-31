from time import time
import csv

tic = time()

old_xml_id = "xml_id_old.csv"
new_xml_id = "xml_id_new.csv"

dist_xml_id = {}

# def csv_reader(file_elem):
#     reader = csv.reader(file_elem)
#     for row in reader:
#         str_row = str("".join(row))
#         print(str_row)

# for row in csv_reader(old_xml_id):
#     try:
#         str_row = str("".join(row))
#         name = str(str_row.split(';')[1])
#         xml_id = str(str_row.split(';')[0])
#         dist_xml_id[name] = [xml_id]
#     except:
#         continue

def csv_reader_old(file_elem):
    reader = csv.reader(file_elem)
    for row in reader:
        try:
            str_row = str("".join(row))
            name = str(str_row.split(';')[1])
            xml_id = str(str_row.split(';')[0])
            dist_xml_id[name] = [xml_id]

        except:
            return 'Error'

        #print('"'+name+'": "'+xml_id+'",')


def csv_reader_new(file_elem):
    reader = csv.reader(file_elem)
    for row in reader:
        try:
            str_row = str("".join(row))
            name = str(str_row.split(';')[1])


        except:
            return 'Error'

        if name in dist_xml_id:
            xml_id = str(str_row.split(';')[0])
            if xml_id != dist_xml_id[name]:
                dist_xml_id[name].append(xml_id)
            else:
                del dist_xml_id[name]

        #print('"'+name+'": "'+xml_id+'",')



if __name__ == "__main__":
    with open(old_xml_id, "r", encoding='utf-8') as f_obj:
        csv_reader_old(f_obj)

if __name__ == "__main__":
    with open(new_xml_id, "r", encoding='utf-8') as f_obj:
        csv_reader_new(f_obj)


#for name in dist_xml_id:
#    print('"'+name+'": "['+dist_xml_id[name][0]+', '+dist_xml_id[name][1]+']",')



print(dist_xml_id)
print(len(dist_xml_id))

#print(csv_reader(old_xml_id))

print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')