from stockscraper import parsing_url, scraper
from session import Session, stocks_db_update
from database import CAC, LVC, BX4

# on crée un dictionnaire prenant en valeur les xpath à scraper
base = '//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]'

CAC_xpath_dict = {'date_xpath': base + '/div[2]/div[1]/div[5]/div[2]/div[1]/div/div/table/thead/tr/th[{}]/text()',
                  'row_xpath': base + '/div[2]/div[1]/div[5]/div[2]/div[1]/div/div/table/tbody/tr[{}]/td[{}]/text()'}

STOCKS_xpath_dict = {'date_xpath': base + '/div[1]/div[1]/div[6]/div[2]/div[1]/div/div/table/thead/tr/th[{}]/text()',
                     'row_xpath': base + '/div[1]/div[1]/div[6]/div[2]/div[1]/div/div/table/tbody/tr[{}]/td[{}]/text()'}

# on scrape les données des valeurs CAC, LVC et BX4 pour mettre à jour la base de données
cac_content = parsing_url('https://www.boursorama.com/bourse/indices/cours/1rPCAC/')
scraping_list_CAC = scraper(CAC_xpath_dict, cac_content)
stocks_db_update(CAC, scraping_list_CAC)
print("les données de SCRAPING_LIST_CAC sont affichées pour l'exemple :")
for element in scraping_list_CAC:
    print(element)
print("\n")

lvc_content = parsing_url('https://www.boursorama.com/bourse/trackers/cours/1rTLVC/')
scraping_list_LVC = scraper(STOCKS_xpath_dict, lvc_content)
stocks_db_update(LVC, scraping_list_LVC)

bx4_content = parsing_url('https://www.boursorama.com/bourse/trackers/cours/1rTBX4/')
scraping_list_BX4 = scraper(STOCKS_xpath_dict, bx4_content)
stocks_db_update(BX4, scraping_list_BX4)

# on interroge la base de données et on affiche le résultat
session = Session()
update_CAC = session.query(CAC).all()
print("On affiche le contenu de la TABLE CAC :")
print(update_CAC)
