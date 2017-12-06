import requests, csv
from bs4 import BeautifulSoup


def writeFile(grupo,user ):
    with open('/home/fgpereira/Área de Trabalho/user_fotolog.csv', 'a') as f:
        writeit = csv.writer(f, delimiter=',', lineterminator='\n')
        writeit.writerow([grupo] + [user])


def findUsers(grupo,link):
    for i in range(1, 2):
        url = "http://www.fotolog.com/"+grupo+"/participants/"
        r = requests.get(url)
        print(r.url, r.status_code)
        plain_text = r.text
        soup = BeautifulSoup(plain_text, "html.parser")


        for img in soup.findAll('img', {'class': 'img_border_radius'}):
          user = img.get('alt')
          writeFile(grupo, user)
          print(user)



with open('/home/fgpereira/Área de Trabalho/group_fotolog.csv', 'r') as f:
    data = csv.reader(f, delimiter=',')
    for row in data:
        findUsers(row[0], row[1])