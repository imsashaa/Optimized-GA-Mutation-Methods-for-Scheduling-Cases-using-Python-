from base import Base
from sqlalchemy import Column, Integer, String

class JamMatkulRegulerModel(Base):
  __tablename__="jam_matkul_reguler"
  id = Column(Integer, primary_key=True)
  hari = Column(String(150), nullable=False)
  kelas_id = Column(Integer, nullable=False)
  jam_id = Column(Integer, nullable=False)