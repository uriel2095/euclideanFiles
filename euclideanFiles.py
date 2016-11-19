from scipy.spatial import distance
import csv
from math import*

with open("data.txt") as f:
  reader = csv.reader(f)
  for line, in reader:
      entries = line.split()
      
      print "\nPrimera Lista de valores \n" + str (entries)

with open("data2.txt") as f:
  reader = csv.reader(f)
  for line, in reader:
      entries2 = line.split()
      
      print "\nSegunda Lista de valores\n" +str(entries2) 

a =list(map(int,entries))
b =list(map(int,entries2))

dst = distance.euclidean(a,b)

print "\nDistancia euclidiana\n" + str(dst) + "\n"
