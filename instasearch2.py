import urllib.request
import json
from pprint import pprint
import string

nome = input("Digite a pesquisa: ")
#print("OLA"+nome+"user")

url = 'https://instagram.com/web/search/topsearch/?context=blended&query='+nome
print (url)
resp = urllib.request.urlopen(url).read()
data = json.loads(resp.decode('utf-8'))
#for i in range(0,80):
i=0
#while (i<70):
#for i in range(0,80):
#i = 0
#while True:
	#try:
usuarios = data['users']
for i in usuarios: 	
	#if isset(data['users'][i]['user']['username']):
		#print (data['users'][i]['user']['username'])
	print ("Usuario: "+i['user']['username'])		
	print ("Segudiores: "+i['user']['byline'])
	print ("Foto: "+i['user']['profile_pic_url'])
	#	i = i+1
#		break
	#except ValueError:
	       # break
	#i += 1
	#print (i)
		#i=i+1
