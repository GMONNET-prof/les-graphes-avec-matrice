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
        if s2 in self.dico[s1] and s1 in self.dico[s2]:
            return True
        return False

    def sommets(self):
        """ renvoie la liste des sommets du graphe. 
            Entrée :
            Sortie : """
        liste_som = []
        for cle, valeur in self.dico.items():
            liste_som.append(cle)
        return liste_som

    def ordre(self):
        """ renvoie l'ordre du graphe. 
            Entrée :
            Sortie : """
        total = 0
        for cle, valeur in self.dico.items():
            total += 1
        return total

    def voisins(self, s):
        """ renvoie la liste des voisins du sommet s.
            Entrée :
            Sortie : """
        return self.dico[s]
            
    def degre(self, s):
        """ renvoie le degré du sommet s.
            Entrée :
            Sortie : """
        total = 0
        for i in self.dico[s]:
            total += 1
        return total

    def est_simple(self):
        """ renvoie True si le graphe est simple, False sinon. 
            Entrée :
            Sortie : """
        for cle, valeur in self.dico.items():
            if cle in valeur:
                return False
            double = []
            for v in valeur:
                if v in double:
                    return False
                double.append(v)
        return True

    def affichage(self):
        """ propose un affichage dans la console du graphe sous la forme :
            0 : {1, 3}
            1 : {2, 3}
            2 : {}
            3 : {1} 
            Entrée :
            Sortie : """
        affich = ""
        for cle, valeur in self.dico.items():
            affich += str(cle)
            affich += " : "
            affich += str(valeur)
            affich += "\n"
        return affich

    def est_oriente(self):
        """ renvoie True si le graphe est orienté, False sinon. 
            Entrée :
            Sortie : """
        longueur = len(self.dico) - 1
        for cle, valeur in self.dico.items():
            if len(valeur) != longueur:
                return True
        return False

    def arcs(self):
        """ renvoie le nombre d'arcs ou d'arêtes du graphe.
            Entrée :
            Sortie : """
        total = 0
        for cle, valeur in self.dico.items():
            for i in valeur:
                total += 1
        return total
            
    def supprimer_arc(self, s1, s2):
        """ Supprime s2 de la liste d'adjacence de s1.
            ne fait rien si s1 et s2 n'étaient pas adjacents.
            Entrée :
            Sortie : """
        if s2 in self.dico[s1]:
            self.dico[s1].remove(s2)

    def est_complet(self):
        """ renvoie True si le graphe est complet, False sinon.
            Entrée :
            Sortie : """
        if self.est_simple():
            for cle, valeur in self.dico.items():
                if len(valeur) != len(self.dico)-1:
                    return False
            return True 
        return False                   
                

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
    
    ####################
    #TEST GRAPHE 3
    ####################
    
    assert(graphe_3.est_adjacent(1, 2) == True), "Erreur, le point 1 et 2 sont adjacents"
    assert(graphe_3.sommets()==[1, 2, 3]), "Erreur, les sommets sont [1, 2, 3]"
    assert(graphe_3.ordre()==3), "Erreur, l'ordre est de 3"
    assert(graphe_3.voisins(1)==[2, 3]), "Erreur, les voisins de 1 sont 2 et 3"
    assert(graphe_3.degre(1)==2), "Erreur, le degre de 1 est de 2"
    assert(graphe_3.est_simple()==True), "Erreur, le graphe est simple"
    print(graphe_3.affichage())
    assert(graphe_3.est_oriente()==False), "Erreur, ce graphe est non orienté"
    assert(graphe_3.arcs()==6), "Erreur, il doit avoir 6 arcs"
    assert(graphe_3.est_complet()==True), "Erreur le graphe est complet"
    graphe_3.supprimer_arc(2, 3)
    print(graphe_3.affichage())
    assert(graphe_3.est_complet()==False), "Erreur le graphe n'est plus complet"
    print("tous les tests sont passés")
