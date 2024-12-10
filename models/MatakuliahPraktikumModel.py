from base import Base
from sqlalchemy import Column, Integer, String

class MatakuliahPraktikumModel(Base):
  __tablename__ = "matakuliah_praktikum"
  id = Column(Integer, primary_key=True)
  matakuliah = Column(String(150), nullable=False)
  tipe_pc = Column(String(150), nullable=False)