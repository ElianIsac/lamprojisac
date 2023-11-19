
"""
Crea coordinate cubo, ruotate
"""

from math import sin, cos
import numpy as np
from SchermoPytamaro import LUNGHEZZA_RIGA, NUMERO_RIGHE, grafica_due_liste
import sys
sys.setrecursionlimit(1500)

SCALA = 70
ANGOLO = 0.3
offset = [LUNGHEZZA_RIGA/2, NUMERO_RIGHE/2]

matrice_proiezione = np.matrix([
    [1,0,0],
    [0,1,0]
])

ruota_y = np.matrix([
        [cos(ANGOLO), 0, sin(ANGOLO)],
        [0, 1, 0],
        [-sin(ANGOLO), 0, cos(ANGOLO)],
    ])

ruota_z = np.matrix([
        [cos(ANGOLO), -sin(ANGOLO), 0],
        [sin(ANGOLO), cos(ANGOLO), 0],
        [0, 0, 1],
    ])

ruota_x = np.matrix([
        [1, 0, 0],
        [0, cos(ANGOLO), -sin(ANGOLO)],
        [0, sin(ANGOLO), cos(ANGOLO)],
    ])

def crea_matrice_vertici() -> np.matrix:
    """
    Crea una matrice che contiene le coordinate di tutti i vertici per un cubo di lato 2
    :returns: Matrice spigoli
    """
    vertici =[]
    for x in (-1, 1): 
        for y in (-1, 1):
            for z in (-1, 1):
                vertici.append(np.matrix([x, y, z]))
    return vertici

def ruota_proietta_vertici(vertici: np.matrix) -> np.matrix:
    '''
    Crea una lista che contiene le coordinate dei vertici del cubo, dopo che è stata calcolata la loro rotazione per un certo angolo, e la proiezione ortogonale.
    :param vertici: I vertici del cubo in coordinate tridimensionali.
    :returns: Lista di coordinate in forma bidimensionale dei vertici ruotati e proiettati.
    '''
    coordinate_vertici = []
    for vertice in vertici:
        ruota3d = np.dot(ruota_y, vertice.reshape((3, 1)))
        ruota3d = np.dot(ruota_z, ruota3d)
        ruota3d = np.dot(ruota_x, ruota3d)
        punti_proiezione = np.dot(matrice_proiezione, ruota3d)
        x = int(punti_proiezione[0][0] * SCALA) + offset[0]
        y = int(punti_proiezione[1][0] * SCALA) + offset[1]
        coordinate_vertici.append([x, y])
    return coordinate_vertici

def crea_punti_linee(vertice1, vertice2, vertici):
    '''
    Crea una lista di punti che appartengono alla funzione retta che attraversa due vertici del cubo.
    :param vertice1: Uno dei due vertici che devono essere attraversati dalla retta.
    :param vertice2: Uno dei due vertici che devono essere attraversati dalla retta.
    :param vertici: Lista di coordinate dei vertici del cubo.
    :returns: Lista di punti che appartengono alla funzione retta che attraversa due vertici del cubo.
    '''
    punti_linee = []
    x1 = int(vertici[vertice1][0])
    y1 = int(vertici[vertice1][1])
    x2 = int(vertici[vertice2][0])
    y2 = int(vertici[vertice2][1])
    delta = (y2 - y1) / (x2 - x1)
    b = (delta * x1 - y1) * -1

    x_attuale = x1
    if x_attuale <= x2: 
        while x_attuale <= x2:
            y = delta * x_attuale + b
            punti_linee.append([int(x_attuale), int(y)])
            x_attuale += 0.01

    if x_attuale >= x2:
        while x_attuale >= x2:
            y = delta * x_attuale + b
            punti_linee.append([int(x_attuale), int(y)])
            x_attuale += -0.01

    return punti_linee

def main_grafica_vertici():
    grafica_vertici = crea_matrice_vertici()
    grafica_vertici = ruota_proietta_vertici(grafica_vertici)
    return grafica_vertici

def main_grafica_linee():
    vertici = main_grafica_vertici()
    linee = []
    linee.append(crea_punti_linee(0, 1, vertici))
    linee.append(crea_punti_linee(2, 0, vertici))
    linee.append(crea_punti_linee(2, 3, vertici))
    linee.append(crea_punti_linee(3, 1, vertici))

    linee.append(crea_punti_linee(4, 5, vertici))
    linee.append(crea_punti_linee(6, 4, vertici))
    linee.append(crea_punti_linee(6, 7, vertici))
    linee.append(crea_punti_linee(7, 5, vertici))

    linee.append(crea_punti_linee(0, 4, vertici))
    linee.append(crea_punti_linee(1, 5, vertici))
    linee.append(crea_punti_linee(2, 6, vertici))
    linee.append(crea_punti_linee(3, 7, vertici))
    return linee

grafica_due_liste(main_grafica_vertici(), main_grafica_linee())