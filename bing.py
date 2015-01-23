#!/usr/bin/python
import mechanize
import array
import urllib2
import time
import re
from bs4 import BeautifulSoup
from urlparse import urlparse
import hashlib
i=1
string = raw_input("Digite sua pesquisa: ")
    ##for n in range(1,70,10):
            ##time.sleep(2)##  
            ##n = str(n)
while (i<300):  
            html_content = urllib2.urlopen("http://www.bing.com/search?q="+string+"&first="+str(i)).read()
           
            links = []
            soup = BeautifulSoup(html_content)
            resultado = soup.findAll('a')
            time.sleep(1.32)
            i = i+10
            for link in soup.find_all('a'):
              url = link.get('href')
              if url is not None:
                        if url.find('http://www') != -1:  #joga tudo com http, filtra com o q eu quero
                                if url.find('http://www.microsofttranslator.com/') : ##cria filtro, eliminando
                                ##url.strip('http://www.microsofttranslator.com/')
                                        url = ('')                                     
                                        print(link.get('href'))
                                        var_file = open("bingado.txt","a")
                                        var_file.write(link.get('href'))
                                        var_file.close()