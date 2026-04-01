# Bardia - Spécialité NSI Terminale - Classe Graphe V2
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
            Entrée : 2 Sommets
            Sortie : Booléen """
        if s2 in self.dico[s1] or s1 in self.dico[s2]:
            return True
        return False

    def sommets(self):
        """ renvoie la liste des sommets du graphe. 
            Entrée :
            Sortie : """
        sommets_a_return = []
        for sommet in self.dico.keys():
            sommets_a_return.append(sommet)
        return sommets_a_return

    def ordre(self):
        """ renvoie l'ordre du graphe. 
            Entrée :
            Sortie : """
        return len(self.sommets())

    def voisins(self, s):
        """ renvoie la liste des voisins du sommet s.
            Entrée :
            Sortie : """
        return self.dico[s]

    def degre(self, s):
        """ renvoie le degré du sommet s.
            Entrée :
            Sortie : """
        return len(self.voisins(s))

    def est_simple(self):
        """ renvoie True si le graphe est simple, False sinon. 
            Entrée :
            Sortie : """
            
        ## test des boucles
        for sommet, voisin in self.dico.items():
            if sommet in voisin:
                return False
       
        ## test des doublons
        verifier = []
        for vv in voisin:
            if vv in verifier:
                return False
            else:
                verifier.append(vv)
        return True
    
    def affichage(self):
        """ propose un affichage dans la console du graphe sous la forme :
            0 : {1, 3}
            1 : {2, 3}
            2 : {}
            3 : {1} 
            Entrée :
            Sortie : """
        for sommet in self.sommets():
            print(f"{sommet} : {self.voisins(sommet)}")

    def est_oriente(self):
        """ renvoie True si le graphe est orienté, False sinon. 
            Entrée :
            Sortie : """
        for s1 in self.sommets():
            for s2 in self.voisins(s1):
                if s1 != s2 and not self.est_adjacent(s2, s1):
                    return True
        return False


    def arcs(self):
        """ renvoie le nombre d'arcs ou d'arêtes du graphe.
            Entrée :
            Sortie : """
        somme = 0
        for voisins in self.dico.values():
            somme += len(voisins)
        return somme
        
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
        n = self.ordre()
        for sommet,voisins in self.dico.items():
            if sommet in voisins or len(voisins) != (n-1):
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



# G1
assert graphe_1.ordre() == 6
assert graphe_1.sommets() == ["A", "B", "C", "D", "F", "H"]
assert graphe_1.voisins("A") == ["B", "F"]
assert graphe_1.est_simple() is True
assert graphe_1.est_complet() is False
# graphe_1.affichage()

# G2
assert graphe_2.sommets() == [1, 2, 3, 4, 5]
assert graphe_2.ordre() == 5
assert graphe_2.est_adjacent(2, 4) is True
assert graphe_2.est_simple() is True
assert graphe_2.voisins(4) == [2, 5]
# print(graphe_2.arcs()) # Reponse attendue -> 8
assert graphe_2.est_complet() is False
# graphe_2.affichage()

# G3
assert graphe_3.ordre() == 3
assert graphe_3.voisins(1) == [2, 3]
assert graphe_3.sommets() == [1, 2, 3]
assert graphe_3.est_adjacent(1, 3) is True
assert graphe_3.est_simple() is True
# print(graphe_3.arcs()) # Reponse attendue -> 6
assert graphe_3.est_oriente() is False
assert graphe_3.est_complet() is True
# graphe_3.affichage()

print("Tous les tests sont validés")