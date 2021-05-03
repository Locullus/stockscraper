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

# on crée les boucles qui vont scraper les différentes données
date_list = [(get_data(content, date_xpath.format(i))+'-'+str(year)) for i in range(2, index)]
closing_list = [get_data(content, row_xpath.format(1, i)) for i in range(2, index)]
opening_list = [get_data(content, row_xpath.format(3, i)) for i in range(2, index)]
higher_list = [get_data(content, row_xpath.format(4, i)) for i in range(2, index)]
lower_list = [get_data(content, row_xpath.format(5, i)) for i in range(2, index)]

# on crée la liste des données scrapées que l'on enverra à la base de données
length = len(date_list)
scraping_list = [[date_list[i], closing_list[i], opening_list[i], higher_list[i], lower_list[i]] for i in range(length)]

# on inverse la liste pour qu'elle fournisse les dates de la plus récente à la plus ancienne
# ceci va permettre de mettre à jour la base uniquementles avec les éléments les plus récents
scraping_list.reverse()

