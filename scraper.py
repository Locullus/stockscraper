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

# on définit les xpath
date_xpath = '//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]/div[2]/div[1]/div[5]/div[2]/div[1]\
/div/div/table/thead/tr/th[{}]/text()'

row_xpath = '//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]/div[2]/div[1]/div[5]/div[2]\
/div[1]/div/div/table/tbody/tr[{}]/td[{}]/text()'

# on détermine le nombre de données à récupérer en fonction de l'état du marché (ouvert ou fermé)
index = 6 if opened else 7

# on crée la boucle qui va scraper les dates
date_list = [(get_data(content, date_xpath.format(i))+'-'+str(year)) for i in range(2, index)]
print(date_list)

# boucle qui va scraper les cours de fermeture  1 6
closing_list = [get_data(content, row_xpath.format(1, i)) for i in range(2, index)]
print(closing_list)

# boucle qui va scraper les cours d'ouverture   3 6
opening_list = [get_data(content, row_xpath.format(3, i)) for i in range(2, index)]
print(opening_list)

# boucle qui va scraper les plus haut   4 6
higher_list = [get_data(content, row_xpath.format(4, i)) for i in range(2, index)]
print(higher_list)

# boucle qui va scraper les plus bas    5 6
lower_list = [get_data(content, row_xpath.format(5, i)) for i in range(2, index)]
print(lower_list)

# on affiche les résultats
print(f"date :      {date_list[-1]}")
print(f"clôture :   {closing_list[-1]}")
print(f"ouverture : {opening_list[-1]}")
print(f"plus haut : {higher_list[-1]}")
print(f"plus bas :  {lower_list[-1]}")
