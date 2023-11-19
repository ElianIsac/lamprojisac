
"""
Questo modulo permette di creare una lista di coordinate del perimetro di un cerchio
"""
import sys
sys.setrecursionlimit(1500)
from math import sin, cos, pi
from SchermoPytamaro import passa_coordinate, LUNGHEZZA_RIGA, NUMERO_RIGHE, indaga_controlla

def chiedi_raggio_cerchio() -> int:
    """
    Chiede all'utente qual'è il raggio desiderato per il cerchio
    :returns: Raggio inserito
    """
    r = input("Inserire scelta raggio del cerchio: ")
    return r

def chiedi_risoluzione_cerchio() -> float:
    """
    Chiede all'utente qual'è la risoluzione desiderata per il cerchio
    :returns: Risoluzione inserita
    """
    risoluzione = float(input("Inserire scelta risoluzione del cerchio (Step Size): "))
    return risoluzione

def crea_lista_punti(risoluzione: float, r: int) -> list[list[int, int]]:
    """
    Crea la lista di punti del cerchio in base a un valore di risoluzione e raggio
    :param risoluzione: Risoluzione voluta
    :param r: Raggio voluto
    """
    offset =[LUNGHEZZA_RIGA/2, NUMERO_RIGHE/2]
    coordinate = []
    angolo = 0
    while angolo <= 2 * pi:
        coordinate.append([round((int(r) * cos(angolo)) + offset[0]), round((int(r) * sin(angolo)) + offset[1])])
        angolo += risoluzione
    return coordinate

def main_grafica_cerchio():
    raggio = chiedi_raggio_cerchio()
    risoluzione = chiedi_risoluzione_cerchio()
    punti = crea_lista_punti(risoluzione, raggio)
    passa_coordinate(punti)

main_grafica_cerchio()
