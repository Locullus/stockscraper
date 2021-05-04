from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///database.db')
engine.connect()

Base = declarative_base()


class CAC(Base):

    """
    classe gérant une TABLE  de la base de données.

    Ici la classe étendant Base = declarative_Base(), deux paramètres sont obligatoires :
    - le nom de la table __tablename__
    - une Column() avec une primary_key
    """

    __tablename__ = 'cac'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    closing = Column(Integer)
    opening = Column(Integer)
    higher = Column(Integer)
    lower = Column(Integer)

    def __repr__(self):
        return f"""
            le {self.date} :
            le CAC a clôturé à {self.closing}
            Il avait ouvert à {self.opening}
            Il a atteint {self.higher} au plus haut
            Au plus bas il a touché {self.lower}
                """


class LVC(Base):

    __tablename__ = 'lvc'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    closing = Column(Integer)
    opening = Column(Integer)
    higher = Column(Integer)
    lower = Column(Integer)

    def __repr__(self):
        return f"""
            le {self.date} :
            le LVC a clôturé à {self.closing}
            Il avait ouvert à {self.opening}
            Il a atteint {self.higher} au plus haut
            Au plus bas il a touché {self.lower}
                """


class BX4(Base):

    __tablename__ = 'bx4'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    closing = Column(Integer)
    opening = Column(Integer)
    higher = Column(Integer)
    lower = Column(Integer)

    def __repr__(self):
        return f"""
            le {self.date} :
            le BX4 a clôturé à {self.closing}
            Il avait ouvert à {self.opening}
            Il a atteint {self.higher} au plus haut
            Au plus bas il a touché {self.lower}
                """


# la création de la base doit se trouver après la déclaration de la Table (via la classe)
Base.metadata.create_all(engine)
