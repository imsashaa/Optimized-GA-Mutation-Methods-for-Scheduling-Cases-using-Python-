from base import fetch
import pandas as pd
from function.jadwal import createJadwal, matkul_kelas, createExcel
from function.genetika import createPopulation, genetic

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

popLen = 30

jadwal = createJadwal()
temp_best_fitness = -1
gen = 1
populations = createPopulation(jadwal, matkul_kelas, popLen)
best_popoulation, gen = genetic(populations=populations, param_best_fitness=temp_best_fitness, gen=gen, popLen=popLen)
createExcel(best_population=best_popoulation, gen=gen)

print("done")