import csv
from os import path
import numpy as np

print path.dirname(__file__)
plafonds = []
with open(path.join(path.dirname(__file__),'plafonds.csv')) as csv_file:
   csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
   #csv_reader.next()

   for row in csv_reader:
       pt_charge = int(row[0])
       plafonds.append(np.asarray(map(lambda x : int(x), row[1:])))

plafonds = np.asarray(plafonds)
def get_plafond(point_charge):
	return np.transpose(plafonds[point_charge.astype(int)])
