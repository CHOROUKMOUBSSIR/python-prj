contacts = []

while True:
    print("1. Ajouter un contact")
    print("2. Afficher tous les contacts")
    print("3. Quitter le programme")

    choix = input("Votre choix : ")

    if choix == "1":
        nom = input("Nom : ")
        telephone = input("Téléphone : ")
        contact = {"nom": nom, "telephone": telephone}
        contacts.append(contact)
        print("Contact ajouté.")
    elif choix == "2":
        if len(contacts) == 0:
            print("Aucun contact enregistré.")
        else:
            for index, contact in enumerate(contacts, start=1):
                print(f"{index}. Nom: {contact['nom']} | Téléphone: {contact['telephone']}")
    elif choix == "3":
        print("Au revoir.")
        break
    else:
        print("Choix invalide.")