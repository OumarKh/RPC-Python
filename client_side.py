from xmlrpc.client import ServerProxy

# Adresse du serveur XML-RPC
server_address = 'http://localhost:8000/RPC2'

# Créer un proxy pour se connecter au serveur
server_proxy = ServerProxy(server_address)

while True:
    print("\nMenu:")
    print("1- Ajouter nouveau membre")
    print("2- Chercher membre")
    print("3- Afficher annuaire")
    print("4- Afficher enseignants")
    print("5- Afficher administratifs")
    print("6- Quitter")

    try:
        choice = int(input("Choisissez une option (1-6): "))

        if choice == 1:
            # Obtenir les détails du membre auprès de l'utilisateur
            nom = input("Nom: ")
            prenom = input("Prénom: ")
            numero = input("Numéro de téléphone: ")
            email = input("Email: ")
            fonction = input("Fonction (enseignant/administratif): ")

            # Appeler la méthode ajouterMembre sur le serveur
            result = server_proxy.ajouterMembre(nom, prenom, numero, email, fonction)
            print(result)

        elif choice == 2:
            # Obtenir le nom du membre auprès de l'utilisateur
            nom = input("Nom du membre à chercher: ")

            # Appeler la méthode chercherMembre sur le serveur
            result = server_proxy.chercherMembre(nom)
            if result:
                print(f"Email: {result['email']}, Numéro de téléphone: {result['numero']}")
            else:
                print(f"Aucun membre trouvé avec le nom {nom}.")

        elif choice == 3:
            # Appeler la méthode afficherAnnuaire sur le serveur
            result = server_proxy.afficherAnnuaire()
            if result:
                print("\nAnnuaire des membres:")
                for member_info in result:
                    print(member_info)
            else:
                print("Aucun membre dans l'annuaire.")

        elif choice == 4:
            # Appeler la méthode afficherEnseignants sur le serveur
            result = server_proxy.afficherEnseignants()
            if result:
                print("\nEnseignants:")
                for teacher_info in result:
                    print(teacher_info)
            else:
                print("Aucun enseignant trouvé.")

        elif choice == 5:
            # Appeler la méthode afficherAdministratifs sur le serveur
            result = server_proxy.afficherAdministratifs()
            if result:
                print("\nAdministratifs:")
                for admin_info in result:
                    print(admin_info)
            else:
                print("Aucun administratif trouvé.")

        elif choice == 6:
            print("Au revoir!")
            break

        else:
            print("Option invalide. Veuillez choisir une option entre 1 et 6.")

    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre entre 1 et 6.")
    except Exception as e:
        print(f"Erreur lors de l'exécution de l'option : {e}")
