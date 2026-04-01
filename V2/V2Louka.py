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
        self.dico[s1].append(s2)
            
            
            
    def est_adjacent(self, s1, s2):
        """ renvoie True si s1 et s2 sont adjacents, False sinon.
            Entrée :
            Sortie : """
        return s2 in self.dico[s1] and s1 in self.dico[s2]

    def sommets(self):
        """ renvoie la liste des sommets du graphe. 
            Entrée :
            Sortie : """
        return self.dico.keys()

    def ordre(self):
        """ renvoie l'ordre du graphe. 
            Entrée :
            Sortie : """
        return len(self.dico.keys())

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
        for keys,values in self.dico.items():
            if keys in values:
                return False
            for i in range(len(values)):
                if values[i] in values[:i]:
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
        sortie = ""
        for keys,values in self.dico.items(): sortie += f"{keys}  ->  {','.join(values)} \n"
        return sortie
            
            

    def est_oriente(self):
        """ renvoie True si le graphe est orienté, False sinon. 
            Entrée :
            Sortie : """
        for keys,values in self.dico.items():
            for value in values:
                if not keys in self.dico[value]:
                    return True
        return False

    def arcs(self):
        """ renvoie le nombre d'arcs ou d'arêtes du graphe.
            Entrée :
            Sortie : """
        arcs = 0
        for values in self.dico.values():
            arcs += len(values)
        return arcs

    def supprimer_arc(self, s1, s2):
        """ Supprime s2 de la liste d'adjacence de s1.
            ne fait rien si s1 et s2 n'étaient pas adjacents.
            Entrée :
            Sortie : """
        self.dico[s1].remove(s2)

    def est_complet(self):
        """ renvoie True si le graphe est complet, False sinon.
            Entrée :
            Sortie : """
        length = len(self.dico)
        if not self.est_simple(): return False
        for values in self.dico.values():
            if len(values) != length-1: return False
        return True


if __name__ == "__main__":
    graphe_1 = Graphe_V2({"A":list("BF"),
                          "B":list("ACD"),
                          "C":list("BDH"),
                          "D":list("BCFH"),
                          "F":list("AD"),
                          "H":list("CD")})
    
    print(graphe_1.affichage())
    
    
    assert graphe_1.est_adjacent("A", "C") == False, "C n'est pas adjacent de A"
    assert graphe_1.est_adjacent("A", "B") == True, "B est adjacent de A"
    
    
    assert ",".join(graphe_1.sommets()) == "A,B,C,D,F,H", 'les sommets sont "A,B,C,D,F,H"'
    assert graphe_1.ordre() == 6, "le graphe a pour ordre 6"
    
    
    assert ",".join(graphe_1.voisins("A")) == "B,F", "les voisins sont B,F"
    assert graphe_1.degre("A") == 2, "A a pour degré 2"
    
    
    assert graphe_1.est_simple() == True, "le graphe est simple"
    
    graphe_1.ajouter_arc("A", "B")
    assert graphe_1.est_simple() == False, "le graphe n'est plus simple"
    
    graphe_1.supprimer_arc("A","B")
    graphe_1.ajouter_arc("A", "A")
    assert graphe_1.est_simple() == False, "le graphe n'est plus simple"


    assert graphe_1.est_oriente() == False, "le graphe n'est pas orienté"

    graphe_2 = Graphe_V2({1:[2, 3, 4],
                          2:[],
                          3:[2, 4, 5],
                          4:[2, 5],
                          5:[]})
    
    assert graphe_2.est_oriente() == True, "le graphe est orienté"
    
    assert graphe_2.arcs() == 8, "le graphe a 8 arcs"
    
    assert graphe_2.est_complet() == False, "le graphe n'est pas complet"
    
    graphe_3 = Graphe_V2({1:[2, 3],
                          2:[1, 3],
                          3:[1, 2]})

    assert graphe_3.est_complet() == True, "le graphe est complet"
