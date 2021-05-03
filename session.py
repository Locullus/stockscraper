from sqlalchemy.orm import sessionmaker
from database import engine, CAC

from scraper import scraping_list_CAC

Session = sessionmaker(bind=engine)

# on ouvre une session pour récupérer la date la plus récente de la base de données
session = Session()
last_high = str(session.query(CAC.date).order_by(CAC.date.desc()).first())
print(f"La date la plus récente dans la base de donnée : {last_high}")
session.close()

# on crée une liste des éléments à ajouter à la base de données dans l'ordre chronologique
committing_list = []
for element in scraping_list_CAC:
    if element[0] not in last_high or last_high is None:
        committing_list.insert(0, element)
    else:
        break
for element in committing_list:
    print(element)

# on ouvre une nouvelle session pour peupler la base de données avec les éléments de la liste précédente
session = Session()
for element in committing_list:
    data = CAC(date=element[0], closing=element[1], opening=element[2], higher=element[3], lower=element[4])
    session.add(data)
session.commit()

# pour récupérer toutes les entrées de la table CAC
session = Session()
datas = session.query(CAC).all()
print("ceci est écrit depuis le module session.py :")
print(datas)
session.close()

# on ouvre une session pour récupérer la date la plus récente de la base de données
session = Session()
new_last_high = str(session.query(CAC.date).order_by(CAC.date.desc()).first())
print(f"La date la plus récente après la mise à jour de la base de donnée : {new_last_high}")
session.close()

"""
# pour supprimer toute les entrées depuis l'indice 4 de la table CAC
session = Session()
session.query(CAC).filter(CAC.id >= 6).delete()
session.commit()
session.close()

"""
