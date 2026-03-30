class Graphe_V1:

    def __init__(self, n, liste=None):
        """Constructeur : crée une matrice n x n."""
        self.ordre = n
        if liste is None:
            self.matrice = [[0]*n for i in range(n)]
        else:
            
            self.matrice = liste

    def ajouter_arc(self, s1, s2):
        """Incrémente le coefficient de s1 à s2 de 1."""
        self.matrice[s1][s2] += 1

    def est_adjacent(self, s1, s2):
        """Renvoie True si s1 et s2 sont adjacents."""
        return self.matrice[s1][s2] > 0

    def voisins(self, s):
        """ renvoie la liste des voisins du sommet s.
            Entrée :
            Sortie : liste des voisin"""
        liste = []
        for i in range(self.ordre) :
            if self.matrice[s][i] > 0:
                liste.append(i)
        return liste 
            

    def degre(self, s):
        """ renvoie le degré du sommet s.
            Entrée :
            Sortie : nombre de liaison du sommet """
        compt = 0
        for i in range(self.ordre) :
            if self.matrice[s][i] > 0:
                compt += 1
        return compt 

    def est_simple(self):
        """ renvoie True si le graphe est simple, False sinon.
            Entrée :
            Sortie : bool"""
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
        chaine = ""
        for i in range(self.ordre):
            resultat = self.voisins(i)
            chaine += str(i) + "--->"+ str(resultat) +"\n"
        return chaine 
        
    def est_oriente(self):
        """ renvoie True si le graphe est orienté, False sinon.
            Entrée :
            Sortie : """
        for i in range(self.ordre):
            for j in range(self.ordre):
                if self.matrice[i][j] != self.matrice[j][i] :
                    return False
        return True
                
    def arcs(self):
        """ renvoie le nombre d'arcs ou d'arêtes du graphe.
            Entrée :
            Sortie : """
        compt = 0 
        for i in range(self.ordre):
            for j in range(self.ordre):
                if self.matrice[i][j] > 0:
                    compt += self.matrice[i][j]
        return compt 

    def supprimer_arc(self, s1, s2):
        """ décrémente le coefficient de s1 à s2 de 1 dans la matrice.
            ne fait rien si s1 et s2 n'étaient pas adjacents.
            Entrée :
            Sortie : """
        if self.est_adjacent(s1, s2):
            self.matrice[s1][s2] -= 1

    def est_complet(self):
        """ renvoie True si le graphe est complet, False sinon.
            Entrée :
            Sortie : """
        if self.est_simple() == False:
            return False
        else:
            for i in range(self.ordre):
                for j in range(self.ordre):
                    if i != j:
                        if self.matrice[i][j] == 0:
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
    # TESTS GRAPHE 1
    assert graphe_1.voisins(2) == [1, 3, 5]
    assert graphe_1.degre(2) == 3 ,"le nombre de liaison partant de S3 n'est pas correcte "
    assert graphe_1.est_simple() == True ,"le graphe 1 est simple "
    print(graphe_1.affichage())
    assert graphe_1.est_oriente() == True ,"le graphe 1 est oriente "
    assert graphe_1.arcs() == 16 ,"le nombre d'arc du graphe n'est pas correcte "
    assert graphe_1.est_complet() == False ,"le graphe 1 n'est pas complet "
    
    # TESTS GRAPHE 2
    assert graphe_2.voisins(4) == []
    print(graphe_2.affichage())
    assert graphe_2.est_simple() == True ,"le graphe 2 est simple "
    assert graphe_2.est_complet() == False ,"le graphe 2 n'est pas complet "
    
    # TESTS GRAPHE 3
    assert graphe_3.est_oriente() == True ,"le graphe 3 est oriente "
    assert graphe_3.arcs() == 6 ,"le nombre d'arc du graphe n'est pas correcte "
    assert graphe_3.est_complet() == True ,"le graphe 3 est complet "
    print(graphe_3.affichage())
    
    print("tous les tests sont validés")
