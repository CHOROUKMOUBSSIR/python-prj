from abc import ABC, abstractmethod
from dataclasses import dataclass

#partie 1 : Structure de base
class Boisson(ABC):
    @abstractmethod
    def cout(self) -> float: pass
    @abstractmethod
    def description(self) -> str: pass

    def __add__(self, other):
        return Combo(self, other)

# partie 2 : création de Boissons simples
class Cafe(Boisson):
    def cout(self): return 2.0
    def description(self): return "Café simple"

class The(Boisson):
    def cout(self): return 1.5
    def description(self): return "Thé"

# partie 3-6 : création de décorateurs pour les ingrédients
class DecorateurBoisson(Boisson):
    def __init__(self, boisson): self._boisson = boisson

class Lait(DecorateurBoisson):
    def cout(self): return self._boisson.cout() + 0.5
    def description(self): return self._boisson.description() + ", Lait"

class Sucre(DecorateurBoisson):
    def cout(self): return self._boisson.cout() + 0.2
    def description(self): return self._boisson.description() + ", Sucre"

class Caramel(DecorateurBoisson):
    def cout(self): return self._boisson.cout() + 0.8
    def description(self): return self._boisson.description() + ", Caramel"

# partie 4 : Combinaison de boissons
class Combo(Boisson):
    def __init__(self, b1, b2): self.b1, self.b2 = b1, b2
    def cout(self): return self.b1.cout() + self.b2.cout()
    def description(self): return f"{self.b1.description()} + {self.b2.description()}"

# partie 5 : Gestion des clients
@dataclass
class Client:
    nom: str
    numero: int
    points_fidelite: int

# partie 7 : Système de commandes et fidélité

# classe de base pour les commandes
class Commande:
    def __init__(self, client):
        self.client = client
        self.items = [] # Liste de boissons

    def ajouter(self, b: Boisson):
        self.items.append(b)

    def total(self):
        return sum(item.cout() for item in self.items)

    def afficher(self):
        print(f"Client : {self.client.nom}")
        for i in self.items:
            print(f"- {i.description()} : {i.cout()}€")
        print(f"Total : {self.total()}€")

# types de commandes avec comportements différents
class CommandeSurPlace(Commande):
    def afficher(self):
        print("SUR PLACE")
        super().afficher()

class CommandeEmporter(Commande):
    def afficher(self):
        print("À EMPORTER (Taxe +0.50€)")
        super().afficher()
        print(f"Total final : {self.total() + 0.5}€")

# Système de fidélité
class Fidelite:
    def maj_points(self, client, montant):
        # 1€ dépensé = 1 point ajouté
        pts_gagnes = int(montant)
        client.points_fidelite += pts_gagnes
        print(f"Points gagnés : {pts_gagnes}")

# 4. Héritage multiple
class CommandeFidele(Commande, Fidelite):
    def valider(self):
        montant = self.total()
        self.maj_points(self.client, montant)
        print("Commande validée avec fidélité.")


# Création du client
cl = Client("Aya", 101, 0)

# Création des boissons
b1 = Sucre(Lait(Cafe())) # Café + Lait + Sucre
b2 = Caramel(The())      # Thé + Caramel

# Création de la commande fidèle
cmd = CommandeFidele(cl)
cmd.ajouter(b1)
cmd.ajouter(b2)

# Affichage
cmd.afficher()

# Validation et points
cmd.valider()

# État final du client
print(f"Points de {cl.nom} après achat : {cl.points_fidelite}")