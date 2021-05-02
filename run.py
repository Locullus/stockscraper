from sqlalchemy.orm import sessionmaker
from database import engine, Px1

Session = sessionmaker(bind=engine)

# on ouvre une session une fois la base créée, on fait les requêtes 
session = Session()

last_high = session.query(Px1.date).order_by(Px1.date.desc()).first()

session.close()

print(f"La date la plus récente dans la base de donnée : {last_high}")