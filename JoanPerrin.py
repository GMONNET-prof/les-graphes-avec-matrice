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
        if self.matrice[s1][s2] == self.matrice[s2][s1] or self.matrice[s1][s2] != 0 or self.matrice[s2][s1] != 0:
                return True
        return False

    def voisins(self, s):
        """ renvoie la liste des voisins du sommet s.
            Entrée :
            Sortie : Liste des voisins d'un sommet"""
        voi = [] 
        
        for i in range (self.ordre) : 
            if self.matrice[s][i] != 0:
                voi.append(i)
        return voi

    def degre(self, s):
        """ renvoie le degré du sommet s.
            Entrée :
            Sortie : Le nombre d'arcs partant d'un sommet s (int) """
        resultat = 0
        for elt in self.matrice[s]:
            resultat += elt
        return resultat

    def est_simple(self):
        """ renvoie True si le graphe est simple, False sinon.
            Entrée :
            Sortie : Booléen"""
        rang = 0
        for i in range(len(self.matrice)):
            for elt in self.matrice[i]:
                if elt != 0 and elt != 1:
                    return False
            rang +=1
        return True

    def affichage(self):
        """ propose un affichage dans la console du graphe sous la forme :
            0 -> [1, 3]
            1 -> [2, 3]
            2 -> []
            3 -> [1]
            Entrée :
            Sortie : Une chaine (str)"""
        aff = ""
        for i in range(len(self.matrice)):
            aff += f"{i}->{self.voisins(i)}"+"\n"
        return aff

    def est_oriente(self):
        """ renvoie True si le graphe est orienté, False sinon.
            Entrée :
            Sortie : Booléen """
        for i in range(len(self.matrice)):
            for j in range(i) :
                if self.matrice[i][j] != self.matrice[j][i] :
                    return True
        return False

    def arcs(self):
        """ renvoie le nombre d'arcs ou d'arêtes du graphe.
            Entrée :
            Sortie : """
        res = 0
        for i in range(self.ordre):
            for j in self.matrice[i] :
                res += j
        return res
    
    
    def supprimer_arc(self, s1, s2):
        """ décrémente le coefficient de s1 à s2 de 1 dans la matrice.
            ne fait rien si s1 et s2 n'étaient pas adjacents.
            Entrée :
            Sortie : """
        if self.est_adjacent(s1, s2) is True:
            self.matrice[s1][s2] -= 1
            
            
            
    def est_complet(self):
        """ renvoie True si le graphe est complet, False sinon.
            Entrée :
            Sortie : """
        if self.est_simple() is True :
            for i in range(self.ordre) :
                if self.voisins(i) == len(self.ordre):
                    return True
        return False

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
    assert graphe_3.affichage() == '0->[1, 2]\n1->[0, 2]\n2->[0, 1]\n' , "L'affichage ne fonctionne pas"
    assert graphe_3.degre(2) == 2 , "Degré ne fonctionne pas"
    assert graphe_3.est_adjacent(0, 1) == True , "Est adjacent ne fonctionne pas"
    assert graphe_3.arcs() == 6 , "arc ne fonctionne pas"
    assert graphe_3.est_oriente() == True , "oriente ne fonctionne pas"
    assert graphe_3.est_complet() == False ,"complet ne marche pas"
    print("tous les tests sont validés")
