import matplotlib.pyplot as plt
from data import Data_List

Produit=[item[0] for item in Data_List]
Prix=[item[1] for item in Data_List]
# Unite=[item[2] for item in Data_List]

#Tracé Graphique ------------ < Barre

plt.bar(Produit, Prix, color='orange')
plt.xlabel('Produits')
plt.ylabel('Prix')
plt.title('Quantité Par Produit')
plt.show()


#-------------< Pie:




