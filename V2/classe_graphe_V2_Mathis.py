class Graphe_V2:

    def __init__(self, dico_user = None):
        """ constructeur de la classe Graphe_v2.
            l'attribut dico sera un dictionnaire vide ou dico_user. """
        if dico_user is None:
            self.dico = {}
        else:
            self.dico = dico_user

    def ajouter_sommet(self, s):
        """ ajoute le sommet s dans le dictionnaire d'adjacence,
            avec une liste vide comme valeur. """
        if not s in self.dico:
            self.dico[s] = []

    def ajouter_arc(self, s1, s2):
        """ ajoute s2 à la liste d'adjacence de s1. """
        if not s2 in self.dico[s1]:
            self.dico[s1].append(s2)
            
            
    def est_adjacent(self, s1, s2):
        """ renvoie True si s1 et s2 sont adjacents, False sinon.
            Entrée :
            Sortie : """
        return s2 in self.dico[s1]

    def sommets(self):
        """ renvoie la liste des sommets du graphe. 
            Entrée :
            Sortie : """
        return list(self.dico.keys())

    def ordre(self):
        """ renvoie l'ordre du graphe. 
            Entrée :
            Sortie : """
        return len(self.dico)

    def voisins(self, s):
        """ renvoie la liste des voisins du sommet s.
            Entrée :
            Sortie : """
        return self.dico[s]

    def degre(self, s):
        """ renvoie le degré du sommet s.
            Entrée :
            Sortie : """
        return len(self.dico[s])

    def est_simple(self):
        """ renvoie True si le graphe est simple, False sinon. 
            Entrée :
            Sortie : """
        ## test des boucles
        for cle in self.dico:
            for m in self.dico[cle]:
                if cle == m:
                    return False
        ## test des doublons
        for j in self.dico:
            voisins = self.dico[j]
            if len(voisins) != len(set(voisins)):
                return False
        return True

    def affichage(self):
        chaine = ""
        for s in self.sommets():
            voisins = self.voisins(s)
            chaine += str(s) + " : " + str(voisins) + "\n"
        return chaine

    def est_oriente(self):
        """ renvoie True si le graphe est orienté, False sinon. 
            Entrée :
            Sortie : """
        for cle in self.dico:
            for voisin in self.dico[cle]:
                if cle not in self.dico[voisin]:
                    return True
        return False 
                    

    def arcs(self):
        """ renvoie le nombre d'arcs ou d'arêtes du graphe.
            Entrée :
            Sortie : """
        compt = 0
        for cle in self.dico:
            for valeur in self.dico[cle]:
                compt += 1
        return compt
            

    def supprimer_arc(self, s1, s2):
        """ Supprime s2 de la liste d'adjacence de s1.
            ne fait rien si s1 et s2 n'étaient pas adjacents.
            Entrée :
            Sortie : """
        if self.est_adjacent(s1, s2) is True :
            self.dico[s1].remove(s2)
            

    def est_complet(self):
        """ renvoie True si le graphe est complet, False sinon.
            Entrée :
            Sortie : """
        if self.est_simple() == False:
            return False
        ordre = len(self.dico)
        for cle in self.dico:
            if len(self.dico[cle]) != ordre - 1 :
                return False
            else:
                return True
            

if __name__ == "__main__":
    graphe_1 = Graphe_V2({"A":list("BF"),
                          "B":list("ACD"),
                          "C":list("BDH"),
                          "D":list("BCFH"),
                          "F":list("AD"),
                          "H":list("CD")})

    graphe_2 = Graphe_V2({1:[2, 3, 4],
                          2:[],
                          3:[2, 4, 5],
                          4:[2, 5],
                          5:[]})

    graphe_3 = Graphe_V2({1:[2, 3],
                          2:[1, 3],
                          3:[1, 2]})
    #ici commencent les tests
    # TESTS GRAPHE 1
    assert graphe_1.voisins("C") == ["B", "D", "H"]
    assert graphe_1.degre("C") == 3 ,"le nombre de liaison partant de S n'est pas correcte "
    assert graphe_1.est_simple() == True ,"le graphe 1 est simple "
    print(graphe_1.affichage())
    assert graphe_1.est_oriente() == False ,"le graphe 1 est oriente "

    # TESTS GRAPHE 2
    print(graphe_2.affichage())
    assert graphe_2.est_simple() == True ,"le graphe 2 est simple "
    assert graphe_2.est_complet() == False ,"le graphe 2 n'est pas complet "
    assert graphe_2.est_oriente() == True ,"le graphe 2 est oriente "
    assert graphe_2.degre(5) == 0 ,"le nombre de liaison partant de S n'est pas correcte "
     
    # TESTS GRAPHE 3
    print(graphe_3.affichage())
    assert graphe_3.est_oriente() == False ,"le graphe 3 est oriente "
    assert graphe_3.arcs() == 6 ,"le nombre d'arc du graphe n'est pas correcte "
    assert graphe_3.est_complet() == True ,"le graphe 3 est complet "
    assert graphe_3.degre(1) == 2 ,"le nombre de liaison partant de S n'est pas correcte "