from noeud import Noeud
import numpy as np
from matplotlib import pyplot as plt
n2 = Noeud(2, [])
n3 = Noeud("y",[])
n1 = Noeud("+",[n2,n3])

n = Noeud("exp",[n1])
#n.ajouter_noeud()
print(n.afficher())
d = {"y" : 5}
print(n.evaluer(d))
valeurs_y = np.linspace(-2, 2, 100)
n.tracer("y", valeurs_y)