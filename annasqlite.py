#!/usr/bin/env python
"""
Anna University Name, Registration Number extractor

Copyrighted by Greedy Capitalist Pigs.

Improvement: Scraping grades to generate GPA, statistics

Feroze Naina
"""


import urllib
import urllib2
from BeautifulSoup3 import BeautifulSoup
import sqlite3


#first=int(raw_input('Enter first roll: '))
#last=int(raw_input('Enter last roll: '))
first=12008106001
last=12008106111
last+=1

conn = sqlite3.connect('test.db')

f= conn.cursor()

f.execute('create table marks (roll text, name text)')

for i in range(first,last):
    j=str(i)
    response = urllib2.urlopen("http://result.annauniv.edu/cgi-bin/result/result10gr.pl?regno="+j)
    page=response.read()
    soup=BeautifulSoup(page)
    results = soup.findAll('font', attrs={'color' : "Brown"})

    roll=results[0].renderContents()
    name=results[1].renderContents()
    print roll ," - ", name
    
    t=(roll,name)
    f.execute('insert into marks values (?,?)',t)
    
conn.commit()
f.close()

