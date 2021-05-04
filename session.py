from sqlalchemy.orm import sessionmaker
from database import engine, CAC, LVC, BX4

from scraper import scraping_list_CAC, scraping_list_LVC, scraping_list_BX4

Session = sessionmaker(bind=engine)


def stocks_db_update(TABLE, scraping_list):
    """
    fonction qui met à jour une table de la base de données
    :param TABLE: la TABLE à mettre à jour
    :param scraping_list: la liste des éléments à insérer
    :return: une TABLE de la BDD complétée avec les dernières données disponibles
    """
    # on ouvre une session pour récupérer la date la plus récente de la base de données
    session = Session()
    last_high = str(session.query(TABLE.date).order_by(TABLE.id.desc()).first())
    print(f"La date la plus récente dans la base de donnée {TABLE.__tablename__}: {last_high}")
    session.close()

    # on crée une liste des éléments à ajouter à la base de données dans l'ordre chronologique
    committing_list = []
    for element in scraping_list:
        if element[0] not in last_high or last_high is None:
            committing_list.insert(0, element)
        else:
            break
    for element in committing_list:
        print(element)

    # on ouvre une nouvelle session pour peupler la base de données avec les éléments de la liste précédente
    session = Session()
    for element in committing_list:
        data = TABLE(
            date=element[0],
            closing=element[1],
            opening=element[2],
            higher=element[3],
            lower=element[4]
        )
        session.add(data)
    session.commit()

    # pour récupérer toutes les entrées d'une TABLE
    session = Session()
    datas = session.query(TABLE).all()
    print(datas)
    session.close()


# ====================== update des Stocks scrapées ======================
stocks_db_update(CAC, scraping_list_CAC)
stocks_db_update(LVC, scraping_list_LVC)
stocks_db_update(BX4, scraping_list_BX4)
