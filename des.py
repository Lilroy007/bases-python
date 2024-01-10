from random import randint


class Dé:
    nbFaces = 6 # variable de classe
    
    
    def __init__(self): # constructeur
        self.face = 1
    def lancer(self):  # méthode (fonction d'objet) 
        self.face = randint(1, self.nbFaces)
    def afficher(self): # méthode (fonction d'objet)
        print(f"La face du dé est {self.face}")
    def valeur(self): # méthode (fonction d'objet)
        return self.face

# Créer deux dés
class Dés:
    de1 = Dé()
    de2 = Dé()

# Lancer les dés
Dés.de1.lancer()
Dés.de2.lancer()

# Afficher les valeurs
print(f"Valeur dé 1: {Dés.de1.valeur()}")
print(f"Valeur dé 2: {Dés.de2.valeur()}")  

# Vérifier si c'est un double
if Dés.de1.valeur() == Dés.de2.valeur():  
    print("C'est un double!")
else:
    print("Ce n'est pas un double.")

# Calculer et afficher la somme et le produit des deux dés
somme = Dés.de1.valeur() + Dés.de2.valeur()  
produit = Dés.de1.valeur() * Dés.de2.valeur()  
print(f"Somme des deux dés: {somme}")
print(f"Produit des deux dés: {produit}")