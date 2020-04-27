# import section
import os
import urllib.request as request
import mysql.connector
from bs4 import BeautifulSoup

# constants section
OPEN_EDU_MAIN_URL = "https://openedu.ru"
DB_NAME = "openedu_cources"

# ##########################
# main script
# ##########################

# download list of cource's links, cource names and 
# list of direction of preparation for each cource
html_file = (request.urlopen(OPEN_EDU_MAIN_URL)).read().decode('utf-8')
soup = BeautifulSoup(html_file, 'lxml')

found_cources_links = soup.findAll("a", attrs={"class":"uho"})
found_cources_names = soup.findAll("div", attrs={"class":"course-title"})
if (found_cources_links.__len__() != found_cources_names.__len__()):
    print('Parsing error ocured')
    exit()
dbNotes = []
print('-----------------------------------------------------------------------------')
for i in range(found_cources_links.__len__()):
    print(OPEN_EDU_MAIN_URL + found_cources_links[i].attrs['href'])
    print(found_cources_names[i].a.text)
    
    # get list of directions of preparation for each cource
    html_file = (request.urlopen(
        OPEN_EDU_MAIN_URL + found_cources_links[i].attrs['href'])).read().decode('utf-8')
    soup = BeautifulSoup(html_file, 'lxml')
    found_directions_of_preparation = soup.find("div", attrs={"class":"course_groups-box"})
    if (found_directions_of_preparation == None):
        dbNotes.append((
            OPEN_EDU_MAIN_URL + found_cources_links[i].attrs['href'],
            found_cources_names[i].a.text,
            'Unknown',
        ))
        continue
    found_directions_of_preparation = found_directions_of_preparation.findAll("a")
    for val in found_directions_of_preparation:
        print('>>>>>', val.text)
        dbNotes.append((
            OPEN_EDU_MAIN_URL + found_cources_links[i].attrs['href'],
            found_cources_names[i].a.text,
            val.text,
        ))
    print('-----------------------------------------------------------------------------')

# Work with db section

# Establish connection
mydb = mysql.connector.connect(host='localhost', user='root', password='qwerty123456')
cursor = mydb.cursor()
cursor.execute("SHOW DATABASES")
foundFlag = False
for dbName in cursor:
    if (dbName[0] == DB_NAME):
        foundFlag = True
if (not foundFlag):
    cursor.execute("CREATE DATABASE " + DB_NAME)
mydb = mysql.connector.connect(host='localhost', user='root', password='qwerty123456', database=DB_NAME)
cursor = mydb.cursor()
if (not foundFlag):
    cursor.execute("CREATE TABLE cource_list (address VARCHAR(255), name VARCHAR(255), dir_of_prep VARCHAR(255))")

# Add notes, that not in db
cursor.execute("SELECT address, name, dir_of_prep FROM cource_list")
already_in_list = cursor.fetchall()
for note in dbNotes:
    foundFlag = False
    for val in already_in_list:
        if (val == note):
            foundFlag = True
    if (not foundFlag):
        cursor.execute("INSERT into cource_list (address, name, dir_of_prep) VALUES (%s, %s, %s)", note)
        mydb.commit()
print('=====================================================')
print('Data in dataBase')
print('=====================================================')
cursor.execute("SELECT address, name, dir_of_prep FROM cource_list")
for val in cursor:
    print(val)

