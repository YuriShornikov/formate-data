import csv

# Дл больших файлов, читает по 1 строке
# with open('files/newsafr.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     count = -1
#     for row in reader:
#         count += 1
#         if count == 0:
#             continue
#         print(row[-1])
# print(f'All news {count}')



# Для маленьких, читает весь файл, занося в оперативную память
# with open('files/newsafr.csv', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     new_list = list(reader)
#
#     header = new_list.pop(0)
#
#     for row in new_list:
#         print(row[-1])
#
# print()
# print(new_list[:3])
# print(f'Всего у нас {len(new_list)} новостей')

# для вызова конкретного значения
# with open('files/newsafr.csv', 'r', encoding='utf-8') as f:
#     reader = csv.DictReader(f)
#     count = 0
#     for row in reader:
#         count += 1
#         print(row['title'])
# print(f'All news {count}')



# with open('files/newsafr2.csv', 'w', encoding='utf-8') as f:
#     writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONE, escapechar='\\')
#     writer.writerow(header)
#     writer.writerows(new_list[:3])
#     # функция write.writerows как ниже раскрытая
#     # for row in new_list[:3]:
#     #     writer.writerow(row)
#
# csv.register_dialect('comma_dialect', dialect=',', quoting=csv.QUOTE_NONE, escapechar='\\')
# csv.register_dialect('other_dialect', dialect=',', quoting=csv.QUOTE_ALL, escapechar='\\')
#
# with open('files/newsafr2.csv', 'w', encoding='utf-8') as f:
#     writer = csv.writer(f, 'comma_dialect')
#     writer.writerow(header)
#     writer.writerows(new_list[:3])

import sys

import json

with open('files/newsafr.json') as f:
    json_data = json.load(f)
news_list =json_data['rss']['channel']['items']
print(f'Всего у нас {len(news_list)} новостей')
for news in news_list:
    print(news['title'])
# print(json_data)

with open('files/newsafr2.json', 'w') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)

sys.exit()