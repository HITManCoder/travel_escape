import yagmail
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl
import keyring
import datetime
import sqlite3
from pathlib import Path
#Module to Scrape Destinations from www.EscapeHouston.com

#Inputs
#emails = 'xx@gmail.com', 'xx@gmail.com'
subject = "Escape Houston"
password = keyring.get_password("Gmail HIT Travel", "HITTravelDeals@gmail.com")
email1 = keyring.get_password("email", "scr")
email2 = keyring.get_password('email', 'sjr')
emails=(email1, email2)

file='ehss.txt'
db_path = Path(r"C:\Users\Stephen\Python\Travel")
db_file = db_path / "Escape.db"

# Create Database Connections
cnx = sqlite3.connect(db_file)
cur = cnx.cursor()

#What deals do you want to be notified of?
allflights='Flights:' # use Flights for all trips and include punctuation
city1='XX'
city2='XX'
city3='Durango'
city4='Sacramento'
city5='Farmington'
city6='XX'
city7='XX'
city8='Boise'
city9='XX'
city10='Moab'


#Scraping
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://escapehouston.com/category/cheap-flights-from-houston/'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#Lists needed
info=list()
deals=list()

#Limits the findings to blog post title and description
title = soup.find_all('div', class_ = 'excerpt-header')
description = soup.find_all('div', class_ = 'excerpt-content')

#Creates a list that includes blog title (Not using description):
for t, in title:
    info=info+[t.text]

#Creating Deal (deals) list by limiting blog titles to only those we are interested in:
for x in info:
    word=x.split()

    for i in word:
        if i == allflights:
            deals.append(x)
        if i == city1:
            deals.append(x)
        if i == city2:
            deals.append(x)
        if i == city3:
            deals.append(x)
        if i == city4:
            deals.append(x)
        if i == city5:
            deals.append(x)
        if i == city6:
            deals.append(x)
        if i == city7:
            deals.append(x)
        if i == city8:
            deals.append(x)
        if i == city9:
            deals.append(x)
        if i == city10:
            deals.append(x)

# Adding Date Stamp
today=datetime.datetime.now()
todaystr=today.strftime("%x")

for element in deals:
    cur.execute('''INSERT OR IGNORE INTO people (datetime_txt, flights) VALUES (?, ?)''', (today, element))

cnx.commit()

cur.execute('''SELECT flights 
                FROM people
                WHERE datetime_txt = ( SELECT MAX(datetime_txt) 
                FROM people
                WHERE datetime_txt < ( SELECT MAX(datetime_txt) 
                FROM people)
                )''')
date2deals=cur.fetchall()


cur.execute('''SELECT flights 
                FROM people 
                WHERE datetime_txt = (SELECT MAX(datetime_txt)
                FROM people)''')
date1deals=cur.fetchall()

# Compare Date and Title for New Travel Updates
difference=set(date1deals)-set(date2deals)
if len(difference) != 0:

#Send out an Update Email


    yag = yagmail.SMTP('HITTravelDeals@gmail.com', password)
    contents=[todaystr, url, date1deals]
    yag.send(emails,subject,contents)

quit()