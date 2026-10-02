import math
from matplotlib import pyplot as plt

class Noeud : 
    """ Représente la classe Noeud d'une arbre d'expression """
    def __init__(self, noeud, liste_noeud) :
        """ Constructeur de la classe Noeud.
        Paremètres : 
        ---------------------
        noeud : Noeud
        liste : liste[Noeud] 
        """
        self.noeud = noeud
        self.liste_noeud = liste_noeud

    def ajouter_noeud(self, n):
        """ Ajoute un noeud dans la liste des noeuds.
        Paramètres :
        --------------------
        n : Noeud
        """
        if not isinstance (n, Noeud):
            raise TypeError("Il faut un noeud en paramètre !")
        self.liste_noeud.append(n)

    def afficher(self):
        """Afficher l'expression mathématique.

        Returns:
            str: L'expression mathématique sous forme d'une affichage polonais.
        """
        res = str(self.noeud)
        for enfant in self.liste_noeud:
            res = res + " " + enfant.afficher()
        return res


    def evaluer(self, d)->float:
        """Evaluer l'expression symbolique pour une combinaison données des variables de l'expression.

        Paramètres:
            d (dict[str, int|float]): Contient les valeurs associées aux noms des variables.

        Raises:
            ValueError: LA variable n'est pas dans le dictionnaire d.
            ValueError: Division par 0.
            ValueError: Le logarithme exige une valeur strictement positive.
            ValueError: Opérateur inconnu.

        Returns:
            float : Le résultat de l'expression symbolique.
        """
        if isinstance(self.noeud, (int, float)):
            return float(self.noeud)

        if len(self.liste_noeud) == 0:
            var = str(self.noeud)
            if var not in d:
                raise ValueError(f"La variable '{var}' n'est pas dans le dictionnaire !")
            return float(d[var])

        liste = []
        for enfant in self.liste_noeud:
            valeur = enfant.evaluer(d)
            liste.append(valeur)

        op = self.noeud

        if op == '+':
            return liste[0] + liste[1]
        elif op == '-' :
            return liste[0] - liste[1]
        elif op == '*':
            return liste[0] * liste[1]

        elif op == '/':
            if liste[1] == 0:
                raise ValueError("Division par zéro.")
            return liste[0] / liste[1]

        elif op == 'exp':
            return math.exp(liste[0])
        elif op == 'log':
            if liste[0] <= 0:
                raise ValueError("Le logarithme exige une valeur strictement positive.")
            return math.log(liste[0])
        elif op == 'sin':
            return math.sin(liste[0])
        elif op == 'cos':
            return math.cos(liste[0])

        else:
            raise ValueError("Opérateur inconnu")

    def tracer(self,c,l):
        """Tracer la fonction correspondant à l'expression symbolique.

        Paramètres:
            c (str): Variable qu'on souhaite tracer.
            l (liste[int|float]): Liste de valeurs prises par c.
        """
        y = []
        for v in l:
            res = self.evaluer({c: v})
            y.append(res)
        plt.plot(l, y)
        plt.xlabel(c)
        plt.ylabel("f(" + c + ")")
        plt.grid(True)
        plt.show()

