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
            Entrée : Deux indices (int) entre 0 et (n-1)
            Sortie : booléen """
        if self.matrice[s1][s2] != 0 and self.matrice[s2][s1] != 0:
            return True
        return False

    def voisins(self, s):
        """ renvoie la liste des voisins du sommet s.
            Entrée : indice (int)
            Sortie : liste des voisins (list)"""
        liste_voisin = []
        for i in range(self.ordre):
            if self.matrice[s][i] != 0:
                liste_voisin.append(i)
        return liste_voisin

    def degre(self, s):
        """ renvoie le degré du sommet s.
            Entrée indice (int):
            Sortie : entier (int)"""
        som = 0
        for i in range(len(self.matrice[s])):
            som += self.matrice[s][i]
        return som

    def est_simple(self):
        """ renvoie True si le graphe est simple, False sinon.
            Entrée Aucune:
            Sortie : Booléen"""
        for i in range(self.ordre):
            for j in (self.matrice[i]):
                if j >= 2:
                    return False
        return True

    def affichage(self):
        """ propose un affichage dans la console du graphe sous la forme :
            0 -> [1, 3]
            1 -> [2, 3]
            2 -> []
            3 -> [1]
            Entrée : Aucune
            Sortie : chaine de caractere (str)"""
        affiche = ""
        for i in range(self.ordre):
            affiche += "\n"
            affiche += str(i)
            affiche += " -------> "
            for j in range(self.ordre):
                affiche += str(self.matrice[j][i])
                affiche += ", "
        return affiche

    def est_oriente(self):
        """ renvoie True si le graphe est orienté, False sinon.
            Entrée : Aucune
            Sortie : Booléen"""
        for i in range(self.ordre):
            for j in (self.matrice[i]):
                if self.matrice[j][i] != self.matrice[i][j]:
                    return False
        return True
                
                
                
                
    def arcs(self):
        """ renvoie le nombre d'arcs ou d'arêtes du graphe.
            Entrée : Aucune
            Sortie : entier (int)"""
        nombre = 0
        for i in range(self.ordre):
            for j in (self.matrice[i]):
                nombre += j
        return nombre

    def supprimer_arc(self, s1, s2):
        """ décrémente le coefficient de s1 à s2 de 1 dans la matrice.
            ne fait rien si s1 et s2 n'étaient pas adjacents.
            Entrée : Deux indices (int) entre 0 et (n-1)
            Sortie : Aucune Sortie"""
        if self.matrice[s1][s2] >= 1:
            self.matrice[s1][s2] -= 1 

    def est_complet(self):
        """ renvoie True si le graphe est complet, False sinon.
            Entrée : Aucune
            Sortie : Booléen"""
        cpt_indice_milieu = -1
        if self.est_simple():
            for i in range(self.ordre):
                cpt_indice_milieu += 1
                for j in range(self.ordre):
                    if i != cpt_indice_milieu and j != cpt_indice_milieu:
                        if self.matrice[i][j] == 0:
                            return False
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
    
    
    ###############
    #  GRAPHE 3
    ###############
    
    print(graphe_3.affichage())
    assert(graphe_3.est_simple()==True), "Erreur, le graphe est simple"
    graphe_3.ajouter_arc(1, 0)
    print(graphe_3.affichage())
    assert(graphe_3.est_adjacent(1, 0)==True), "Erreur, les indices 1 et 0 sont adjacents"
    assert(graphe_3.est_adjacent(0, 0)==False), "Erreur, 0 est pas adjacent avec lui meme"
    assert(graphe_3.voisins(1)==[0, 2]), "Erreur, 1 à pour voisin 1 et 2"
    assert(graphe_3.degre(2)==2), "Erreur, 2 à deux en degre"
    assert(graphe_3.est_simple()==False), "Erreur, le graphe est simple"
    assert(graphe_3.est_oriente()==False), "Erreur, le graphe est non orienté"
    assert(graphe_3.arcs()==7), "Erreur, le nombre d'arcs est de 7"
    graphe_3.supprimer_arc(1, 0)
    print(graphe_3.affichage())
    assert(graphe_3.est_complet()==True), "Erreur, la matrice est complet"
    
    
    
    print("tous les tests sont validés")
