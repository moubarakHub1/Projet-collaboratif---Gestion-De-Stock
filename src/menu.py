from stock import afficher_stock, ajouter_produit, supprimer_produit, modifier_quantite

def menu():
    while True:
        print("\n--- Menu Principal ---")
        print("1- Ajouter un produit ")
        print("2- Supprimer un produit")
        print("3- Mettre à jour la quantité d’un produit existant")
        print("4- Afficher la liste des produits disponibles")
        print("5- Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            nom = input("Nom du produit : ")
            quantite = int(input("Quantité : "))
            prix = float(input("Prix : "))
            ajouter_produit(nom, quantite, prix)

        elif choix == "2":
            nom = input("Nom du produit à supprimer : ")
            supprimer_produit(nom)

        elif choix == "3":
            nom = input("Nom du produit : ")
            nouvelle_quantite = int(input("Nouvelle quantité : "))
            modifier_quantite(nom, nouvelle_quantite)

        elif choix == "4":
            afficher_stock()

        elif choix == "5":
            print("Au revoir !")
            break

        else:
            print("Option invalide, réessayez.")

