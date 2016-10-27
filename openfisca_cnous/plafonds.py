import csv
from os import path

print path.dirname(__file__)	
plafonds = {}
with open(path.join(path.dirname(__file__),'plafonds.csv')) as csv_file:
   csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
   #csv_reader.next()

   for row in csv_reader:
       pt_charge = int(row[0])
       plafonds[pt_charge] = map(lambda x : int(x), row[1:])

def plafond(point_charge):
   return plafonds[point_charge]