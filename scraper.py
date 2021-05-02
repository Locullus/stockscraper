from lxml import html
import requests
from datetime import date

year = date.today().year

# on utilise requests.get pour récupérer la page web et on la parse avec le module html
page = requests.get('https://www.boursorama.com/bourse/indices/cours/1rPCAC/')

# on utilise page.content plutôt que page.text parce que html.fromstring attend implicitement des bytes en entrée
content = html.fromstring(page.content)

# ============================================================================


def get_data(xpath):
    """
    fonction qui récupère une liste de contenus ciblée par un xpath et en retourne le premier élément

    La méthode xpath() parse un objet et renvoit une liste contenant toutes les occurences du chemin passé en argument
    """
    return [x.strip() for x in content.xpath(xpath)][0]


# la date
date = get_data('//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]/div[2]/div[1]/div[5]/div[2]/div[1]\
/div/div/table/thead/tr/th[6]/text()')

# le cours de fermeture
closing = get_data('//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]/div[2]/div[1]/div[5]/div[2]/div[1]\
/div/div/table/tbody/tr[1]/td[6]/text()')

# le cours d'ouverture
opening = get_data('//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]/div[2]/div[1]/div[5]/div[2]/div[1]\
/div/div/table/tbody/tr[3]/td[6]/text()')

# le cours le plus haut
higher = get_data('//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]/div[2]/div[1]/div[5]/div[2]/div[1]\
/div/div/table/tbody/tr[4]/td[6]/text()')

# le cours le plus bas
lower = get_data('//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]/div[2]/div[1]/div[5]/div[2]/div[1]\
/div/div/table/tbody/tr[5]/td[6]/text()')

# on affiche les résultats
print(f"date :      {date}-{year}")
print(f"clôture :   {closing}")
print(f"ouverture : {opening}")
print(f"plus haut : {higher}")
print(f"plus bas :  {lower}")

"""
# code tiré de https://oxylabs.io/blog/lxml-tutorial#Handling
response = requests.get('http://books.toscrape.com/')
print(response.text)

# idem
response = requests.get('https://en.wikipedia.org/wiki/List_of_countries_by_population_in_2010')
print(response.text)

tree = html.fromstring(response.text)
countries = tree.xpath('//span[@class="flagicon"]')
print(countries)
for country in countries:
    print(country.xpath('./following-sibling::a/text()')[0])
"""
