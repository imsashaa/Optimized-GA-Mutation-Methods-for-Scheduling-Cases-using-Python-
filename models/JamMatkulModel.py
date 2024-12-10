from base import Base
from sqlalchemy import Column, Integer, String

class JamMatkulModel(Base):
  __tablename__ = 'jam_matkul'
  id = Column(Integer, primary_key=True)
  jam = Column(String(150), nullable=False)
  