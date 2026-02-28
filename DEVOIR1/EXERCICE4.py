nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

print("Choisissez une opération :")
print("1 : addition")
print("2 : soustraction")
print("3 : multiplication")
print("4 : division")

choix = input("Votre choix : ")

if choix == "1":
    print("Résultat :", nombre1 + nombre2)
elif choix == "2":
    print("Résultat :", nombre1 - nombre2)
elif choix == "3":
    print("Résultat :", nombre1 * nombre2)
elif choix == "4":
    if nombre2 != 0:
        print("Résultat :", nombre1 / nombre2)
    else:
        print("Erreur : division par zéro impossible.")
else:
    print("Choix invalide.")