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
while (i<70):
        print ("Usuario: "+data['users'][i]['user']['username'])
        print ("Seguidores: "+data['users'][i]['user']['byline'])
        print ("Link_Foto: "+data['users'][i]['user']['profile_pic_url'])
        #print (i)
        i=i+1
