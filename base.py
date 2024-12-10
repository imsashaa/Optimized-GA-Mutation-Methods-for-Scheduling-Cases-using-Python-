from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

session_maker = sessionmaker(bind=create_engine('mysql://root:@localhost/jadwal_praktikum'))

def create(model) : 
  with session_maker() as session: 
    session.add(model)
    session.commit()    

def fetch(model) : 
  session = session_maker()
  try:
      datas = session.query(model).all()
      return datas
  except Exception as e:
      print(f"Error fetching data: {e}")
  finally:
      session.close()




