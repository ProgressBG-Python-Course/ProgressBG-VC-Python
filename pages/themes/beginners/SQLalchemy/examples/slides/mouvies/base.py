from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

\engine = create_engine('sqlite:///sqlalchemy_mouvies.db')
Session = sessionmaker(bind=engine)

Base = declarative_base()