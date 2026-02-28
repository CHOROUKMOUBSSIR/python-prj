age = int(input("Entrez votre âge : "))

if age >= 0 and age <= 12:
    print("Vous êtes un enfant.")
elif age >= 13 and age <= 17:
    print("Vous êtes un adolescent.")
elif age >= 18 and age <= 64:
    print("Vous êtes un adulte.")
elif age >= 65:
    print("Vous êtes un senior.")
else:
    print("Âge invalide.")