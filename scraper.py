from stockscraper import parsing_url, scraper

# on crée un dictionnaire prenant en valeur les xpath à scraper
x_path_dict = {'date_xpath': '//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]/div[2]/div[1]/div[5]/div[2]\
/div[1]/div/div/table/thead/tr/th[{}]/text()',
               'row_xpath': '//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]/div[2]/div[1]/div[5]/div[2]\
               /div[1]/div/div/table/tbody/tr[{}]/td[{}]/text()'}

# on récupère le contenu parsé d'une page html
cac_content = parsing_url('https://www.boursorama.com/bourse/indices/cours/1rPCAC/')

scraping_list_CAC = scraper(x_path_dict, cac_content)
for element in scraping_list_CAC:
    print(element)

# on va pouvoir scraper le LVC et le BX4 en changeant simplement l'url de content
# lvc_content = parsing_url('...')
# scraping_list_LVC = scraper(lvc_content)
