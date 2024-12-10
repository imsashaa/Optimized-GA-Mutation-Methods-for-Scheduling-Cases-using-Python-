from base import Base
from sqlalchemy import Column, Integer

class MatkulPraktikumKelasModel(Base):
  __tablename__="matkul_praktikum_kelas"
  id = Column(Integer, primary_key=True)
  matkul_id = Column(Integer, nullable=False)
  kelas_praktikum_id = Column(Integer, nullable=False)