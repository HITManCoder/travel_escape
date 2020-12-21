import yagmail
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import keyring
import datetime
#Module to Scrape Destinations from www.EscapeHouston.com

#Inputs
to = 'scr343@gmail.com', 'sjh6v8@gmail.com'
subject = "Escape Houston"
file = 'EHSS.txt'
punc=','

#What deals do you want to be notified of?
city1='Albuquerque'
city2='XX'
city3='Durango'
city4='Sacramento'
city5='Farmington'
city6='XX'
city7='XX'
city8='Reno'
city9='Los Angeles'
city10='Moab'
city11=city1+punc
city22=city2+punc
city33=city3+punc
city44=city4+punc
city55=city5+punc
city66=city6+punc
city77=city7+punc
city88=city8+punc
city99=city9+punc
city100=city10+punc

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
        if i == city11:
            deals.append(x)
        if i == city22:
            deals.append(x)
        if i == city33:
            deals.append(x)
        if i == city44:
            deals.append(x)
        if i == city55:
            deals.append(x)
        if i == city66:
            deals.append(x)
        if i == city77:
            deals.append(x)
        if i == city88:
            deals.append(x)
        if i == city99:
            deals.append(x)
        if i == city100:
            deals.append(x)

# Adding Date Stamp
x=datetime.datetime.now()
today=x.strftime("%x")

#Open / Create a File / Append Date and Title
f=open(file,'a+')
f.write(today)
f.write('\n')
for element in deals:
    f.write(element)
f.write('\n')
f.close()

#Compare Date and Title for New Travel Updates
f=open(file,'r')
comparedeal=list()
for line in f:
    line=line.rstrip()
    comparedeal.append(line)
if comparedeal[-3] != comparedeal[-1] and comparedeal[-1] != '':

#if the last deal is not the same as the one before send an email update
    print(today)
    for d in deals:
        print(d)
    print(url)
#change deals list to a string
    dealsstring = ''.join(deals)

#Send out an Update Email

    password=keyring.get_password("Gmail HIT Travel", "HITTravelDeals@gmail.com")
    yag = yagmail.SMTP('HITTravelDeals@gmail.com', password)
    contents=[dealsstring, url]
    yag.send(to,subject,contents)
quit()