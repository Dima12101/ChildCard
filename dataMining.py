import requests
import csv
from bs4 import BeautifulSoup


def GetRows(table):
    rows = []
    for tr in table.find_all('tr')[2:]:
        tdAge = tr.find_all('td')[0].text
        countAge = tdAge.split(' ')[0]
        nameAge = tdAge.split(' ')[1]
        if nameAge == 'мес.':
            nameAge = 'month'
        elif nameAge == 'год' or nameAge == 'года' or nameAge == 'лет':
            nameAge = 'year'
        age = '{} {}'
        rows.append([age.format(countAge, nameAge)] + [td.text for td in tr.find_all('td')[1:]])
    return rows


def createTables(name, url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    tables = soup.find_all(class_='data')

    title = ["age", "3", "10", "25", "50", "75", "90", "97"]
    with open(f'centileTables/{name}Man.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(title)
        writer.writerows(GetRows(tables[0]))

    with open(f'centileTables/{name}Girl.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(title)
        writer.writerows(GetRows(tables[1]))


if __name__ == '__main__':
    createTables(name='weight', url='https://www.ourbaby.ru/article/1417')
    createTables(name='growth', url='https://www.ourbaby.ru/article/1418')
    createTables(name='circleHead', url='https://www.ourbaby.ru/article/1425')
    createTables(name='circleChest', url='https://www.ourbaby.ru/article/1423')


