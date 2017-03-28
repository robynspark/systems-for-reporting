import csv
import requests
from BeautifulSoup import BeautifulSoup
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

url = 'https://columbian.gwu.edu/2015-2016'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table')

list_of_rows = []
for row in table.findAll('tr')[1:-1]:
    list_of_cells = []
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text.encode('utf-8'))
    list_of_rows.append(list_of_cells)

outfile = open("college.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Department", "Faculty", "Sponsor", "Title"])
writer.writerows(list_of_rows)

url = 'https://columbian.gwu.edu/2014-2015'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table')

list_of_rows = []
for row in table.findAll('tr')[1:-1]:
    list_of_cells = []
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text.encode('utf-8'))
    list_of_rows.append(list_of_cells)

outfile = open("college.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Department", "Faculty", "Sponsor", "Title"])
writer.writerows(list_of_rows)

url = 'https://columbian.gwu.edu/2013-2014'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table')

list_of_rows = []
for row in table.findAll('tr')[1:-1]:
    list_of_cells = []
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text.encode('utf-8'))
    list_of_rows.append(list_of_cells)

outfile = open("college.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Department", "Faculty", "Sponsor", "Title"])
writer.writerows(list_of_rows)