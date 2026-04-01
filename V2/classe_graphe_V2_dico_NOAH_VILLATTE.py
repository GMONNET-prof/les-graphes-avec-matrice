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
        if s2 in self.dico[s1]:
            return True
        return False
            

    def sommets(self):
        """ renvoie la liste des sommets du graphe. 
            Entrée :
            Sortie : """
        total=[]
        for i in self.dico.keys():
            total.append(i)
        return total            

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
        total=0
        for i in self.dico[s]:
            total+=1
        return total
    
    def est_simple(self):
        """ renvoie True si le graphe est simple, False sinon. 
            Entrée :
            Sortie : """
        ## test des boucles
        for i,j in self.dico.items():
            temp=[]
            for double in j:
                
                if double in temp or double==i:
                    return False
                else:
                    temp.append(double)
        return True   
        ## test des doublons
        

    def affichage(self):
        
        """ propose un affichage dans la console du graphe sous la forme :
            0 : {1, 3}
            1 : {2, 3}
            2 : {}
            3 : {1} 
            Entrée :
            Sortie : """
            
        for i,j in self.dico.items():
            print(i,"---->",j)
                
            
                

    def est_oriente(self):
        """ renvoie True si le graphe est orienté, False sinon. 
            Entrée :
            Sortie : """
        for i,j in self.dico.items():
            for val in j:
                if i not in self.dico[val]:
                    return False
        return True

    def arcs(self):
        """ renvoie le nombre d'arcs ou d'arêtes du graphe.
            Entrée :
            Sortie : """
        compteur=0
        for i,j in self.dico.items():
            compteur+=len(j)
        return compteur
    def supprimer_arc(self, s1, s2):
        """ Supprime s2 de la liste d'adjacence de s1.
            ne fait rien si s1 et s2 n'étaient pas adjacents.
            Entrée :
            Sortie : """
        if self.est_adjacent(s1, s2)==True:
            for i,j in self.dico.items():
                for val in j:
                    if val==s2:
                        j.remove(val)
            
                

    def est_complet(self):
        """ renvoie True si le graphe est complet, False sinon.
            Entrée :
            Sortie : """
        if self.est_simple()==True:
            for i,j in self.dico.items():
                if len(j)!=(self.ordre()-1):
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
   
    graphe_4= Graphe_V2({1:[2, 3],
                          2:[1, 3],
                          3:[1, 2,]})
    
    
    graphe_1.affichage()
    assert graphe_1.ordre()==6, "erreur, c'est égal à 6"
    assert graphe_1.est_adjacent("A", "D")==False, "erreur, ils ne sont pas adjacent"
    assert graphe_1.voisins("B")==['A','C','D'], "erreur, c'est égal à ['A','C','D']"
    assert graphe_3.est_simple()==True, "erreur, il est simple"
    assert graphe_2.est_complet()==False, "erreur, il est pas complet"
    assert graphe_3.est_oriente()==True, "erreur, il est orienté"
    assert graphe_2.degre(3)==3, "erreur, c'est égal à 3"
    assert graphe_1.arcs()==16, "erreur, c'est égal à 16"
    
    print("#####################################")
    graphe_1.supprimer_arc("A", "B")
    graphe_1.affichage()