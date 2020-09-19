import urllib
import urllib.request
import html.parser
import requests
from requests.exceptions import HTTPError
from socket import error as SocketError
from http.cookiejar import CookieJar
from bs4 import BeautifulSoup
import json
import time
import io

for page in range(1, 32):
    time.sleep(1)
    try:
        url = 'https://www.dofus.com/fr/mmorpg/encyclopedie/equipements?page='+str(page)
        #url = 'https://www.dofus.com/en/mmorpg/encyclopedia/equipment?page='+str(page)
        #url = 'https://www.dofus.com/fr/mmorpg/encyclopedie/armes?page='+str(page)
        #url = 'https://www.dofus.com/en/mmorpg/encyclopedia/weapons?page='+str(page)
        req=urllib.request.Request(url, None, {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; G518Rco3Yp0uLV40Lcc9hAzC1BOROTJADjicLjOmlr4=) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Connection': 'keep-alive'})
        cj = CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        response = opener.open(req)
        raw_response = response.read().decode('utf-8')
        response.close()
    except urllib.request.HTTPError as inst:
        output = format(inst)
        print(output)

    soup = BeautifulSoup(raw_response,'html.parser')

    sspan = soup.find_all('span')

    '''from pprint import pprint
    pprint(vars(sspan[60]))
    pprint(vars(sspan[61]))'''

    for items in sspan:
        if str(items.contents).find('[<a href=') == 0 and items.text != '':
            data_file = io.open('items_en.txt', 'a+', encoding="utf-8")
            #data_file = io.open('items_fr.txt', 'a+', encoding="utf-8")
            data_file.write(items.text+'\n')
            print(items.text)

   