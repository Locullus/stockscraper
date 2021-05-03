# ====================== fonctions =====================
def get_data(content, xpath):
    """
    fonction qui récupère une liste de contenus ciblée par un xpath et en retourne le premier élément
    La méthode xpath() parse un objet et renvoit une liste contenant toutes les occurences du chemin passé en argument
    """
    return [x.strip() for x in content.xpath(xpath)][0]
