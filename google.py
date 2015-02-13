#!/usr/bin/python
import mechanize
from mechanize import Browser
import array
import urllib2
import time
import re
from bs4 import BeautifulSoup
from urlparse import urlparse
import hashlib
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders= [('User-agent','chrome')]
term = "thales".replace(" ","+")
query = "https://www.google.com/search?q="+term
htmltext = br.open(query).read()
soup = BeautifulSoup(htmltext)
search = soup.findAll('div',attrs={'id':'search'})          
searchtext = str(search[0])
soup1 = BeautifulSoup(searchtext)
list_items = soup1.findAll('li')
regex = "q(?!.*q).*?&amp"
pattern = re.compile(regex)
for li in list_items:
        soup2 = BeautifulSoup(str(li))
        links = soup2.findAll('a')
        source_link = links[0]
        source_url = re.findall(pattern,str(source_link))
        if len(source_url)>0:
                if source_url[0].find('http') != -1:  #joga tudo com http, filtra com o q eu quero
                                if source_url[0].find('q%3Dcache:') :

                                            print source_url[0].replace("q=","").replace("&amp","").replace("related:","")
