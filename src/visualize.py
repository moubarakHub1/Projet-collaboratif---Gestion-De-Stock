import matplotlib.pyplot as plt
# from data import Data_List
from stock import stock

Produit=[item[0] for item in stock]
Prix=[item[1] for item in stock]
# Unite=[item[2] for item in Data_List]

#Tracé Graphique ------------ < Barre

plt.bar(Produit, Prix, color='orange')
plt.xlabel('Produits')
plt.ylabel('Prix')
plt.title('Quantité Par Produit')
plt.show()


#-------------< Pie:

labels = ['Python', 'C++', 'Java'] 
labels = (item[0] for) 
sizes = [50, 30, 20]
explode = [0.1, 0, 0]  # Met en évidence Python

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, explode=explode)
plt.title('Répartition des langages')
plt.show()


