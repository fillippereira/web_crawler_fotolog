import requests, csv
from bs4 import BeautifulSoup

i=10

with open('/home/fgpereira/Área de Trabalho/group_fotolog.csv', 'w') as f:
    writeit = csv.writer(f, delimiter=',')

    while i<=60:
        url = "http://www.fotolog.com/group_list/popular/0/"+str(i)
        r = requests.get(url)
       # print (r.url, r.status_code)
        plain_text = r.text

        soup = BeautifulSoup(plain_text, "html.parser")
        #print(soup)
        for a in soup.findAll ('a',{'class':'wall_img_container'}):
            grupo = a.get('href')
            link = a.find_next('img').get('alt')
            writeit.writerow([grupo] + [link])



        i += 10


