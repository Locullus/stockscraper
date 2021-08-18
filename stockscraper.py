import requests
from lxml import html
from datetime import datetime, date


def parsing_url(url):
    """
    fonction qui convertit en string le contenu renvoyé par une requête à une url
    :param url: url de la page à parser
    :return: le contenu parsé d'un document html
    """
    response = requests.get(url)
    content = html.fromstring(response.content)
    return content


def get_data(content, xpath):
    """
    fonction qui récupère une liste de contenus ciblée par un xpath et en retourne le premier élément
    :param content: le contenu parsé d'un document html
    :param xpath: le chemin d'accès à un élément ciblé
    :return: string
    """
    return [x.strip() for x in content.xpath(xpath)][0]


def scraper(xpath_dict, content):
    """
    fonction qui analyse un page html pour récupérer les valeurs d'un sous-jacent depuis leur xpath
    :param xpath_dict: dictionnaire contenant les x_path des contenus recherchés
    :param content: la page parsée
    :return: une liste de string [date, closing, opening, higher, lower]
    """
    # on récupère la date et l'heure du jour et on initialise l'état du marché à fermé
    year = date.today().year
    hour = datetime.now().hour
    opened = False

    # on définit les xpath
    date_xpath = xpath_dict['date_xpath']
    row_xpath = xpath_dict['row_xpath']

    # on vérifie si le marché est ouvert
    if 7 < hour < 19:
        opened = True

    # on détermine le nombre de données à récupérer en fonction de l'état du marché (ouvert ou fermé)
    index = 6 if opened else 7

    # on crée les boucles qui vont scraper les différentes données
    date_list = [(get_data(content, date_xpath.format(i)) + '-' + str(year)) for i in range(2, index)]
    closing_list = [get_data(content, row_xpath.format(1, i)) for i in range(2, index)]
    opening_list = [get_data(content, row_xpath.format(3, i)) for i in range(2, index)]
    higher_list = [get_data(content, row_xpath.format(4, i)) for i in range(2, index)]
    lower_list = [get_data(content, row_xpath.format(5, i)) for i in range(2, index)]

    # on crée la liste des données scrapées que l'on enverra à la base de données
    length = len(date_list)
    scraping_list = [[date_list[i], closing_list[i], opening_list[i], higher_list[i],
                      lower_list[i]] for i in range(length)]

    # on inverse la liste pour qu'elle fournisse les dates de la plus récente à la plus ancienne
    # ceci va permettre de mettre à jour la base uniquementles avec les éléments les plus récents
    scraping_list.reverse()
    return scraping_list

# le 18/08, la dernière entrée dans la base de données a l'id n°(82,)
