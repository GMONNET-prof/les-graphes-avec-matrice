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
        self.dico[s] = []

    def ajouter_arc(self, s1, s2):
        """ ajoute s2 à la liste d'adjacence de s1. """
        if not s2 in self.dico[s1]:
            self.dico[s1].append(s2)
            
            
    def est_adjacent(self, s1, s2):
        """ renvoie True si s1 et s2 sont adjacents, False sinon.
            Entrée :
            Sortie : """
        if s1 in self.dico[s2] or s2 in self.dico[s1]:
            return True
        return False

    def sommets(self):
        """ renvoie la liste des sommets du graphe. 
            Entrée :
            Sortie : """
        liste_sommets = []
        for i in self.dico :
            liste_sommets += [i]
        return liste_sommets
            

    def ordre(self):
        """ renvoie l'ordre du graphe. 
            Entrée :
            Sortie : """
        ordre_graphe = 0
        for i in range(len(self.dico)):
            ordre_graphe += 1
        return ordre_graphe
            

    def voisins(self, s):
        """ renvoie la liste des voisins du sommet s.
            Entrée :
            Sortie : """
        return self.dico[s]

    def degre(self, s):
        """ renvoie le degré du sommet s.
            Entrée :
            Sortie : """
        degre_graphe = 0
        for i in range(len(self.dico[s])):
            degre_graphe += 1 
        return degre_graphe
            

    def est_simple(self):
        """ renvoie True si le graphe est simple, False sinon. 
            Entrée :
            Sortie : """
        ## test des boucles
        for cle in self.dico :
            liste_voisin = self.dico[cle]
            for i in range(len(liste_voisin)):
                valeur = liste_voisin[i]
                if valeur in liste_voisin[0:i]:
                    print(valeur, liste_voisin,"!")
                    
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
        chaine_finale = ""
        for cle in self.dico:
            chaine_finale += f"{cle} : {self.dico[cle]},\n"
        return chaine_finale

    def est_oriente(self):
        """ renvoie True si le graphe est orienté, False sinon. 
            Entrée :
            Sortie : """
        for cles,valeurs in self.dico.items():
            for valeur in valeurs:
                if not cles in self.dico[valeur]:
                    return True
        return False

    def arcs(self):
        """ renvoie le nombre d'arcs ou d'arêtes du graphe.
            Entrée :
            Sortie : """
        arcs = 0
        for valeurs in self.dico.values():
            arcs += len(valeurs)
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
        taille = len(self.dico)
        if not self.est_simple():
            return False
        for valeur in self.dico.values():
            if len(valeur) != taille-1:
                return False
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
    
    
    graphe_4 = Graphe_V2({1:[2, 3, 3],
                          2:[1, 3],
                           3:[1, 2]})


    assert graphe_1.est_adjacent("A", "B") == True , "est adjacent ne fonctionne pas"
    assert graphe_1.est_adjacent("A", "D") == False , "est adjacent ne fonctionne pas"
    assert graphe_1.sommets() == ["A","B","C","D","F","H"] , "sommets ne fonctionne pas"
    assert graphe_1.sommets() != ["A","B","C","D","H"] , "sommets ne fonctionne pas"
    assert graphe_1.ordre() == 6 , "ordre ne fonctionne pas"
    assert graphe_1.voisins("A") == ["B","F"] , "voisins ne fonctionne pas"
    assert graphe_1.degre("A") == 2 ,"degre ne fonctionne pas"
    assert graphe_1.est_simple() == True , "est simple ne fonctionne pas"
    print(graphe_4.est_simple())
    # assert graphe_4.est_simple() == False , "est simple ne fonctionne pas"
    print(graphe_1.affichage())
    
    print("Les test sont réussis")