
#Exercice 1

import csv

def convert(dico):
    return {
        'longueur_petale': float(dico['petal_length']),
        'largeur_petale': float(dico['petal_width']),
        'espece': dico['species']
    }


#convert(table[1]) petal_length,petal_width,species

fichier = open("iris_data_set.csv")
table = list(csv.DictReader(fichier, delimiter=","))
iris = [convert(ligne) for ligne in table]
#print(iris)
fichier.close()

#print(table)
print(iris)

with open("NouveauFichier.csv", "w") as sortie:
    objet = csv.DictWriter(sortie,
                           ['longueur_petale', 'largeur_petale', 'espece'])

    objet.writeheader()

    objet.writerows(iris)

#Exercice 2


import matplotlib.pyplot as plt

fichier = open("NouveauFichier.csv")
table = list(csv.DictReader(fichier, delimiter=","))
X_iris_0 = [
    float(ligne['longueur_petale']) for ligne in table
    if ligne['espece'] == 'setosa'
]
Y_iris_0 = [
    float(ligne['largeur_petale']) for ligne in table
    if ligne['espece'] == 'setosa'
]

X_iris_1 = [
    float(ligne['longueur_petale']) for ligne in table
    if ligne['espece'] == 'versicolor'
]
Y_iris_1 = [
    float(ligne['largeur_petale']) for ligne in table
    if ligne['espece'] == 'versicolor'
]

X_iris_2 = [
    float(ligne['longueur_petale']) for ligne in table
    if ligne['espece'] == 'virginica'
]
Y_iris_2 = [
    float(ligne['largeur_petale']) for ligne in table
    if ligne['espece'] == 'virginica'
]
#print(iris)
fichier.close()
#print(X_iris_0)
#print(Y_iris_0)

#Exercice 3

plt.figure()
# Options de scatter : s = taille du point (20 par défaut), marker = symbole, on a
#  'o' : rond.
#  's' : carré (square).
#  '+' : croix en forme de +.
#  'x' : croix en forme de x.
# '*' : étoile.
# 'D' : losange (diamond).
#  'd' : losange allongé.
# 'H' : hexagone ('h' est aussi un hexagone, mais tourné).
# 'p' : pentagone.
# '.' : point.
# '>' : triangle vers la droite ('<' pour vers la gauche).
# 'v' : triangle vers le bas ('^' pour vers la haut).
# '|' : trait vertical ('_' pour trait horizontal).
#  '1' : croix à 3 branches vers le bas ('2' vers le haut, '3' vers la gauche, '4' vers la droite).

plt.scatter(X_iris_0, Y_iris_0, color='g', label='setosa', s=20, marker='*')
plt.scatter(
    X_iris_1, Y_iris_1, color='r', label='versicolor', s=20, marker='.')
plt.scatter(X_iris_2, Y_iris_2, color='b', label='virginica', s=20, marker='+')
plt.legend()


plt.xlabel('Longueur des pétales')
plt.ylabel('Largeur des pétales')
 
plt.savefig('plot.png')


plt.figure()
plt.scatter(X_iris_0, Y_iris_0, color='g', label='setosa', s=20, marker='*')
plt.scatter(
    X_iris_1, Y_iris_1, color='r', label='versicolor', s=20, marker='.')
plt.scatter(X_iris_2, Y_iris_2, color='b', label='virginica', s=20, marker='+')


plt.scatter(2, 0.5, color='orange', label='Iris 1', s=30, marker='v')


plt.scatter(2.5, 0.75, color='purple', label='Iris 2', s=30, marker='^')
plt.legend()


plt.xlabel('Longueur des pétales')
plt.ylabel('Largeur des pétales')
 
plt.savefig('plot2.png')

#Exercice 4

from math import sqrt
def d(xa,ya,xb,yb):
    return sqrt((xb-xa)**2+(yb-ya)**2)

# Pour trier une liste L de tuples par rapport à un élément, on utilise la fonction sorted et une clé
# trier/1er élément : sorted(L, key=lambda x: x[0])
# trier/2e élément : sorted(L, key=lambda x: x[1])
def knn(liste_dico,k,longueur,largeur):
    '''In : liste de dictionnaires, le paramètre k et la longueur et largeur de l'iris à tester
      Out : une liste des k plus proches voisins'''
    L=[]
    xb=longueur
    yb=largeur
    for dico in liste_dico:
        xa=dico['longueur_petale']
        ya=dico['largeur_petale']
        dist=d(xa,ya,xb,yb)
        label=dico['espece']
        L.append((dist,label))
    L=sorted(L,key=lambda x: x[0])
    return L[0:k]

#Exercice 5

def decision(liste_dico,k,longueur,largeur):
    '''In : liste de dictionnaires, le paramètre k et la longueur et largeur de l'iris à tester
      Out : l'espèce attribuée'''
    L=knn(liste_dico,k,longueur,largeur)
    compte=dict()
    for c in L:
        compte[c[1]]=0
    for c in L:
        compte[c[1]]=compte[c[1]]+1
    L=sorted(compte.items(), key=lambda t: t[1])
    return compte,L[-1][0]


k=10
longueur=2.5
largeur=0.75
     

dico={'Pierre':50,'Anatole':150,'Zaina':75}
L0=sorted(dico.items(), key=lambda t: t[0])
L1=sorted(dico.items(), key=lambda t: t[1])
#print(L0,L1)

liste_tuples=[(2.5,'Marc'),(12,'Bernard'),(100,'Carole')]


L0=sorted(liste_tuples, key=lambda t: t[0])


L1=sorted(liste_tuples, key=lambda t: t[1])
#print(L0,L1)