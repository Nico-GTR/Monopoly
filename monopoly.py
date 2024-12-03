# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:41:37 2024

@author: gautnico
"""

# Classe Joueur :
class Joueur:
    
    def __init__(self, player: str, monopoly: Monopoly):    
        self.name = player
        self.cash = 1500
        self.nbGare = []
        self.nbCompagnie = []
        self.nbPropriete = []
        self.jeu = monopoly
        self.pos = self.jeu.dico_carreauu[1]

    # -------------------Nom------------------------
    def set_name(self, new_val: str):
        self.name = new_val
        
    def get_name(self):
        return self.name
    
    # -------------------Position-------------------
    def set_pos(self, val_des: int):
        self.pos += val_des
    
    def get_pos(self):
        return self.pos
    
    # -------------------Gare----------------------
    def set_nbGare(self, new_val: int):
        self.nbGare = new_val

    def get_nbGare(self):
        return self.nbGare
    
    # -------------------Compagnie-----------------
    def set_nbCompagnie(self, new_val: int):
        self.nbCompagnie = new_val

    def get_nbCompagnie(self):
        return self.nbCompagnie
    
    # -------------------Propriete-----------------
    def set_nbPropriete(self, new_val: int):
        self.nbPropriete = new_val

    def get_nbPropriete(self):
        return len(self.nbPropriete)
    
    # ------------------Cash-----------------------
    # def moins_cash(self, montant: int):
    #     self.cash -= montant
    # 
    # def plus_cash(self, montant: int):
    #     self.cash += montant



# Classe CarreauPropriete :
class CarreauPropriete(Carreau):
    
    def __init__(self, numero: int, prix_terrain_nu: int, loyer_1_maison: int):
        super().__init__(numero)
        self.proprio = None
        self.prix_terrain_nu = prix_terrain_nu
        self.loyer_1_maison = loyer_1_maison
        
    def set_proprio(self, name: Joueur):  # Ici Joueur est le type de l'attribut player
        self.proprio = name
    
    def get_proprio(self):
        return self.proprio
    
    def get_terrain_nu(self):
        return self.prix_terrain_nu
    
    def get_loyer_1_maison(self):
        return self.loyer_1_maison
    


# Classe Compagnie :
class Compagnie(CarreauPropriete):
    
    def __init__(self, proprietaire: str, nom: str, loyer: str):
        super().__init__(proprietaire)
        self.name = nom
        self.loyer = loyer
    
    def get_prix_compagnie(self):
        if Joueur.get_nbCompagnie() == 1:
            return self.loyer = 4 * des
        elif Joueur.get_nbCompagnie() == 2:
            return self.loyer = 10 * des
        else:
            return self.loyer = 0


# Classe Gare : 
class Gare(CarreauPropriete):
    
    def __init__(self, nom: str, prix: int):
        super().__init__()
        self.name = nom

    
# Classe Groupe:
class Groupe:
    
    def __init__(self, couleur):
        self.color = couleur

    def set_color(self, new_color : str):
        self.color = new_color       


# Classe ProprieteAConstruire :
class ProprieteAConstruire(Groupe, CarreauPropriete):
    
    def __init__(self, prix):