class Graphe_V1:

    def __init__(self, n, liste = None):
        """ constructeur de la classe Graphe_V1.
            n est l'ordre du graphe et sera affecté à l'attribut ordre.
            l'attribut matrice sera un tableau python de dimension n x n
            dont les valeurs seront initialisées à zéro ou à liste. """
        self.ordre = n
        if liste is None:
            self.matrice = [[0] * n for i in range(n)]
        else:
            self.matrice = liste

    def ajouter_arc(self, s1, s2):
        """ incrémente le coefficient de s1 à s2 de 1 dans la matrice.
            Entrée : Deux indices (int) entre 0 et (n-1)
            Sortie : Aucune Sortie"""
        self.matrice[s1][s2] += 1 

    def est_adjacent(self, s1, s2):
        """ renvoie True si s1 et s2 sont adjacents, False sinon.
            Entrée : Deux indices (int) entre 0 et (n-1) 
            Sortie : Booléen"""
        return self.matrice[s1][s2]>0

    def voisins(self, s):
        """ renvoie la liste des voisins du sommet s.
            Entrée :
            Sortie : Liste des voisins d'un sommet"""
        liste=[]
        for i in range(len(self.matrice[s])):
            if self.matrice[s][i]>0:
                
                liste.append(i)
        return liste

    def degre(self, s):
        """ renvoie le degré du sommet s.
            Entrée :
            Sortie : Le nombre d'arcs partant d'un sommet s (int) """
        total=0
        for i in range(len(self.matrice[s])):
            total+=self.matrice[s][i]
        return total

    def est_simple(self):
        """ renvoie True si le graphe est simple, False sinon.
            Entrée :
            Sortie : Booléen"""
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[i])):
                if self.matrice[i][j]>1:
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
        chaine=""
        for i in range(len(self.matrice)):
            liste=[]
            chaine+= str(i)+" -> ["
            for j in self.matrice[i]:
                if j>0:
                    liste.append(j)
            chaine+=str(liste)+"\n"
        
        return chaine
            
            
            

    def est_oriente(self):
        """ renvoie True si le graphe est orienté, False sinon.
            Entrée :
            Sortie : Booléen """
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[i])):
                if self.matrice[i][j]==self.matrice[j][i] and self.matrice[i][j]!=0:
                    return False
        return True

    def arcs(self):
        """ renvoie le nombre d'arcs ou d'arêtes du graphe.
            Entrée :
            Sortie : """
        total=0
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[i])):
                total+=self.matrice[i][j]
        return total

    def supprimer_arc(self, s1, s2):
        """ décrémente le coefficient de s1 à s2 de 1 dans la matrice.
            ne fait rien si s1 et s2 n'étaient pas adjacents.
            Entrée :
            Sortie : """
        self.matrice[s1][s2] -= 1 

    def est_complet(self):
        """ renvoie True si le graphe est complet, False sinon.
            Entrée :
            Sortie : """
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[i])):
               if self.matrice[i][j]<=0 and i!=j :
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
    # for ligne in graphe_2.matrice:
    #     print(ligne)
    

    graphe_3 = Graphe_V1(3, [[0, 1, 1],
                             [1, 0, 1],
                             [1, 1, 0]])
    #ici commencent les tests
    assert Graphe_V1.est_adjacent(graphe_1,1,0)==True,"s1 et s2 sont adgacent"
    assert Graphe_V1.voisins(graphe_1,1)==[0,2,3],"les voisin de s ne sont pas correcte"
    assert Graphe_V1.degre(graphe_1,2)==3,"Le nombre d'arcs partant d'un sommet s n'set pas correcte"
    assert Graphe_V1.est_simple(graphe_1)==True,"est simple"
    print(Graphe_V1.affichage(graphe_1))
    assert Graphe_V1.est_oriente(graphe_1)==False,"graphe_1 est pas orienté"
    assert Graphe_V1.arcs(graphe_1)==16,"il y a 16 arcs au total"
    # Graphe_V1.supprimer_arc(graphe_1,1,0)
    assert Graphe_V1.est_complet(graphe_1)==False,"le graphe n'est pas complet"
    
    
    assert Graphe_V1.est_adjacent(graphe_2,0,1)==True,"s1 et s2 sont adgacent"
    assert Graphe_V1.voisins(graphe_2,0)==[1,2,3],"les voisin de s ne sont pas correcte"
    assert Graphe_V1.degre(graphe_2,2)==3,"Le nombre d'arcs partant d'un sommet s n'set pas correcte"
    assert Graphe_V1.est_simple(graphe_2)==True,"est simple"
    print(Graphe_V1.affichage(graphe_2))
    assert Graphe_V1.est_oriente(graphe_2)==True,"graphe_1 est orienté"
    assert Graphe_V1.arcs(graphe_2)==8,"il y a 8 arcs au total"
    # Graphe_V1.supprimer_arc(graphe_2,1,0)
    assert Graphe_V1.est_complet(graphe_2)==False,"le graphe n'est pas complet"
    
    assert Graphe_V1.est_adjacent(graphe_3,0,1)==True,"s1 et s2 sont adgacent"
    assert Graphe_V1.voisins(graphe_3,0)==[1,2],"les voisin de s ne sont pas correcte"
    assert Graphe_V1.degre(graphe_3,2)==2,"Le nombre d'arcs partant d'un sommet s n'set pas correcte"
    assert Graphe_V1.est_simple(graphe_3)==True,"est simple"
    print( Graphe_V1.affichage(graphe_3))
    assert Graphe_V1.est_oriente(graphe_3)==False,"graphe_1 est pas orienté"
    assert Graphe_V1.arcs(graphe_3)==6,"il y a 6 arcs au total"
    # Graphe_V1.supprimer_arc(graphe_3,1,0)
    assert Graphe_V1.est_complet(graphe_3,)==True,"le graphe est complet"
    
    
    
    
    
    
    print("tous les tests sont validés")


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
