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
        if s1 not in self.dico:
            self.ajouter_sommet(s1)
        self.dico[s1].append(s2)
            
            
    def est_adjacent(self, s1, s2):
        """ renvoie True si s1 et s2 sont adjacents, False sinon.
            Entrée :
            Sortie : """
        if s1 in self.dico:
            return s2 in self.dico[s1]
        return False

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
        for s in self.dico:
            ## Test des boucles 
            if s in self.dico[s]:
                return False
            ## Test des doublons 
            if len(self.dico[s]) != len(set(self.dico[s])):
                return False
        return True

    def affichage(self):
        """ propose un affichage dans la console du graphe sous la forme :
            0 : {1, 3}
            1 : {2, 3}
            2 : {}
            3 : {1} 
            Entrée :
            Sortie : """
        for s in self.dico:
            liste_v = self.dico[s]
            ensemble_v = set(liste_v)
            print(s, ":", ensemble_v)

    def est_oriente(self):
        """ renvoie True si le graphe est orienté, False sinon. 
            Entrée :
            Sortie : """
        for s1 in self.dico:
            for s2 in self.dico[s1]:
                if s1 not in self.dico[s2]:
                    return True
        return False

    def arcs(self):
        """ renvoie le nombre d'arcs ou d'arêtes du graphe.
            Entrée :
            Sortie : """
        compteur = 0
        for s in self.dico:
            liste_voisins = self.dico[s]
            compteur = compteur + len(liste_voisins)
        if self.est_oriente() == False:
            return compteur // 2
        else:
            return compteur

    def supprimer_arc(self, s1, s2):
        """ Supprime s2 de la liste d'adjacence de s1.
            ne fait rien si s1 et s2 n'étaient pas adjacents.
            Entrée :
            Sortie : """
        if self.est_adjacent(s1, s2):
            self.dico[s1].remove(s2)

    def est_complet(self):
        """ renvoie True si le graphe est complet, False sinon.
            Entrée :
            Sortie : """
        if not self.est_simple():
            return False
        n = self.ordre()
        for s in self.dico:
            if self.degre(s) != n - 1:
                return False
        return True

if __name__ == "__main__":
    #graphe 1 du cours :
    graphe_1 = Graphe_V2({"A":list("BF"),
                          "B":list("ACD"),
                          "C":list("BDH"),
                          "D":list("BCFH"),
                          "F":list("AD"),
                          "H":list("CD")})
    #graphe2 du cours (non simple):
    graphe_2 = Graphe_V2({"A":list("BCCCH"),
                          "B":list("AH"),
                          "C":list("AAAHFF"),
                          "D":list("E"),
                          "E":list("DEG"),
                          "F":list("CCFH"),
                          "G":list("EE"),
                          "H":list("ABCFH")})
    #graphe3 du cours (orienté):
    graphe_3 = Graphe_V2({1:[2, 3, 4],
                          2:[],
                          3:[2, 4, 5],
                          4:[2, 5],
                          5:[]})
    #graphe4 complet
    graphe_4 = Graphe_V2({1:[2, 3],
                          2:[1, 3],
                          3:[1, 2]})
