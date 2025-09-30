import matplotlib.pyplot as plt

#-------------< Pie:
# labels = ['Python', 'C++', 'Java'] 
# labels = (item[0] for)
# sizes = [50, 30, 20]
# explode = [0.1, 0, 0]  # Met en évidence Python

# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, explode=explode)
# plt.title('Répartition des langages')
# plt.show()

#------------< Barre
# import matplotlib.pyplot as plt

categories = ['Python', 'C++', 'Java']
values = [80, 60, 70]

plt.bar(categories, values, color='orange')
plt.xlabel('Langages')
plt.ylabel('Popularité')
plt.title('Popularité des langages')
plt.show()