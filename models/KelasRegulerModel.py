from base import Base
from sqlalchemy import Column, Integer, String

class KelasRegulerModel(Base): 
  __tablename__="kelas_reguler"
  id = Column(Integer, primary_key=True)
  kelas = Column(String(150), nullable=False)
  angkatan = Column(String(150), nullable=False)