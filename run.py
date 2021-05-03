from sqlalchemy.orm import sessionmaker
from database import engine, CAC

from scraper import scraping_list

Session = sessionmaker(bind=engine)

# on ouvre une session pour récupérer la date la plus récente de la base de données
session = Session()
last_high = session.query(CAC.date).order_by(CAC.date.desc()).first()
print(f"La date la plus récente dans la base de donnée : {last_high}")
session.close()

# on ouvre une nouvelle session pour peupler la base de données avec les données scrapées
session = Session()
for element in scraping_list:
    data = CAC(data=element[0], closing=element[1], opening=element[2], higher=element[3], lower=element[4])
    session.add(data)
session.commit()
