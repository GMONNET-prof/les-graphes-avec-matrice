# Bardia - Spécialité NSI Terminale - Classe Graphe V1

class Graphe_V1:

    def __init__(self, n, liste = None):
        """ constructeur de la classe Graphe_V1.
            n est l'ordre du graphe et sera affecté à l'attribut ordre.
            l'attribut matrice sera un tableau python de dimension n x n
            dont les valeurs seront initialisées à zéro ou à liste. """
        self.ordre = n
        if liste is None:
            self.matrice = [[0] * n for i in range (n)]
        else:
            self.matrice = liste

    def ajouter_arc(self, s1, s2):
        """ incrémente le coefficient de s1 à s2 de 1 dans la matrice.
            Entrée : Deux indices (int) entre 0 et (n-1)
            Sortie : Aucune Sortie"""
        self.matrice[s1][s2] += 1 

    def est_adjacent(self, s1, s2):
        """ renvoie True si s1 et s2 sont adjacents, False sinon.
            Entrée : 
            Sortie : Booléen"""
        if self.matrice[s1][s2] > 0:
            return True
        else:
            return False
        
    def voisins(self, s):
        """ renvoie la liste des voisins du sommet s.
            Entrée :
            Sortie : Liste des voisins d'un sommet"""
        voisins = []
        for i in range(self.ordre):
            if self.matrice[s][i] > 0:
                voisins.append(i)
        return voisins
        
    def degre(self, s):
        """ renvoie le degré du sommet s.
            Entrée :
            Sortie : Le nombre d'arcs partant d'un sommet s (int) """
        degre = 0
        for i in range(self.ordre):
            degre += self.matrice[s][i]
        return degre

    def est_simple(self):
        """ renvoie True si le graphe est simple, False sinon.
            Entrée :
            Sortie : Booléen"""
        for i in range(self.ordre):
            if self.matrice[i][i] != 0:
                return False
            else:
                for j in range(self.ordre):
                    if self.matrice[i][j] > 1:
                        return False
        return True
    
    def affichage(self):
        """ propose un affichage dans la console du graphe sous la forme :
            0 -> [1, 3]
            1 -> [2, 3]
            2 -> []
            3 -> [1]
            Entrée :
            Sortie : Une chaine (str)"""
        for i in range(self.ordre):
            print(f"{i} -> {self.voisins(i)}")

    def est_oriente(self):
        """ renvoie True si le graphe est orienté, False sinon.
            Entrée :
            Sortie : Booléen """
        for i in range(self.ordre):
            for j in range(self.ordre):
                if self.matrice[i][j] != self.matrice[j][i]:
                    return True
        return False

    def arcs(self):
        """ renvoie le nombre d'arcs ou d'arêtes du graphe.
            Entrée :
            Sortie : """
        total = 0
        for i in range(self.ordre):
            for j in range(self.ordre):
                total += self.matrice[i][j]
        return total

    def supprimer_arc(self, s1, s2):
        """ décrémente le coefficient de s1 à s2 de 1 dans la matrice.
            ne fait rien si s1 et s2 n'étaient pas adjacents.
            Entrée :
            Sortie : """
        if self.matrice[s1][s2] > 0:
                self.matrice[s1][s2] -= 1

    def est_complet(self):
        """ renvoie True si le graphe est complet, False sinon.
            Entrée :
            Sortie : """
        for i in range(self.ordre):
            for j in range(self.ordre):
                if i != j and self.matrice[i][j] == 0:
                    return False
        return True

if __name__ == "__main__":
    graphe_1 = Graphe_V1(6, [[0, 1, 0, 0, 1, 0],
                             [1, 0, 1, 1, 0, 0],
                             [0, 1, 0, 1, 0, 1],
                             [0, 1, 1, 0, 1, 1],
                             [1, 0, 0, 1, 0, 0],
                             [0, 0, 1, 1, 0, 0]])

    graphe_2 = Graphe_V1(5)
    graphe_2.ajouter_arc(0, 1)
    graphe_2.ajouter_arc(0, 2)
    graphe_2.ajouter_arc(0, 3)
    graphe_2.ajouter_arc(2, 1)
    graphe_2.ajouter_arc(2, 3)
    graphe_2.ajouter_arc(2, 4)
    graphe_2.ajouter_arc(3, 1)
    graphe_2.ajouter_arc(3, 4)

    graphe_3 = Graphe_V1(3, [[0, 1, 1],
                             [1, 0, 1],
                             [1, 1, 0]])

# LES TESTS
    
assert graphe_1.est_adjacent(0, 1) == True
assert graphe_1.voisins(0) == [1, 4]
assert graphe_1.degre(0) == 2
assert graphe_1.est_simple() == True
assert graphe_1.est_oriente() == False
assert graphe_1.est_complet() == False
# graphe_1.affichage()

assert graphe_2.voisins(1) == []
assert graphe_2.est_complet() == False
assert graphe_2.est_adjacent(0, 1) == True
assert graphe_2.est_oriente() == True
# graphe_2.affichage()

assert graphe_3.arcs() == 6
assert graphe_3.est_adjacent(0, 0) == False
assert graphe_3.est_complet() == True
assert graphe_3.voisins(0) == [1, 2]
assert graphe_3.est_oriente() == False
assert graphe_3.est_simple() == True
# graphe_3.affichage()




note = 0

# =========================
# CONSTRUCTEUR (2 tests)
# =========================
try:
    g = Graphe_V1(3)
    assert g.ordre == 3
except:
    print("Erreur constructeur : attribut ordre incorrect")
else:
    note += 1

try:
    g = Graphe_V1(3)
    assert len(g.matrice) == 3 and all(len(ligne) == 3 for ligne in g.matrice)
except:
    print("Erreur constructeur : matrice mal initialisée")
else:
    note += 1

# =========================
# ajouter_arc (2 tests)
# =========================
try:
    g = Graphe_V1(2)
    g.ajouter_arc(0, 1)
    assert g.matrice[0][1] == 1
except:
    print("Erreur ajouter_arc : incrément simple incorrect")
else:
    note += 1

try:
    g = Graphe_V1(2)
    g.ajouter_arc(0, 1)
    g.ajouter_arc(0, 1)
    assert g.matrice[0][1] == 2
except:
    print("Erreur ajouter_arc : incrément multiple incorrect")
else:
    note += 1

# =========================
# est_adjacent (2 tests)
# =========================
try:
    g = Graphe_V1(2, [[0,1],[1,0]])
    assert g.est_adjacent(0,1) == True
except:
    print("Erreur est_adjacent : devrait être True")
else:
    note += 1

try:
    g = Graphe_V1(2, [[0,1],[1,0]])
    assert g.est_adjacent(0,0) == False
except:
    print("Erreur est_adjacent : boucle mal gérée")
else:
    note += 1

# =========================
# voisins (2 tests)
# =========================
try:
    g = Graphe_V1(3, [[0,1,0],[1,0,1],[0,1,0]])
    assert g.voisins(1) == [0,2]
except:
    print("Erreur voisins : liste incorrecte")
else:
    note += 1

try:
    g = Graphe_V1(3, [[0,0,0],[0,0,0],[0,0,0]])
    assert g.voisins(0) == []
except:
    print("Erreur voisins : devrait être vide")
else:
    note += 1

# =========================
# degre (2 tests)
# =========================
try:
    g = Graphe_V1(3, [[0,1,1],[1,0,0],[1,0,0]])
    assert g.degre(0) == 2
except:
    print("Erreur degre : valeur incorrecte")
else:
    note += 1

try:
    g = Graphe_V1(3, [[0,0,0],[0,0,0],[0,0,0]])
    assert g.degre(1) == 0
except:
    print("Erreur degre : devrait être 0")
else:
    note += 1

# =========================
# est_simple (2 tests)
# =========================
try:
    g = Graphe_V1(2, [[0,1],[1,0]])
    assert g.est_simple() == True
except:
    print("Erreur est_simple : devrait être True")
else:
    note += 1

try:
    g = Graphe_V1(2, [[0,2],[1,0]])
    assert g.est_simple() == False
except:
    print("Erreur est_simple : devrait être False")
else:
    note += 1

# =========================
# est_oriente (2 tests)
# =========================
try:
    g = Graphe_V1(2, [[0,1],[1,0]])
    assert g.est_oriente() == False
except:
    print("Erreur est_oriente : devrait être False")
else:
    note += 1

try:
    g = Graphe_V1(2, [[0,1],[0,0]])
    assert g.est_oriente() == True
except:
    print("Erreur est_oriente : devrait être True")
else:
    note += 1

# =========================
# arcs (2 tests)
# =========================
try:
    g = Graphe_V1(2, [[0,1],[1,0]])
    assert g.arcs() == 2
except:
    print("Erreur arcs : somme incorrecte")
else:
    note += 1

try:
    g = Graphe_V1(2, [[0,2],[0,0]])
    assert g.arcs() == 2
except:
    print("Erreur arcs : gestion des poids incorrecte")
else:
    note += 1

# =========================
# supprimer_arc (2 tests)
# =========================
try:
    g = Graphe_V1(2, [[0,1],[0,0]])
    g.supprimer_arc(0,1)
    assert g.matrice[0][1] == 0
except:
    print("Erreur supprimer_arc : décrément incorrect")
else:
    note += 1

try:
    g = Graphe_V1(2, [[0,0],[0,0]])
    g.supprimer_arc(0,1)
    assert g.matrice[0][1] == 0
except:
    print("Erreur supprimer_arc : ne doit pas passer sous 0")
else:
    note += 1

# =========================
# est_complet (2 tests)
# =========================
try:
    g = Graphe_V1(3, [[0,1,1],[1,0,1],[1,1,0]])
    assert g.est_complet() == True
except:
    print("Erreur est_complet : devrait être True")
else:
    note += 1

try:
    g = Graphe_V1(3, [[0,1,0],[1,0,1],[0,1,0]])
    assert g.est_complet() == False
except:
    print("Erreur est_complet : devrait être False")
else:
    note += 1

# =========================
# NOTE FINALE
# =========================
print("Note finale :", note, "/20")
print("tous les tests sont validés")
