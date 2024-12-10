from models.JamMatkulRegulerModel import JamMatkulRegulerModel
from function.jadwal import hari, kelas_praktikum, kelas_reguler, matkul_kelas, matkul_praktikum, ruangan
import pandas as pd
from base import fetch

jam_reguler =  pd.DataFrame([(row.id, row.hari ,row.jam_id, row.kelas_id) for row in fetch(JamMatkulRegulerModel)], columns=['id','hari','jam_id', 'kelas_id'])

def checkJamReguler(jadwal_praktikum, jadwal_kelas_only):
  # Checking Jam Reguler
  for index, row in jadwal_kelas_only.iterrows() :
    find_matkul_kelas = matkul_kelas[matkul_kelas['id'] == row['kelas_praktikum']].iloc[0]
    find_kelas_praktikum = kelas_praktikum[kelas_praktikum['id'] == find_matkul_kelas['kelas_praktikum_id']].iloc[0]
    find_kelas_reguler = kelas_reguler[kelas_reguler['id'] == find_kelas_praktikum['kelas_id']].iloc[0]
    
    check_jadwal = jam_reguler[(jam_reguler['hari'] == row['hari']) & (jam_reguler['jam_id'] == row['jam']) & (jam_reguler['kelas_id'] == find_kelas_reguler['id'])]
    if(check_jadwal.shape[0] > 0) :
      jadwal_praktikum.at[index, 'error'] = True
      
  return jadwal_praktikum

def checkRuangan(jadwal_praktikum_checked, jadwal_kelas_only) :
  # checking Ruangan
  for index, row in jadwal_kelas_only.iterrows() :
    find_matkul_kelas = matkul_kelas[matkul_kelas['id'] == row['kelas_praktikum']].iloc[0]
    find_matkul_praktikum = matkul_praktikum[matkul_praktikum['id'] == find_matkul_kelas['matkul_id']].iloc[0]
    check_ruangan = ruangan[(ruangan['id'] == row['jam']) & (ruangan['tipe_pc'] == find_matkul_praktikum['tipe_pc'])]
    if(check_ruangan.shape[0] > 0) :
      jadwal_praktikum_checked.at[index, 'error'] = True
      
  return jadwal_praktikum_checked

def checkErrorHari(jadwal_all_checked) :
  def map_hari(fill_day) :
    return jadwal_all_checked[(jadwal_all_checked['hari'] == fill_day) & (jadwal_all_checked['error'] == True)].shape[0]
  error_day = map(map_hari, hari)
  return sum(list(error_day))

