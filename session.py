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
    inner_session = Session()
    inner_last_high = str(inner_session.query(TABLE.date).order_by(TABLE.id.desc()).first())
    print(f"La date la plus récente dans la base de donnée {TABLE.__tablename__}: {inner_last_high}")
    inner_session.close()

    # on crée une liste des éléments à ajouter à la base de données dans l'ordre chronologique
    inner_committing_list = []
    for inner_element in scraping_list:
        if inner_element[0] not in inner_last_high or inner_last_high is None:
            inner_committing_list.insert(0, inner_element)
        else:
            break
    for inner_element in inner_committing_list:
        print(inner_element)

    # on ouvre une nouvelle session pour peupler la base de données avec les éléments de la liste précédente
    inner_session = Session()
    for inner_element in inner_committing_list:
        inner_data = TABLE(
            date=inner_element[0],
            closing=inner_element[1],
            opening=inner_element[2],
            higher=inner_element[3],
            lower=inner_element[4]
        )
        inner_session.add(inner_data)
    inner_session.commit()

    # pour récupérer toutes les entrées d'une TABLE
    inner_session = Session()
    inner_datas = inner_session.query(TABLE).all()
    print(inner_datas)
    inner_session.close()


# ====================== update des Stocks scrapées ======================
stocks_db_update(CAC, scraping_list_CAC)
stocks_db_update(LVC, scraping_list_LVC)
stocks_db_update(BX4, scraping_list_BX4)
