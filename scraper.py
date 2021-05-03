from lxml import html
import requests
from datetime import datetime, date

from functions import get_data

# on récupère la date et l'heure du jour
year = date.today().year
hour = datetime.now().hour
opened = False

# on vérifie si le marché est fermé
if hour > 7 or hour < 18:
    opened = True

# url de la page web à analyser avec le module html
response = requests.get('https://www.boursorama.com/bourse/indices/cours/1rPCAC/')
content = html.fromstring(response.content)

# on détermine le nombre de données à récupérer en fonction de l'état du marché (ouvert ou fermé)
index = 5 if opened else 6

# on définit les xpath. Les indices vont de 2 à 6 (5 si le marché est ouvert et donc que
date_xpath = '//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]/div[2]/div[1]/div[5]/div[2]/div[1]\
/div/div/table/thead/tr/th[{}]/text()'

# on crée la boucle qui va scraper les données
list_date = []
for i in range(2, index+1):
    result = get_data(content, date_xpath.format(i))
    list_date.append(result)
print(list_date)

# le cours de fermeture
closing = get_data(content, '//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]/div[2]/div[1]/div[5]/div[2]\
/div[1]/div/div/table/tbody/tr[1]/td[6]/text()')

# le cours d'ouverture
opening = get_data(content, '//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]/div[2]/div[1]/div[5]/div[2]\
/div[1]/div/div/table/tbody/tr[3]/td[6]/text()')

# le cours le plus haut
higher = get_data(content, '//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]/div[2]/div[1]/div[5]/div[2]\
/div[1]/div/div/table/tbody/tr[4]/td[6]/text()')

# le cours le plus bas
lower = get_data(content, '//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]/div[2]/div[1]/div[5]/div[2]\
/div[1]/div/div/table/tbody/tr[5]/td[6]/text()')

# on affiche les résultats
print(f"date :      {list_date[-1]}-{year}")
print(f"clôture :   {closing}")
print(f"ouverture : {opening}")
print(f"plus haut : {higher}")
print(f"plus bas :  {lower}")
