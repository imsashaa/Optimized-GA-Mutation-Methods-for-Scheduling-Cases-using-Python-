import pandas as pd
from base import fetch
from models.JamMatkulModel import JamMatkulModel
from models.RuanganModel import RuanganModel
from models.MatkulPraktikumKelasModel import MatkulPraktikumKelasModel
from models.KelasPraktikumModel import KelasPraktikumModel
from models.KelasRegulerModel import KelasRegulerModel
from models.MatakuliahPraktikumModel import MatakuliahPraktikumModel

jam =  pd.DataFrame([(row.id, row.jam) for row in fetch(JamMatkulModel)], columns=['id', 'jam'])
kelas_praktikum =  pd.DataFrame([(row.id, row.nama_kelas, row.kelas_id) for row in fetch(KelasPraktikumModel)], columns=['id', 'nama_kelas', 'kelas_id'])
kelas_reguler =  pd.DataFrame([(row.id, row.kelas, row.angkatan) for row in fetch(KelasRegulerModel)], columns=['id', 'kelas', 'angkatan'])
ruangan = pd.DataFrame([(row.id, row.ruangan, row.tipe_pc) for row in fetch(RuanganModel)], columns=['id', 'ruangan', 'tipe_pc'])
matkul_kelas = pd.DataFrame([(row.id, row.matkul_id, row.kelas_praktikum_id) for row in fetch(MatkulPraktikumKelasModel)], columns=['id', 'matkul_id', 'kelas_praktikum_id'])
matkul_praktikum = pd.DataFrame([(row.id, row.matakuliah, row.tipe_pc) for row in fetch(MatakuliahPraktikumModel)], columns=['id', 'matakuliah', 'tipe_pc'])
hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat']

def createExcel(best_population, gen) : 
  
  def map_nama_jam(id_jam) : 
    return jam[jam['id'] == id_jam].head(1)['jam'].values[0]
  
  def map_nama_ruangan(id_ruangan) : 
    return ruangan[ruangan['id'] == id_ruangan].head(1)['ruangan'].values[0]
  
  def map_nama_kelas(id_kelas) :
    if (id_kelas != '') :
      kelas_id = matkul_kelas[matkul_kelas['id'] == id_kelas].head(1)['kelas_praktikum_id'].values[0]
      kelas_reguler_id = kelas_praktikum[kelas_praktikum['id'] == kelas_id].head(1)['kelas_id'].values[0]
      angkatan_kelas = kelas_reguler[kelas_reguler['id'] == kelas_reguler_id].head(1)['angkatan'].values[0]
      nama_kelas_praktikum = kelas_praktikum[kelas_praktikum['id'] == kelas_id].head(1)['nama_kelas'].values[0]
      return nama_kelas_praktikum + " " + str(angkatan_kelas)
    
    return ''
  
  def map_nama_matkul(id_kelas) :
    if (id_kelas != '') :
      matkul_id = matkul_kelas[matkul_kelas['id'] == id_kelas].head(1)['matkul_id'].values[0]
      nama_matkul = matkul_praktikum[matkul_praktikum['id'] == matkul_id].head(1)['matakuliah'].values[0]
      return nama_matkul
    
    return ''
    
  jadwal_hari = best_population['hari']
  jadwal_jam = list(map(map_nama_jam, best_population['jam']))
  jadwal_kelas = list(map(map_nama_kelas, best_population['kelas_praktikum']))
  jadwal_matkul = list(map(map_nama_matkul, best_population['kelas_praktikum']))
  jadwal_ruangan = list(map(map_nama_ruangan, best_population['ruangan']))
  
  new_jadwal = pd.DataFrame({
    'hari' : jadwal_hari,
    'ruangan': jadwal_ruangan,
    'jam' : jadwal_jam,
    'matkul' : jadwal_matkul,
    'kelas' : jadwal_kelas
  })
  with pd.ExcelWriter(f"result/gen{gen}-first.xlsx", engine='xlsxwriter') as writer:
    for row in hari : 
      new_jadwal[new_jadwal['hari'] == row].to_excel(writer, sheet_name=row, startrow=1, startcol=1, header=True)

def shuffleMatkulKelas(data_kelas) : 
  shuffled_data = data_kelas.sample(frac=1)
  return shuffled_data.reset_index(drop=True)

def shuffleJadwal(data_jadwal, len) : 
  shuffled_data = data_jadwal.sample(frac=1)
  return shuffled_data.head(len)
  
def createJamRuangan() : 
  return pd.DataFrame([{
    "jam": jam,
    "ruangan": room
  } for jam in jam['id'] for room in ruangan['id']])

def createJadwal() : 
  jam_ruangan = createJamRuangan()
  filtered_jam_by_day = pd.DataFrame([])
  for row in hari:
    if(row != 'jumat') :
      filtered_data = pd.DataFrame(jam_ruangan[jam_ruangan['jam'] <= 6])
      filtered_data['hari'] = row
      filtered_jam_by_day = pd.concat([filtered_jam_by_day, filtered_data], ignore_index=True)
    else :
      filtered_data = pd.DataFrame(jam_ruangan[(jam_ruangan['jam'] >= 7) &  (jam_ruangan['jam'] <= 10)])
      filtered_data['hari'] = row
      filtered_jam_by_day = pd.concat([filtered_jam_by_day, filtered_data], ignore_index=True)
  filtered_jam_by_day['kelas_praktikum'] = ''
  filtered_jam_by_day['error'] = False
  filtered_jam_by_day['id'] = [i for i in range(1, filtered_jam_by_day.shape[0]+1)]
  return filtered_jam_by_day

def insertMatkulToJadwal(jadwal, shuffled_jadwal, shuffled_matkul) : 
  # getting index from shuffled jadwal
  shuffle_jadwal_index = list(shuffled_jadwal.index.values)
  # inserting shuffled matkul to jadwal
  for index, dataShuffle in enumerate(shuffle_jadwal_index) :
    jadwal.loc[dataShuffle, 'kelas_praktikum'] = shuffled_matkul.loc[index, 'id']
  
  return jadwal
  
