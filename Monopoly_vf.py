import random

def lancer_de_detail():
    return random.randint(1, 6), random.randint(1, 6)

def gestion_achat(joueur, propriete):
    if propriete.proprietaire is None:
        print(f"{propriete.nom} est disponible à l'achat pour {propriete.prix} euros.")
        achat = input("Voulez-vous l'acheter ? (o/n) : ")
        if achat.lower() == 'o':
            try:
                joueur.acheter_propriete(propriete)
                print(f"{joueur.nom} a acheté {propriete.nom} pour {propriete.prix} euros.")
            except Exception as e:
                print(e)
    elif propriete.proprietaire != joueur:
        loyer = propriete.loyer
        print(f"{joueur.nom} doit payer {loyer} euros à {propriete.proprietaire.nom} pour {propriete.nom}.")
        joueur.payer(loyer, propriete.proprietaire)

def gestion_carreau_special(joueur, carreau):
    if carreau.nom == "Impôts sur le revenu":
        print(f"{joueur.nom} doit payer 200 euros pour les Impôts sur le revenu.")
        joueur.payer(200, None)
    elif carreau.nom == "Taxe de Luxe":
        print(f"{joueur.nom} doit payer 100 euros pour la Taxe de Luxe.")
        joueur.payer(100, None)

class Monopoly:
    def __init__(self):
        self.nb_maisons = 32
        self.nb_hotels = 12
        self.carreaux = self.remplir_carreaux()
        self.joueurs = []
        self.joueur_en_prison = {}
        self.compteur_tour = 0

    def remplir_carreaux(self):
        carreaux = []
        carreaux.append(CarreauMouvement(1, "Départ"))
        carreaux.append(ProprieteAConstruire(2, "Boulevard de Belleville", 60, "Mauve", 2))
        carreaux.append(CarreauAction(3, "Caisse de Communauté"))
        carreaux.append(ProprieteAConstruire(4, "Rue Lecourbe", 60, "Mauve", 4))
        carreaux.append(CarreauPropriete(5, "Impôts sur le revenu", 200))
        carreaux.append(Gare(6, "Gare Montparnasse", 200, 25))
        carreaux.append(ProprieteAConstruire(7, "Rue de Vaugirard", 100, "Bleu ciel", 6))
        carreaux.append(CarreauArgent(8, "Chance", 0))
        carreaux.append(ProprieteAConstruire(9, "Rue de Courcelles", 100, "Bleu ciel", 6))
        carreaux.append(ProprieteAConstruire(10, "Avenue de la République", 120, "Bleu ciel", 8))
        carreaux.append(CarreauMouvement(11, "Simple Visite / En prison"))
        carreaux.append(ProprieteAConstruire(12, "Boulevard de la Villette", 140, "Violet", 10))
        carreaux.append(Compagnie(13, "Compagnie de distribution d'électricité", 150, 4))
        carreaux.append(ProprieteAConstruire(14, "Avenue de Neuilly", 140, "Violet", 10))
        carreaux.append(ProprieteAConstruire(15, "Rue de Paradis", 160, "Violet", 12))
        carreaux.append(Gare(16, "Gare de Lyon", 200, 25))
        carreaux.append(ProprieteAConstruire(17, "Avenue Mozart", 180, "Orange", 14))
        carreaux.append(CarreauArgent(18, "Caisse de Communauté", 0))
        carreaux.append(ProprieteAConstruire(19, "Boulevard Saint-Michel", 180, "Orange", 14))
        carreaux.append(ProprieteAConstruire(20, "Place Pigalle", 200, "Orange", 16))
        carreaux.append(CarreauMouvement(21, "Parc Gratuit"))
        carreaux.append(ProprieteAConstruire(22, "Avenue Matignon", 220, "Rouge", 18))
        carreaux.append(CarreauArgent(23, "Chance", 0))
        carreaux.append(ProprieteAConstruire(24, "Boulevard Malesherbes", 220, "Rouge", 18))
        carreaux.append(ProprieteAConstruire(25, "Avenue Henri-Martin", 240, "Rouge", 20))
        carreaux.append(Gare(26, "Gare du Nord", 200, 25))
        carreaux.append(ProprieteAConstruire(27, "Faubourg Saint-Honoré", 260, "Jaune", 22))
        carreaux.append(ProprieteAConstruire(28, "Place de la Bourse", 260, "Jaune", 22))
        carreaux.append(Compagnie(29, "Compagnie de Distribution d'Electricité", 150, 4))
        carreaux.append(ProprieteAConstruire(30, "Rue La Fayette", 280, "Jaune", 24))
        carreaux.append(CarreauMouvement(31, "Allez en prison"))
        carreaux.append(ProprieteAConstruire(32, "Avenue de Breteuil", 300, "Vert", 26))
        carreaux.append(ProprieteAConstruire(33, "Avenue Foch", 300, "Vert", 26))
        carreaux.append(CarreauArgent(34, "Caisse de Communauté", 0))
        carreaux.append(ProprieteAConstruire(35, "Boulevard des Capucines", 320, "Vert", 28))
        carreaux.append(Gare(36, "Gare Saint-Lazare", 200, 25))
        carreaux.append(CarreauArgent(37, "Chance", 0))
        carreaux.append(ProprieteAConstruire(38, "Avenue des Champs-Elysées", 350, "Bleu foncé", 35))
        carreaux.append(CarreauArgent(39, "Taxe de Luxe", -100))
        carreaux.append(ProprieteAConstruire(40, "Rue de la Paix", 400, "Bleu foncé", 50))
        return carreaux

    def afficher_menu(self):
        while True:
            print("\nMenu:")
            print("1. Inscrire les joueurs")
            print("2. Commencer le jeu")
            print("3. Quitter")
            choix = input("Choisissez une option : ")
            if choix == "1":
                self.inscrire_joueurs()
            elif choix == "2":
                if len(self.joueurs) >= 2:
                    self.determiner_ordre_joueurs()
                    self.lancer_jeu()
                else:
                    print("Au moins deux joueurs doivent être inscrits avant de commencer.")
            elif choix == "3":
                print("Au revoir !")
                break
            else:
                print("Option invalide, veuillez réessayer.")

    def inscrire_joueurs(self):
        pions_disponibles = ['&', '=', '[', '{', '+', '€', '$', '£']
        while True:
            if len(self.joueurs) >= 8:
                print("Le nombre maximum de joueurs est atteint.")
                break
            nom = input("Entrez le nom du joueur (ou appuyez sur Entrée pour terminer) : ")
            if not nom:
                break
            print("Pions disponibles :", ", ".join(pions_disponibles))
            pion = input("Choisissez un pion pour ce joueur : ")
            if pion not in pions_disponibles:
                print("Pion invalide, veuillez réessayer.")
                continue
            pions_disponibles.remove(pion)
            self.joueurs.append(Joueur(nom, pion))

    def determiner_ordre_joueurs(self):
        print("\nChaque joueur lance les dés pour déterminer l'ordre de jeu.")
        scores = {}
        for joueur in self.joueurs:
            d1, d2 = lancer_de_detail()
            score = d1 + d2
            print(f"{joueur.nom} a lancé {d1} et {d2}, total : {score}.")
            scores[joueur] = score
        self.joueurs.sort(key=lambda x: scores[x], reverse=True)
        print("\nOrdre de jeu :")
        for idx, joueur in enumerate(self.joueurs, start=1):
            print(f"{idx}. {joueur.nom}")

    def lancer_jeu(self):
        print("\nLe jeu commence !")
        jeu_termine = False
        while not jeu_termine:
            self.compteur_tour += 1
            print("\n" + "#" * 85)
            print(f"Tour {self.compteur_tour}")
            print("#" * 85)

            # Affichage récapitulatif des propriétés de chaque joueur
            print("\nÉtat des joueurs :")
            for joueur in self.joueurs:
                proprietes = ""
                for p in joueur.proprietes:
                    proprietes += p.nom + ", "
                proprietes = proprietes[:-2] if proprietes else "Aucune"
                print(f"{joueur.nom} ({joueur.pion}) - Solde : {joueur.cash} euros - Propriétés : {proprietes}")

            for joueur in self.joueurs:
                print(f"\n{joueur.nom} ({joueur.pion}) - Solde : {joueur.cash} euros")
                choix = input("Appuyez sur Entrée pour lancer les dés ou 'q' pour quitter : ")
                if choix.lower() == 'q':
                    jeu_termine = True
                    print("Le jeu se termine.")
                    break
                d1, d2 = lancer_de_detail()
                valeur_des = d1 + d2
                joueur.deplacer(valeur_des)
                case_actuelle = self.carreaux[joueur.position - 1]
                print(f"{joueur.nom} a lancé {d1} et {d2}, total : {valeur_des}, il est sur la case {joueur.position} ({case_actuelle.nom}).")
                if isinstance(case_actuelle, Gare) or isinstance(case_actuelle, Compagnie) or isinstance(case_actuelle, ProprieteAConstruire):
                    gestion_achat(joueur, case_actuelle)
                elif isinstance(case_actuelle, CarreauPropriete) and not isinstance(case_actuelle, ProprieteAConstruire):
                    gestion_carreau_special(joueur, case_actuelle)
                if joueur.cash <= 0:
                    print(f"{joueur.nom} n'a plus d'argent. Le jeu se termine.")
                    jeu_termine = True
                    break

class Joueur:
    def __init__(self, nom, pion):
        self.nom = nom
        self.pion = pion
        self.cash = 1500
        self.proprietes = []
        self.position = 1

    def deplacer(self, valeur_des):
        self.position = (self.position + valeur_des - 1) % 40 + 1

    def acheter_propriete(self, propriete):
        if self.cash >= propriete.prix:
            self.cash -= propriete.prix
            self.proprietes.append(propriete)
            propriete.proprietaire = self
        else:
            raise Exception("Fonds insuffisants pour acheter cette propriété.")

    def payer(self, montant, destinataire):
        if self.cash >= montant:
            self.cash -= montant
            if destinataire:
                destinataire.cash += montant
        else:
            self.cash = 0
            print(f"{self.nom} n'a pas assez d'argent pour payer {montant} euros !")

class Carreau:
    def __init__(self, numero, nom):
        self.numero = numero
        self.nom = nom

class CarreauAction(Carreau):
    def __init__(self, numero, nom):
        super().__init__(numero, nom)

class CarreauArgent(CarreauAction):
    def __init__(self, numero, nom, montant):
        super().__init__(numero, nom)
        self.montant = montant

class CarreauMouvement(Carreau):
    def __init__(self, numero, nom):
        super().__init__(numero, nom)

class CarreauPropriete(Carreau):
    def __init__(self, numero, nom, prix):
        super().__init__(numero, nom)
        self.prix = prix
        self.loyer = prix // 10
        self.proprietaire = None

class ProprieteAConstruire(CarreauPropriete):
    def __init__(self, numero, nom, prix, couleur, loyer):
        super().__init__(numero, nom, prix)
        self.couleur = couleur
        self.loyer = loyer
        self.nb_maisons = 0
        self.hotel = False

class Gare(CarreauPropriete):
    def __init__(self, numero, nom, prix, loyer):
        super().__init__(numero, nom, prix)
        self.loyer = loyer

class Compagnie(CarreauPropriete):
    def __init__(self, numero, nom, prix, multiplicateur):
        super().__init__(numero, nom, prix)
        self.multiplicateur = multiplicateur

    def calculer_loyer(self, des):
        return des * self.multiplicateur


if __name__ == "__main__":
    monopoly = Monopoly()
    monopoly.afficher_menu()

