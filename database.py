from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///database.db')
engine.connect()

Base = declarative_base()


class Px1(Base):
    __tablename__ = 'px1'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    closing = Column(Integer)
    opening = Column(Integer)
    higher = Column(Integer)
    lower = Column(Integer)

    def __repr__(self):
        return f"le {self.date} le CAC a clôturé à {self.closing}. Il avait ouvert à {self.opening} pour atteindre un plus haut à {self.higher} et un plus bas à {self.lower}"

# la création de la base doit se trouver après la déclaration de la Table (via la classe)
Base.metadata.create_all(engine)
