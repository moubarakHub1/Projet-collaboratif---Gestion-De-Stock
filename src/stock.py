stock = [
    ["telephone", 15, 2000],
    ["ordinateur", 11, 400],
    ["souris", 6, 300],
    ["clavier",8,400],
    ["ecran",2,1500]
]
#afficher le stock :
def afficher_stock():
    if not stock :
        print('le stock est vide!')
    else:
        print('---Stock actuel---')
        for p in stock:
            print(f"produit : {p[0]}, Quantité: {p[1]}, prix: {p[2]}Dh")
#ajouter produit :
def ajouter_produit(nom,quantite,prix):
    stock.append([nom,quantite,prix])
    print(" produit ajouté avec succes !")
#supproier un produit 
def supprimer_produit(nom):
    trouve = False 
    for produit in stock:
        if produit[0]==nom:
            stock.remove(produit)
            print("produit supprimé :",nom)
            trouve= True
            break
    if not trouve:
        print("produit non trouvé :",nom)
#modifier la quantité 
trouve = False

def modifier_quantite(nom, nouvelle_quantite):
    for produit in stock:
        if produit[0] == nom:
            produit[1] = nouvelle_quantite
            print("quantité mise a jour pour ",nom,":",nouvelle_quantite)
            trouve=True
            break
    if not trouve:
      print("produit non trouvé!",nom)