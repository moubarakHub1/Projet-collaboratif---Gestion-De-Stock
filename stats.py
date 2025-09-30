import numpy as np
from data import Data_List

#------# Calcul valeur totale du stock
somme=0
for i in Data_List:
    for j in range(0,3):
        somme+=Data_List[i][1]

print("la somme est: ",somme)
#------#  Prix moyen
Moy=0
Cpt=0

for i in Data_List:
    cpt+=1

if Cpt!=0:
    Moy=somme/Cpt
else:
    print("Erreur!")
print("La moyenne est: ",Moy)

#------#  Prix min/max
Prix_Max=Data_List.max(key=lambda x : x[1])
Prix_Min=Data_List.min(Key=lambda x : x[1])

#------#  Produit le plus cher et le moins cher
print(f" Le Prix maximal : {Prix_Max} \n et Le Prix minimal : {Prix_Min}")