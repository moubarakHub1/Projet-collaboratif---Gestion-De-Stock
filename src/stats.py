import numpy as np
# from data import Data_List
from stock import stock

#------# Calcul valeur totale du stock
# somme=0
Prix,Qté=1
Val_ttl=0
for i in stock:
    for j in range(0,3):
        # Prix_Qte=Prix * Qté
        # somme+=Prix_Qte
        Val_ttl=np.sum(Prix * Qté)
print("Valeur totale du stock est: ",Val_ttl)
print("<================================>")

#------#  Prix moyen
Moy=0
# Cpt=0
for i in stock:
    Moy=np.average(Prix)

# if Cpt!=0:
#     Moy=somme/Cpt   
# else:
#     print("Erreur!")
print("La moyenne est: ",Moy)

#------#  Prix min/max
Prix_Max=stock.max(key=lambda x : x[1])
Prix_Min=stock.min(Key=lambda x : x[1])

#------#  Produit le plus cher et le moins cher
print(f" Le Prix maximal : {Prix_Max} \n et Le Prix minimal : {Prix_Min}")