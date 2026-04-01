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
        liste=[]
        for valeur in self.dico:
            liste.append(valeur)
        return liste

    def ordre(self):
        """ renvoie l'ordre du graphe. 
            Entrée :
            Sortie : """
        ordre=0
        for cle in self.dico:
            ordre+=1
        return ordre

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
            for valeur in self.dico[cle]:
                if valeur== cle:
                    return False
        ## test des doublons
        for cle2 in self.dico:
            liste=self.dico[cle2]
            i=0
            doublon=0
            for valeur in self.dico[cle2]:
                if valeur==liste[i]:
                    doublon+=1
                if doublon>1:
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
        chaine=""
        for cle in self.dico:
            chaine+= str(cle)+" : {"
            for valeur in self.dico[cle]:
                chaine+=str(valeur)+","
            chaine=chaine[0:-1]+"} \n"
        
        return chaine

    def est_oriente(self):
        """ renvoie True si le graphe est orienté, False sinon. 
            Entrée :
            Sortie : """
        for cle in self.dico.keys():
            for voisin in self.dico[cle]:
                if cle not in self.dico[voisin]:
                    return True
        return False

    def arcs(self):
        """ renvoie le nombre d'arcs ou d'arêtes du graphe.
            Entrée :
            Sortie : """
        arc=0
        for cle in self.dico:
                arc+=len(self.dico[cle])
        return arc
            

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
        for cle in self.dico:
            
            if len(self.dico)-1!=len(self.dico[cle]):
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
    assert Graphe_V2.est_adjacent(graphe_1,"A","F")==True,"s1 et s2 sont adgacent"
    assert Graphe_V2.sommets(graphe_1)==['A', 'B', 'C', 'D', 'F', 'H'],"les sommets ne sont pas correcte"
    assert Graphe_V2.ordre(graphe_1)==6,"L'ordre est de 6"
    assert Graphe_V2.voisins(graphe_1,"A")==['B', 'F'],"les voisin de A sont B et F"
    assert Graphe_V2.degre(graphe_1,"B")==3,"Le nombre d'arcs partant d'un sommet s n'set pas correcte"
    assert Graphe_V2.est_simple(graphe_1)==True,"est simple"
    print(Graphe_V2.affichage(graphe_1))
    assert Graphe_V2.est_oriente(graphe_1)==False,"graphe_1 est pas orienté"
    assert Graphe_V2.arcs(graphe_1)==16,"il y a 16 arcs au total"
    Graphe_V2.supprimer_arc(graphe_1,"B","C")
    assert Graphe_V2.arcs(graphe_1)==15,"il y a 15 arcs au total"
    assert Graphe_V2.est_complet(graphe_1)==False,"le graphe n'est pas complet"
    
    
    assert Graphe_V2.est_adjacent(graphe_2,1,3)==True,"s1 et s2 sont adgacent"
    assert Graphe_V2.sommets(graphe_2)==[1,2,3,4,5],"les sommets ne sont pas correcte"
    assert Graphe_V2.ordre(graphe_2)==5,"L'ordre est de 5"
    assert Graphe_V2.voisins(graphe_2,1)==[2,3,4],"les voisin de 1 sont 2, 3 et 4"
    assert Graphe_V2.degre(graphe_2,2)==0,"Le nombre d'arcs partant d'un sommet s n'est pas correcte"
    assert Graphe_V2.est_simple(graphe_2)==True,"est simple"
    print(Graphe_V2.affichage(graphe_2))
    assert Graphe_V2.est_oriente(graphe_2)==True,"graphe_2 est orienté"
    assert Graphe_V2.arcs(graphe_2)==8,"il y a 8 arcs au total"
    Graphe_V2.supprimer_arc(graphe_2,1,4)
    assert Graphe_V2.arcs(graphe_2)==7,"il y a 7 arcs au total"
    assert Graphe_V2.est_complet(graphe_2)==False,"le graphe n'est pas complet"
    
    assert Graphe_V2.est_adjacent(graphe_3,1,3)==True,"s1 et s2 sont adgacent"
    assert Graphe_V2.sommets(graphe_3)==[1,2,3],"les sommets ne sont pas correcte"
    assert Graphe_V2.ordre(graphe_3)==3,"L'ordre est de 5"
    assert Graphe_V2.voisins(graphe_3,1)==[2,3],"les voisin de 1 sont 2, 3 et 4"
    assert Graphe_V2.degre(graphe_3,2)==2,"Le nombre d'arcs partant d'un sommet s n'est pas correcte"
    assert Graphe_V2.est_simple(graphe_3)==True,"n'est pas simple"
    print(Graphe_V2.affichage(graphe_3))
    assert Graphe_V2.est_oriente(graphe_3)==False,"graphe_2 est pas orienté"
    assert Graphe_V2.arcs(graphe_3)==6,"il y a 8 arcs au total"
    assert Graphe_V2.est_complet(graphe_3)==True,"le graphe est complet"
    Graphe_V2.supprimer_arc(graphe_3,1,2)
    assert Graphe_V2.arcs(graphe_3)==5,"il y a 7 arcs au total"
    
    print("tous les tests sont validés")