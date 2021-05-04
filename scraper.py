from stockscraper import parsing_url, scraper

# on crée un dictionnaire prenant en valeur les xpath à scraper
CAC_xpath_dict = {'date_xpath': '//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]/div[2]/div[1]/\
div[5]/div[2]/div[1]/div/div/table/thead/tr/th[{}]/text()',
                  'row_xpath': '//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]/div[2]/div[1]\
                   /div[5]/div[2]/div[1]/div/div/table/tbody/tr[{}]/td[{}]/text()'}
STOCKS_xpath_dict = {'date_xpath': '//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]/div[1]/div[1]\
/div[6]/div[2]/div[1]/div/div/table/thead/tr/th[{}]/text()',
                     'row_xpath': '//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]/div[1]/div[1]\
                      /div[6]/div[2]/div[1]/div/div/table/tbody/tr[{}]/td[{}]/text()'}

# on scrape les données des valeurs CAC, LVC et BX4 et on les liste
cac_content = parsing_url('https://www.boursorama.com/bourse/indices/cours/1rPCAC/')
scraping_list_CAC = scraper(CAC_xpath_dict, cac_content)
print("SCRAPING_LIST_CAC")
for element in scraping_list_CAC:
    print(element)
print("\n")

lvc_content = parsing_url('https://www.boursorama.com/bourse/trackers/cours/1rTLVC/')
scraping_list_LVC = scraper(STOCKS_xpath_dict, lvc_content)
print("SCRAPING_LIST_LVC")
for element in scraping_list_LVC:
    print(element)
print("\n")

bx4_content = parsing_url('https://www.boursorama.com/bourse/trackers/cours/1rTBX4/')
scraping_list_BX4 = scraper(STOCKS_xpath_dict, bx4_content)
print("SCRAPING_LIST_BX4")
for element in scraping_list_BX4:
    print(element)
print("\n")
