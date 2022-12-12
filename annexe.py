import numpy as np
import matplotlib.pyplot as plt


def graph(pourcentage, nb):
  x = np.linspace(pourcentage/100 - pourcentage/500, pourcentage/100 + pourcentage/500)
  y = np.log2(pow(nb, 2)/(2*np.log(1/(1-x))))
  
  plt.xlabel('Probabilité (en %)')
  plt.ylabel('Taille de la table de hachage (en bits)')
  
  plt.title("Taille de la table de hachage en fonction de la probabilité\nd'avoir une collision avec %i élément(s)." % nb)
  
  plt.plot(x, y, label='')
  plt.show()

pourcentage = float(input("Entrez le pourcentage à atteindre.\n>"))
nb = float(input("Entrez le nombre d'élément à faire pour atteindre cette probabilité.\n>"))
graph(pourcentage, nb)

res = np.ceil(pow(nb, 2)/(2*np.log(1/(1-pourcentage/100))))


print("Il faut {} élément(s) dans la table de hachage ({} bit(s))".format(int(res), int(np.ceil(np.log2(res)))))
