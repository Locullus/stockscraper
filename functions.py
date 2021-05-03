import requests
from lxml import html


# ====================== fonctions =====================

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
