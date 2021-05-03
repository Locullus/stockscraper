from stockscraper import parsing_url, scraper

# on récupère le contenu parsé d'une page html
cac_content = parsing_url('https://www.boursorama.com/bourse/indices/cours/1rPCAC/')

scraping_list_CAC = scraper(cac_content)
for element in scraping_list_CAC:
    print(element)

# on va pouvoir scraper le LVC et le BX4 en changeant simplement l'url de content
# lvc_content = parsing_url('...')
# scraping_list_LVC = scraper(lvc_content)
