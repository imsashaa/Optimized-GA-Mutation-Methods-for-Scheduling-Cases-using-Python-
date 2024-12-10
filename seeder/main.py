import pandas as pd
from models.JamMatkulModel import JamMatkulModel
from models.RuanganModel import RuanganModel
from models.MatakuliahPraktikumModel import MatakuliahPraktikumModel
from models.KelasRegulerModel import KelasRegulerModel
from models.KelasPraktikumModel import KelasPraktikumModel
from models.MatkulPraktikumKelasModel import MatkulPraktikumKelasModel
from models.JamMatkulRegulerModel import JamMatkulRegulerModel
from base import create

jamDF = pd.read_excel('seeder\\initdata\\jam.xlsx')

for jam in range(jamDF.shape[0]) : 
  createData = JamMatkulModel(jam=jamDF.iloc[jam].Jam)
  create(createData)
  
ruanganDF = pd.read_excel('seeder\\initdata\\ruangan.xlsx')

for ruangan in range(ruanganDF.shape[0]) : 
  ruang = ruanganDF.iloc[ruangan]
  createData = RuanganModel(ruangan=ruang.Ruangan, tipe_pc=ruang.PC)
  create(createData)

matakuliahDF = pd.read_excel('seeder\\initdata\\matakuliah.xlsx')

for matkul_i in range(matakuliahDF.shape[0]) : 
  matkul = matakuliahDF.iloc[matkul_i]
  createData = MatakuliahPraktikumModel(matakuliah=matkul['Mata Kuliah'], tipe_pc=matkul['PC'])
  create(createData)

kelasDF = pd.read_excel('seeder\\initdata\\kelas.xlsx')

for kelas_i in range(kelasDF.shape[0]) : 
  kelas_data = kelasDF.iloc[kelas_i]
  createData = KelasRegulerModel(kelas=kelas_data['Kelas'], angkatan=kelas_data['Angkatan'])
  create(createData)
  
praktikumKelasDF = pd.read_excel('seeder\\initdata\\praktikum_kelas.xlsx')

for row in range(praktikumKelasDF.shape[0]) : 
  praktikum_kelas = praktikumKelasDF.iloc[row]
  createData = KelasPraktikumModel(nama_kelas=praktikum_kelas['Kelas'], kelas_id=praktikum_kelas['Kelas Id'])
  create(createData)
  
matkulKelasDf = pd.read_excel('seeder\\initdata\\matkul_kelas.xlsx')

for row in range(matkulKelasDf.shape[0]) : 
  matkul_kelas = matkulKelasDf.iloc[row]
  createData = MatkulPraktikumKelasModel(matkul_id=matkul_kelas['matkul'], kelas_praktikum_id=matkul_kelas['kelas'])
  create(createData)

jamMatkulRegDf = pd.read_excel('seeder\\initdata\\jam_matkul_reguler.xlsx')

for row in range(jamMatkulRegDf.shape[0]) : 
  jam_matkul_reg = jamMatkulRegDf.iloc[row]
  createData = JamMatkulRegulerModel(hari=jam_matkul_reg['hari'],jam_id=jam_matkul_reg['jam_id'], kelas_id=jam_matkul_reg['kelas_id'])
  create(createData)