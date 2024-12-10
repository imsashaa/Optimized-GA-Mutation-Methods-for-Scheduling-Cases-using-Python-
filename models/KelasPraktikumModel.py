from base import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class KelasPraktikumModel(Base):
  __tablename__="kelas_praktikum"
  id = Column(Integer, primary_key=True)
  nama_kelas = Column(String(150), nullable=False)
  kelas_id = Column(Integer, ForeignKey("kelas_reguler.id"), nullable=True)
  