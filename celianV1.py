class Graphe_V1:

    def __init__(self, n, liste = None):
        """ constructeur de la classe Graphe_V1.
            n est l'ordre du graphe et sera affecté à l'attribut ordre.
            l'attribut matrice sera un tableau python de dimension n x n
            dont les valeurs seront initialisées à zéro ou à liste. """
        self.ordre = n  # On crée l'attribut 'ordre'
    
        if liste is None:
            self.matrice = [[0 for i in range(n)] for i in range(n)]
        else:
            self.matrice = liste


    def ajouter_arc(self, s1, s2):
        """ incrémente le coefficient de s1 à s2 de 1 dans la matrice.
            Entrée :
            Sortie : """
        self.matrice[s1][s2] += 1

    def est_adjacent(self, s1, s2):
        """ renvoie True si s1 et s2 sont adjacents, False sinon.
            Entrée :
            Sortie : """
        return self.matrice[s1][s2] >= 1

    def voisins(self, s):
        """ renvoie la liste des voisins du sommet s.
            Entrée :
            Sortie : """
        liste_voisins = []
        for j in range(self.ordre):
            if self.matrice[s][j] > 0:
                liste_voisins.append(j)
        return liste_voisins
                
    def degre(self, s):
        """ renvoie le degré du sommet s.
            Entrée :
            Sortie : """
        degre = 0
        for j in range (self.ordre):
            if self.matrice[s][j] > 0:
                degre +=1
        return degre
    
    def degrebis(self, s):
        """ renvoie le degré du sommet s.
            Entrée :
            Sortie : """
        return len(self.voisins(s))

    def est_simple(self):
        """ renvoie True si le graphe est simple, False sinon.
            Entrée :
            Sortie : """
        for i in range(self.ordre):
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
            Sortie : """
        for i in range(self.ordre):
            v = self.voisins(i)
            print(i, "->", v)

    def est_oriente(self):
        """ renvoie True si le graphe est orienté, False sinon.
            Entrée :
            Sortie : """
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
        
        if self.est_oriente():
            return total
        else:
            return total // 2

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
        if not self.est_simple():
            return False
            
        for i in range(self.ordre):
            for j in range(self.ordre):
                # Si ce n'est pas la diagonale ET qu'il n'y a pas d'arc
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
    #ici commencent les tests
    ...
    
    print("tous les tests sont validés")
