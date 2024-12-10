from function.jadwal import insertMatkulToJadwal, shuffleJadwal, shuffleMatkulKelas, hari, createJadwal
from function.fitness import checkJamReguler, checkRuangan, checkErrorHari
import pandas as pd
import random
import math

def createPopulation(jadwal, matkul, populationLen) : 
  
  population_jadwal = [jadwal.copy() for _ in range(populationLen)]
  
  def mapPopulationWithMatkul(jadwal) : 
    shufled_jadwal = shuffleJadwal(jadwal, matkul.shape[0])
    shuffled_matkul = shuffleMatkulKelas(matkul)
    fix_jadwal = insertMatkulToJadwal(jadwal, shuffled_jadwal=shufled_jadwal, shuffled_matkul=shuffled_matkul)
    return fix_jadwal

  population_with_matkul = list(map(mapPopulationWithMatkul, population_jadwal))
  
  return population_with_matkul

def populationFitness(populations) :
  pop_idx = []
  nilai_fitness = []
  nilai_error = []
  total_kelas = []
  for index, row in enumerate(populations) :
    jadwal_kelas_only = row[row['kelas_praktikum'] != '']
    check_jam_reguler = checkJamReguler(row, jadwal_kelas_only)
    check_ruangan = checkRuangan(check_jam_reguler, jadwal_kelas_only)
    check_error_hari = checkErrorHari(check_ruangan)
    pop_idx.append(index)
    nilai_fitness.append((jadwal_kelas_only.shape[0] - check_error_hari) / jadwal_kelas_only.shape[0] * 100)
    total_kelas.append(jadwal_kelas_only.shape[0])
    nilai_error.append(check_error_hari)
    
  return pd.DataFrame({
    'idx_pop' : pop_idx,
    'fitness' : nilai_fitness,
    'nilai_error' : nilai_error,
    'total_kelas' : total_kelas
  })

def selection(population_fitness, populations) :
  sorted_fitness = population_fitness.sort_values(by='fitness', ascending=False)
  # fetch 6 data from sorted_fitness
  best_mating_pool_index = list(sorted_fitness['idx_pop'])
  return [populations[i] for i in best_mating_pool_index], sorted_fitness

def newGen(best_population, populationLen, sort_fitness) : 
  
  def crossOver(parentA, parentB) :
    only_kelas_parentA = parentA[(parentA['kelas_praktikum'] != '') & (parentA['error'] == True)].sort_values(by='kelas_praktikum', ascending=True)
    only_kelas_parentB = parentB[parentB['kelas_praktikum'] != ''].sort_values(by='kelas_praktikum', ascending=True)
    
    combine = []
    for index, row in only_kelas_parentA.iterrows() : 
      check_kelas = only_kelas_parentB[only_kelas_parentB['kelas_praktikum'] == row['kelas_praktikum']].head(1)
      if(check_kelas.shape[0] != 0) :
        if(check_kelas['error'].values[0] == False) :
          combine.append({
            'parent_a' : row['id'],
            'parent_b' : check_kelas['id'].values[0],
            'kelas_praktikum' : row['kelas_praktikum'],
          })  
        
    child = parentA.copy()
    
    # print('total combine : ', len(combine))
    # print('kurang combine : ', child[child['kelas_praktikum'] != ''].shape[0] - len(combine), '\n')
    for row in combine : 
      child.loc[row['parent_a'] - 1, 'kelas_praktikum'] = ''
      if(child.iloc[row['parent_b'] - 1]['kelas_praktikum'] != '') :
        replace_data = child[child['kelas_praktikum'] == ''].sample(frac=1).head(1)
        child.loc[replace_data['id'].values[0] - 1, 'kelas_praktikum'] = child.iloc[row['parent_b'] - 1]['kelas_praktikum']
      child.loc[row['parent_b'] - 1, 'kelas_praktikum'] = row['kelas_praktikum']
      
    # print('total pas crossover : ' ,child[child['kelas_praktikum'] != ''].shape[0], '\n')
    return child
   

  def mutasi(child) :
    mutate_rate = random.random()
    if(mutate_rate <= 0.03) :
      child_error_only = child[(child['kelas_praktikum'] != '') & (child['error'] == True)]
      child_no_class = child[(child['kelas_praktikum'] == '')].sample(frac=1)
      if(child_error_only.shape[0] > 0) :
        rand_jml_mutate = random.randint(1, child_error_only.shape[0])
        element_picked = child_error_only.head(rand_jml_mutate).sample(frac=1).reset_index(drop=True)
        element_for_replace_picked = child_no_class.head(rand_jml_mutate).reset_index(drop=True)
        
        for index, row in element_for_replace_picked.iterrows() : 
          error_element = element_picked.iloc[index]
          child.at[error_element['id'] - 1, 'kelas_praktikum'] = ''
          child.at[row['id'] - 1, 'kelas_praktikum'] = error_element['kelas_praktikum']
        
    return child
  
  next_gen = []
  for i in range(populationLen) :
    # parentA = random.randint(0, len(best_population)-1)
    parentB = random.randint(0, len(best_population)-1)
    
    child = crossOver(best_population[0], best_population[parentB])
    mutate_child = mutasi(child)
    child['error'] = False
    next_gen.append(child)
  
  return next_gen

def genetic(populations, param_best_fitness, gen, popLen) : 
  
  populations_fitness = populationFitness(populations)
  best_population, sort_fitness = selection(populations_fitness, populations)
  
  if (gen == 1000) :
    return sort_fitness
  
  if (param_best_fitness == -1) or (param_best_fitness < sort_fitness.iloc[0]['fitness']) :
    param_best_fitness = sort_fitness.iloc[0]['fitness']
  
  if(param_best_fitness == 100) :
    first = sort_fitness.iloc[0]['idx_pop'].astype('int')  
    return best_population[first], gen
  
  print(gen, param_best_fitness, sort_fitness.iloc[0]['nilai_error'])
  population_next_gen = newGen(best_population, popLen, sort_fitness)
  new_gen = gen+1
  best_fitness, best_gen = genetic(population_next_gen, param_best_fitness=param_best_fitness, gen=new_gen, popLen=popLen)
  
  return best_fitness, best_gen
  