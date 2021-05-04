from stockscraper import parsing_url, scraper

# on crée un dictionnaire prenant en valeur les xpath à scraper
x_path_dict = {'date_xpath': '//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]/div[2]/div[1]/div[5]/div[2]\
/div[1]/div/div/table/thead/tr/th[{}]/text()',
               'row_xpath': '//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]/div[2]/div[1]/div[5]/div[2]\
               /div[1]/div/div/table/tbody/tr[{}]/td[{}]/text()'}

# parsing des données
cac_content = parsing_url('https://www.boursorama.com/bourse/trackers/cours/1rTLVC/')
scraping_list_CAC = scraper(x_path_dict, cac_content)

lvc_content = parsing_url('https://www.boursorama.com/bourse/indices/cours/1rPCAC/')
scraping_list_LVC = scraper(x_path_dict, lvc_content)

bx4_content = parsing_url('https://www.boursorama.com/bourse/trackers/cours/1rTBX4/')
scraping_list_BX4 = scraper(x_path_dict, bx4_content)
