from base import Base
from sqlalchemy import Column, Integer, String

class RuanganModel(Base):
  __tablename__="ruangan"
  id = Column(Integer, primary_key=True)
  ruangan = Column(String(150), nullable=False)
  tipe_pc = Column(String(150), nullable=False)