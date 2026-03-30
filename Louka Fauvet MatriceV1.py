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
            Entrée : 
            Sortie : Booléen"""
        return self.matrice[s1][s2] >= 1 or self.matrice[s2][s1] >= 1

    def voisins(self, s):
        """ renvoie la liste des voisins du sommet s.
            Entrée :
            Sortie : Liste des voisins d'un sommet"""
        liste = []
        for i in range(self.ordre):
            if self.matrice[s][i] >= 1: liste.append(i)
        return liste

    def degre(self, s):
        """ renvoie le degré du sommet s.
            Entrée :
            Sortie : Le nombre d'arcs partant d'un sommet s (int) """
        degre = 0
        for i in range(self.ordre):
            if self.matrice[s][i] >= 1: degre += 1
        return degre

    def est_simple(self):
        """ renvoie True si le graphe est simple, False sinon.
            Entrée :
            Sortie : Booléen"""
        for i in self.matrice:
            for j in i:
                if j > 1: return False
        return True

    def affichage(self):
        """ propose un affichage dans la console du graphe sous la forme :
            0 -> [1, 3]
            1 -> [2, 3]
            2 -> []
            3 -> [1]
            Entrée :
            Sortie : Une chaine (str)"""
            
        sortie = f"      |"
        for i in range(self.ordre): sortie += f' s{i}' 
        sortie += "|\n"
                
        for i in range(self.ordre):
            sortie += f's{i} -> |'
            for j in self.matrice[i]: sortie += f' {j} '
            sortie += "|\n"
        return sortie

    def est_oriente(self):
        """ renvoie True si le graphe est orienté, False sinon.
            Entrée :
            Sortie : Booléen """
        for i in range(self.ordre):
            for j in range(i):
                if self.matrice[i][j] != self.matrice[j][i]:
                    return True
        return False

    def arcs(self):
        """ renvoie le nombre d'arcs ou d'arêtes du graphe.
            Entrée :
            Sortie : """
        arcs = 0
        for i in self.matrice:
            for j in i:
                if j > 0: arcs += j
        return arcs 

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
        for i in range(self.ordre):
            for j in range(self.ordre):
                if self.matrice[i][j] == 0 and i != j:
                    return False
        return True
        


if __name__ == "__main__":
    
    print('#####################################################################\n')
    
    graphe = Graphe_V1(6, [[0, 1, 0, 0, 1, 0],
                           [1, 0, 1, 1, 0, 0],
                           [0, 1, 0, 1, 0, 1],
                           [0, 1, 1, 0, 1, 1],
                           [1, 0, 0, 1, 0, 0],
                           [0, 0, 1, 1, 0, 0]])


    assert graphe.degre(0) == 2, "degré = 2"
    graphe.ajouter_arc(0, 0)
    assert graphe.matrice[0][0] == 1, "Il est supposé être à 1"

    print(graphe.affichage())

    assert graphe.est_adjacent(0,1), "Ils sont adjacents"

    assert graphe.voisins(1) == [0, 2, 3], "0,2,3 sont ses voisins"
    assert graphe.degre(1) == 3, "degré = 3"

    assert graphe.voisins(0) == [0, 1, 4], "0,1,4 sont ses voisins"
    assert graphe.degre(0) == 3, "degré = 3"

    assert graphe.est_simple(), "il est simple"

    assert not graphe.est_oriente(), "il n'est pas orienté"
    assert graphe.arcs() == 17, "il y a 17 arcs"

    graphe.ajouter_arc(1, 0)
    assert graphe.matrice[1][0] == 2, "Il est supposé être à 2"

    graphe.supprimer_arc(0, 0)
    assert graphe.matrice[0][0] == 0, "Il est supposé être à 0"

    print(graphe.affichage())

    assert not graphe.est_complet(), "il n'est pas complet"
    
    print('#####################################################################\n')
    
    graphe = Graphe_V1(6)
    
    print(graphe.affichage())
    
    for i in range(graphe.ordre):
        for j in range(graphe.ordre):
            if i != j:
                graphe.ajouter_arc(i, j)
            
    print(graphe.affichage())
    assert graphe.est_complet(), "il est complet"

    print("tous les tests sont validés")
