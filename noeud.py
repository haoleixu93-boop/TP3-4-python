import math
from matplotlib import pyplot as plt

class Noeud : 
    def __init__(self, noeud, liste_noeud):
        self.noeud = noeud
        self.liste_noeud = liste_noeud

    def ajouter_noeud(self, n):
        if not isinstance (n, Noeud):
            raise TypeError("Il faut un noeud en paramètre !")
        self.liste_noeud.append(n)

    def afficher(self):
        res = str(self.noeud)
        for enfant in self.liste_noeud:
            res = res + " " + enfant.afficher()
        return res


    def evaluer(self, d):
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
        y = []
        for v in l:
            res = self.evaluer({c: v})
            y.append(res)
        plt.plot(l, y)
        plt.xlabel(c)
        plt.ylabel("f(" + c + ")")
        plt.grid(True)
        plt.show()

